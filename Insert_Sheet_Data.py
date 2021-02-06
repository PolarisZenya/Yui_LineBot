import sys
import gspread
import json
import time
from oauth2client.service_account import ServiceAccountCredentials as SAC
#=======================================================================
#import time
#=======================================================================
class Google_Sheet_DataBase:
    def __init__(self):
        self.GDriveJSON = 'cred.json'
        self.GSpreadSheet = 'LINEBOT'
        self.scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
        #給於驗證進去存取
        self.key = SAC.from_json_keyfile_name(self.GDriveJSON, self.scope)
        self.gc = gspread.authorize(self.key)

    def Sheet_Advice(self,userID,input_message):
        try:
            #第一張sheet -> get_worksheet(0)
            worksheet = self.gc.open(self.GSpreadSheet).get_worksheet(0)
            #抓資料

        #data抓表格 (full data)
            data = worksheet.get_all_records()
            #print(data)
            #print(len(data))
        #row為讀取某行資料(1,2,3...行)
            #row = worksheet.row_values(2)
            #print(row)
        #col為讀取某列資料(A,B,C...列)
            #col = worksheet.col_values(2)
            #print(col)
        #寫入資料(1,2,3...行)
            #worksheet.insert_row(row,3)
        #刪除資料(1,2,3...行)
            #worksheet.delete_row(3)
        #改變指定xy軸內容
            #worksheet.update_cell(1,2,"自定義軸")
            #numofRows = worksheet.row_count
            #print(numofRows)

        #抓目前時間 (EST時間)
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
            #print(str(row_str)+'已加入')
        
        except Exception as ex:
            print(type(ex),'\n發生錯誤，google sheet程式碼錯誤 --> \n', ex)
            sys.exit(1)

        return
#刪除建議 (progess=1)
    def Sheet_Advice_Del(self):
        worksheet = self.gc.open(self.GSpreadSheet).get_worksheet(0)
        #data抓表格 (full data)
        data = worksheet.get_all_records()
        #表格data為json格式0開始，del指令算行列的，中間相差2
        sheet_difference = 2
        for i in range(0,len(data)):
            if (data[i]['process'] == 1):
                worksheet.delete_row(i+sheet_difference)
                print("已刪除第"+str(i+sheet_difference)+"行")
                sheet_difference -= 1
        return
#取得資料庫所有資料-使用者
    def Data_Get_group(self):
        worksheet = self.gc.open(self.GSpreadSheet).get_worksheet(1)
        col = worksheet.col_values(1)
        return col
#取得資料庫所有資料-使用者權限
    def Data_Get_accesslvl(self):
        worksheet = self.gc.open(self.GSpreadSheet).get_worksheet(1)
        col = worksheet.col_values(4)
        return col
#加入新使用者與權限
    def Denied_Insert(self,userID,types,level,name):
        worksheet = self.gc.open(self.GSpreadSheet).get_worksheet(1)
        row_str = [userID,types,0,level,name]
        worksheet.append_row(row_str)
#改變該使用者權限或刪除此row
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