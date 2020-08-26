import sys
import gspread
import json
from oauth2client.service_account import ServiceAccountCredentials as SAC
GDriveJSON = 'cred.json'
GSpreadSheet = 'LINEBOT'
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
try:
    #給於驗證進去存取
    key = SAC.from_json_keyfile_name(GDriveJSON, scope)
    gc = gspread.authorize(key)
    worksheet = gc.open(GSpreadSheet).sheet1
    #抓資料

#data抓表格 (full data)
    #data = worksheet.get_all_records()
    #print(data)
#row為讀取某行資料(1,2,3...行)
    #row = worksheet.row_values(2)
    #print(row)
#col為讀取某行資料(A,B,C...列)
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

    row_str = ['來','抱抱']
    worksheet.append_row(row_str)
    print(str(row_str)+'已加入')
    
except Exception as ex:
    print(type(ex),'\n發生錯誤，程式碼錯誤 --> \n', ex)
    sys.exit(1)
    