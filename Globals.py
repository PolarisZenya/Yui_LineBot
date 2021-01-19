from Insert_Sheet_Data import *
#============================================================

Yui_denied_group  = Google_Sheet_DataBase().Data_Get_group()
Yui_denied_access = Google_Sheet_DataBase().Data_Get_accesslvl()

def Searcher(userID):
    for num in range(0,len(Yui_denied_group)):
        if userID == Yui_denied_group[num]:
            return num