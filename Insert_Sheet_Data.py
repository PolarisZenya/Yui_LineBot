import sys
import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials as SAC
GDriveJSON = 'cred.json'
GSpreadSheet = 'LINEBOT'
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
WaitSecond = 1
print('將資料記錄在試算表' ,GSpreadSheet , '每' ,WaitSecond ,'秒')
print('按下 Ctrl-C中斷執行')
while True:
    try:
        #給於驗證進去存取
        key = SAC.from_json_keyfile_name(GDriveJSON, scope)
        gc = gspread.authorize(key)
        worksheet = gc.open(GSpreadSheet).sheet1
        #抓資料

    #data抓表格 (full data)
        data = worksheet.get_all_records()
        print(data)
    #row為讀取某行資料(1,2,3...行)
        row = worksheet.row_values(2)
        print(row)
    #col為讀取某行資料(A,B,C...列)
        col = worksheet.col_values(2)
        print(col)
    #寫入資料(1,2,3...行)
        worksheet.insert_row(row,3)
    #刪除資料(1,2,3...行)
        worksheet.delete_row(3)
    #改變指定xy軸內容
        worksheet.update_cell(2,2,"自定義軸")
        numofRows = worksheet.row_count
        print(numofRows)


        time.sleep(WaitSecond)
    except Exception as ex:
        print('無法連線Google試算表', ex)
        sys.exit(1)
    