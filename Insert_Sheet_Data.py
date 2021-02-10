import sys
import gspread
import json
import time
from oauth2client.service_account import ServiceAccountCredentials as SAC
#=======================================================================
class Google_Sheet_DataBase:
    def __init__(self):
        self.GDriveJSON = 'cred.json'
        self.GSpreadSheet = 'LINEBOT'
        self.scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
        self.key = SAC.from_json_keyfile_name(self.GDriveJSON, self.scope)
        self.gc = gspread.authorize(self.key)

    def Sheet_Advice(self,userID,input_message):
        try:
            worksheet = self.gc.open(self.GSpreadSheet).get_worksheet(0)
            data = worksheet.get_all_records()

            localtime = time.localtime(time.time())
            localyear = localtime.tm_year
            localmon  = localtime.tm_mon
            localmday = localtime.tm_mday

            localhour = localtime.tm_hour
            if(localhour+8>24):
                localhour=localhour-16
            else:
                localhour=localhour+8
            localmin = localtime.tm_min

            row_str = [userID,0,input_message,localyear,localmon,localmday,localhour,localmin]
            worksheet.append_row(row_str)
        
        except Exception as ex:
            print(type(ex),'\n發生錯誤，google sheet程式碼錯誤 --> \n', ex)
            sys.exit(1)

        return

    def Sheet_Advice_Del(self):
        worksheet = self.gc.open(self.GSpreadSheet).get_worksheet(0)
        data = worksheet.get_all_records()
        sheet_difference = 2
        for i in range(0,len(data)):
            if (data[i]['process'] == 1):
                worksheet.delete_row(i+sheet_difference)
                print("已刪除第"+str(i+sheet_difference)+"行")
                sheet_difference -= 1
        return

    def Data_Get_group(self):
        worksheet = self.gc.open(self.GSpreadSheet).get_worksheet(1)
        col = worksheet.col_values(1)
        return col

    def Data_Get_accesslvl(self):
        worksheet = self.gc.open(self.GSpreadSheet).get_worksheet(1)
        col = worksheet.col_values(4)
        return col

    def Denied_Insert(self,userID,types,level,name):
        worksheet = self.gc.open(self.GSpreadSheet).get_worksheet(1)
        row_str = [userID,types,0,level,name]
        worksheet.append_row(row_str)

    def Denied_Change(self,userID,level):
        worksheet = self.gc.open(self.GSpreadSheet).get_worksheet(1)
        col = worksheet.col_values(1)
        if(level!=0):
            for i in range(0,len(col)):
                if (col[i] == userID):
                    worksheet.update_cell(i+1,4,level)
        else:
            for i in range(0,len(col)):
                if (col[i] == userID):
                    worksheet.delete_row(i+1)
                    print("使用權限：已刪除第"+str(i+1)+"行")