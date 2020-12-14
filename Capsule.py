
# 運算終端插件

#============================================================
import random
#============================================================
from FlexMessage import *
#============================================================
#進行計算

class Capsule_Cul:
    def __init__(self,event):
        #global變數，常駐池
        self.event = event
        self.SLIVER = {
            1  : ["碧",         'https://i.imgur.com/GUWnyhR.jpg'],
            2  : ["步未",       'https://i.imgur.com/64QRbRn.jpg'],
            3  : ["日和",       'https://i.imgur.com/YG2M4T4.jpg'],
            4  : ["優衣",       'https://i.imgur.com/OKxblyE.jpg'],
            5  : ["怜",         'https://i.imgur.com/vaZT3XY.jpg'],
            6  : ["依里",       'https://i.imgur.com/UVrAKpw.jpg'],
            7  : ["胡桃",       'https://i.imgur.com/vY9HMsP.jpg'],
            8  : ["鈴莓",       'https://i.imgur.com/hLo4Gft.jpg'],
            9  : ["優花梨",     'https://i.imgur.com/oktVSsF.jpg'],
            10 : ["美咲",       'https://i.imgur.com/6ylpuNE.jpg'],
            11 : ["莉瑪",       'https://i.imgur.com/jE7WUeE.jpg'],
        }
        self.GOLDEN = {
            1  : ["小雪",       'https://i.imgur.com/3mwQnjb.jpg'],
            2  : ["宮子",       'https://i.imgur.com/2bCb0bW.jpg'],
            3  : ["茜里",       'https://i.imgur.com/5fggvFf.jpg'],
            4  : ["美美",       'https://i.imgur.com/vIMZYNA.jpg'],
            5  : ["香織",       'https://i.imgur.com/ysxXX3F.jpg'],
            6  : ["鈴奈",       'https://i.imgur.com/qArOHSZ.jpg'],
            7  : ["美里",       'https://i.imgur.com/28hUCjZ.jpg'],
            8  : ["七七香",     'https://i.imgur.com/Gzjr1Ch.jpg'],
            9  : ["鈴",         'https://i.imgur.com/k4dHNCz.jpg'],
            10 : ["綾音",       'https://i.imgur.com/UM6N7Xf.jpg'],
            11 : ["紡希",       'https://i.imgur.com/RgTZpAx.jpg'],
            12 : ["深月",       'https://i.imgur.com/RAXPAhz.jpg'],
            13 : ["美冬",       'https://i.imgur.com/liPMffS.jpg'],
            14 : ["珠希",       'https://i.imgur.com/Vr84fSt.jpg'],
            15 : ["空花",       'https://i.imgur.com/p8wrI9i.jpg'],
            16 : ["千歌",       'https://i.imgur.com/dLk3NLx.jpg'],
            17 : ["真陽",       'https://i.imgur.com/zV28Aem.jpg'],
            18 : ["忍",         'https://i.imgur.com/vOUfEY9.jpg'],
            19 : ["惠理子",     'https://i.imgur.com/qVtdj0D.jpg'],
            20 : ["栞",         'https://i.imgur.com/ojeNzap.jpg'],
            21 : ["茉莉",       'https://i.imgur.com/h3VOI23.jpg']
        }
        self.COLOUR = {
            1  : ["杏奈",           'https://i.imgur.com/dMn5fZb.jpg'],
            2  : ["真步",           'https://i.imgur.com/GUTDc8E.jpg'],
            3  : ["璃乃",           'https://i.imgur.com/tmoLmFU.jpg'],
            4  : ["初音",           'https://i.imgur.com/mEaeUv2.jpg'],
            5  : ["霞",             'https://i.imgur.com/oJP4AVi.jpg'],
            6  : ["伊緒",           'https://i.imgur.com/ijleQFV.jpg'],
            7  : ["咲戀",           'https://i.imgur.com/77nKzA8.jpg'],
            8  : ["小望",           'https://i.imgur.com/MYVEygy.jpg'],
            9  : ["妮諾",           'https://i.imgur.com/1JTz0rk.jpg'],
            10 : ["秋乃",           'https://i.imgur.com/g0vX6bw.jpg'],
            11 : ["鏡華",           'https://i.imgur.com/1ww8OeH.jpg'],
            12 : ["智",             'https://i.imgur.com/qvJZ5It.jpg'],
            13 : ["真琴",           'https://i.imgur.com/WZE20Tz.jpg'],
            14 : ["伊莉亞",         'https://i.imgur.com/2MMZaDw.jpg'],
            15 : ["嘉夜",           'https://i.imgur.com/HlQ2Hlu.jpg'],
            16 : ["純",             'https://i.imgur.com/sJOjm6G.jpg'],
            17 : ["靜流",           'https://i.imgur.com/G3eOqQn.jpg'],
            18 : ["莫妮卡",         'https://i.imgur.com/F2G3bUR.jpg'],
            19 : ["流夏",           'https://i.imgur.com/QJGjmzo.jpg'],
            20 : ["吉塔",           'https://i.imgur.com/JYmWQdw.jpg'],
            21 : ["亞里莎",         'https://i.imgur.com/kwPUVoT.jpg'],
            22 : ["安",             'https://i.imgur.com/BaRggvy.jpg'],
            23 : ["古蕾雅",         'https://i.imgur.com/sm5CShx.jpg'],
            24 : ["江戶空花",       'https://i.imgur.com/tzPfVIq.jpg'],
            25 : ["江戶妮諾",       'https://i.imgur.com/3TBrKaS.jpg'],
            26 : ["學院碧",         'https://i.imgur.com/73oSybt.jpg'],
            27 : ["克蘿依",         'https://i.imgur.com/wbo5P0W.jpg'],
            28 : ["優妮",           'https://i.imgur.com/7xFJhQX.jpg'],
            29 : ["萬聖美美",       'https://i.imgur.com/c5B2ahO.jpg'],
            30 : ["露娜",           'https://i.imgur.com/kLRm0BK.jpg'],
            31 : ["魔法少女霞",     'https://i.imgur.com/kuC8w00.jpg'],
            32 : ["遊俠鈴",         'https://i.imgur.com/SrcLrD2.jpg'],
            33 : ["泳裝七七香",     'https://i.imgur.com/NtwFRbb.jpg'],
            34 : ["魔法少女莫妮卡", 'https://i.imgur.com/wqM3nMb.jpg'],
            35 : ["魔法少女智",     'https://i.imgur.com/pLBc5w7.jpg'],
        }
        #特別卡池加入常駐池
        self.PRINCESS_FES = {
            len(self.COLOUR)+1 : ["克莉絲提娜",     "https://i.imgur.com/NH3hSBS.jpg"],
            len(self.COLOUR)+2 : ["矛依未",         "https://i.imgur.com/LY5QG1n.jpg"],
            len(self.COLOUR)+3 : ["似似花",         "https://i.imgur.com/zcmcRtm.jpg"],
            len(self.COLOUR)+4 : ["公主佩可",       "https://i.imgur.com/TWBnp8l.jpg"],
            len(self.COLOUR)+5 : ["公主可可蘿",     "https://i.imgur.com/mK7ENgx.jpg"],
            len(self.COLOUR)+6 : ["公主優衣",       "https://i.imgur.com/mrWeXpE.jpg"],
            len(self.COLOUR)+7 : ["拉比林斯達",     "https://i.imgur.com/q3Ukoor.jpg"],
        }
        self.NEW_YEAR3 = {
            len(self.COLOUR)+1 : ["正月優衣",       "https://i.imgur.com/UPBXgCA.jpg"],
            len(self.COLOUR)+2 : ["正月日和",       "https://i.imgur.com/sDEnUAn.jpg"],
            len(self.COLOUR)+3 : ["正月凱留",       "https://i.imgur.com/zCb8mPU.jpg"],
            len(self.COLOUR)+4 : ["正月可可蘿",     "https://i.imgur.com/dEIAFgW.jpg"],
        }
        self.NEW_YEAR1 = {
            len(self.SLIVER)+1 : ["正月怜",         "https://i.imgur.com/iwJU38a.jpg"],
            len(self.SLIVER)+2 : ["正月鈴莓",       "https://i.imgur.com/PHwR3xA.jpg"],
        }
        self.VALENTINE_DAYS3 = {
            len(self.COLOUR)+1 : ["情人節靜流",     "https://i.imgur.com/Behlb85.jpg"],
        }
        self.VALENTINE_DAYS1 = {
            len(self.SLIVER)+1 : ["情人節惠理子",   "https://i.imgur.com/DKZfP5v.jpg"],
        }
        self.SUMMER3 = {
            len(self.COLOUR)+1 :  ["泳裝佩可",     "https://i.imgur.com/aidRbu9.jpg"],
            len(self.COLOUR)+2 :  ["泳裝鈴莓",     "https://i.imgur.com/22QESXh.jpg"],
            len(self.COLOUR)+3 :  ["泳裝珠希",     "https://i.imgur.com/4elbkEX.jpg"],
            len(self.COLOUR)+4 :  ["泳裝凱留",     "https://i.imgur.com/5mHuiKB.jpg"],
            len(self.COLOUR)+5 :  ["泳裝鈴奈",     "https://i.imgur.com/Stz7fEp.jpg"],
            len(self.COLOUR)+6 :  ["泳裝伊緒",     "https://i.imgur.com/zH6nnn0.jpg"],
            len(self.COLOUR)+7 :  ["泳裝咲戀",     "https://i.imgur.com/8cy3MMl.jpg"],
            len(self.COLOUR)+8 :  ["泳裝真步",     "https://i.imgur.com/xAj9KsD.jpg"],
            len(self.COLOUR)+9 :  ["泳裝真琴",     "https://i.imgur.com/W2312zm.jpg"],
            len(self.COLOUR)+10 : ["泳裝流夏",     "https://i.imgur.com/Nl86SKj.jpg"],
            len(self.COLOUR)+11 : ["泳裝初音",     "https://i.imgur.com/l7wIw0J.jpg"],
            len(self.COLOUR)+12 : ["泳裝純",       "https://i.imgur.com/JaGqH3u.jpg"],
        }
        self.SUMMER1 = {
            len(self.SLIVER)+1 : ["泳裝可可蘿",   "https://i.imgur.com/W5qc0Aj.jpg"],
            len(self.SLIVER)+2 : ["泳裝美冬",     "https://i.imgur.com/Nbav6zz.jpg"],
            len(self.SLIVER)+3 : ["泳裝香織",     "https://i.imgur.com/md53Rz5.jpg"],
            len(self.SLIVER)+4 : ["泳裝杏奈",     "https://i.imgur.com/Lw3Whaa.jpg"],
            len(self.SLIVER)+5 : ["泳裝美里",     "https://i.imgur.com/Xsx9MyN.jpg"],
        }
        self.HALLOWEEN3 = {
            len(self.COLOUR)+1 :  ["萬聖忍",      "https://i.imgur.com/mWSzYst.jpg"],
            len(self.COLOUR)+2 :  ["萬聖美咲",    "https://i.imgur.com/wR6CVPT.jpg"],
            len(self.COLOUR)+3 :  ["萬聖鏡華",    "https://i.imgur.com/7f68rro.jpg"],
            len(self.COLOUR)+4 :  ["萬聖美美",    "https://i.imgur.com/kqDSZ5Z.jpg"],
            len(self.COLOUR)+5 :  ["萬聖紡希",    "https://i.imgur.com/aJdcSOl.jpg"],
            len(self.COLOUR)+5 :  ["萬聖怜",      "https://i.imgur.com/tSqHgDM.jpg"],
        }
        self.HALLOWEEN1 = {
            len(self.SLIVER)+1 : ["萬聖宮子",     "https://i.imgur.com/Vj8NLwU.jpg"],
            len(self.SLIVER)+2 : ["萬聖禊",       "https://i.imgur.com/eRewNT9.jpg"],
            len(self.SLIVER)+3 : ["萬聖茉莉",     "https://i.imgur.com/amBlurG.jpg"],
        }
        self.CHRISTMAS3 = {
            len(self.COLOUR)+1 :  ["聖誕千歌",          "https://i.imgur.com/SzMJ5Lg.jpg"],
            len(self.COLOUR)+2 :  ["聖誕綾音",          "https://i.imgur.com/msMGSuH.jpg"],
            len(self.COLOUR)+3 :  ["聖誕伊莉亞",        "https://i.imgur.com/BAnveru.jpg"],
            len(self.COLOUR)+4 :  ["聖誕克莉絲提娜",    "https://i.imgur.com/ht6jH3G.jpg"],
            len(self.COLOUR)+5 :  ["聖誕秋乃",          "https://i.imgur.com/AzYjE2P.jpg"],
        }
        self.CHRISTMAS1 = {
            len(self.SLIVER)+1 : ["聖誕胡桃",     "https://i.imgur.com/dgBwIH9.jpg"],
            len(self.SLIVER)+2 : ["聖誕小望",     "https://i.imgur.com/0Q4mBY7.jpg"],
            len(self.SLIVER)+3 : ["聖誕優花梨",   "https://i.imgur.com/cCdgTkQ.jpg"],
        }
        self.WONDERLAND3 = {
            len(self.COLOUR)+1 : ["奇幻璃乃",     "https://i.imgur.com/3tNVJUy.jpg"]
        }
        self.WONDERLAND1 = {
            len(self.SLIVER)+1 : ["奇幻步未",     "https://i.imgur.com/7OhZOJ9.jpg"]
        }
        self.CINDERELLA3 = {
            len(self.COLOUR)+1 : ["卯月",     "https://i.imgur.com/4IaCxx4.jpg"],
            len(self.COLOUR)+1 : ["凜",       "https://i.imgur.com/XFnkt4g.jpg"],
        }
        self.CINDERELLA1 = {
            len(self.SLIVER)+1 : ["未央",     "https://i.imgur.com/BZVhIdz.jpg"]
        }
        self.ANGEL = {
            len(self.COLOUR)+1 : ["天使依里",       "https://i.imgur.com/5wwU6c5.jpg"],
            len(self.COLOUR)+1 : ["天使茜里",       "https://i.imgur.com/Pkw5EYT.jpg"],
        }
        self.CN = {
            len(self.COLOUR)+1 : ["橋本環奈",       "https://i.imgur.com/dPX4HBV.jpg"]
        }
        #存個備份值，大混池函數會打亂原先池，可以copy備份回去
        self.SLIVER_COPY = self.SLIVER.copy()
        self.COLOUR_COPY = self.COLOUR.copy()
        #彩卡光環位置存取值
        # top / offsetStart
        self.COLOUR_position = [300,300,300,300,300,300,300,300,300,300]

    def Ordinary_Draw(self,COL_Probability,COLOUR,SLIVER,NAME):
        if(COL_Probability>1000):
            COL_Probability = 1000
        #存亂數取出值
        card_rarity = [0]*10
        chara_name = [0]*10
        chara_picURL = [0]*10
        SLI = 0
        GOL = 0
        COL = 0
        for i in range (0,10):
            #從某稀有度抽一，flag抽稀有度 (彩2.5%，金18%，銀79.5%)
            SLIVER_num = random.randint(1,len(SLIVER))
            GOLDEN_num = random.randint(1,len(self.GOLDEN))
            #那個if/elif是在判斷特殊池，限定角色出現率在彩卡中提高
            if(len(self.COLOUR) != len(COLOUR)):
                random_num = random.randint(0,20)
                if(random_num<=7):
                    COLOUR_num = random.randint(len(self.COLOUR)+1,len(COLOUR))
                else:
                    COLOUR_num = random.randint(1,len(COLOUR))
            else:
                COLOUR_num = random.randint(1,len(COLOUR))
            flag = random.randint(1,1000)
            #第十抽保底金起跳
            if(i!=9):
                if(flag <= COL_Probability):
                    #彩卡光輝的位置
                    pos_counter = 51*i-3
                    if(pos_counter>=252):
                        pos_counter = 51*(i-5)-3
                    self.COLOUR_position[i] = pos_counter
                    COL += 1
                    card_rarity[i]  = 'https://i.imgur.com/u94s9So.png'
                    chara_name[i]   = COLOUR[COLOUR_num][0]
                    chara_picURL[i] = COLOUR[COLOUR_num][1]
                    #print("彩，"+ chara_name[i] +"，"+ chara_picURL[i])
                elif(flag <= COL_Probability+180):
                    GOL += 1
                    card_rarity[i] = 'https://i.imgur.com/pHfHyhV.png'
                    chara_name[i]   = self.GOLDEN[GOLDEN_num][0]
                    chara_picURL[i] = self.GOLDEN[GOLDEN_num][1]
                    #print("金，"+ chara_name[i] +"，"+ chara_picURL[i])
                else:
                    SLI += 1
                    card_rarity[i] = 'https://i.imgur.com/D9mJZp3.png'
                    chara_name[i]   = SLIVER[SLIVER_num][0]
                    chara_picURL[i] = SLIVER[SLIVER_num][1]
                    #print("銀，"+ chara_name[i] +"，"+ chara_picURL[i])
            else:
                if(flag <= COL_Probability):
                    self.COLOUR_position[i] = 200
                    COL += 1
                    card_rarity[i] = 'https://i.imgur.com/u94s9So.png'
                    chara_name[i]   = COLOUR[COLOUR_num][0]
                    chara_picURL[i] = COLOUR[COLOUR_num][1]
                    #print("彩，"+ chara_name[i] +"，"+ chara_picURL[i])
                else:
                    GOL += 1
                    card_rarity[i] = 'https://i.imgur.com/pHfHyhV.png'
                    chara_name[i]   = self.GOLDEN[GOLDEN_num][0]
                    chara_picURL[i] = self.GOLDEN[GOLDEN_num][1]
                    #print("金，"+ chara_name[i] +"，"+ chara_picURL[i])
        if (len(self.COLOUR_COPY) != len(self.COLOUR) or len(self.SLIVER_COPY) != len(self.SLIVER)):
            self.COLOUR = self.COLOUR_COPY
            self.SLIVER = self.SLIVER_COPY
        return Capsule_Gotcha(
            card_rarity[0],
            card_rarity[1],
            card_rarity[2],
            card_rarity[3],
            card_rarity[4],
            card_rarity[5],
            card_rarity[6],
            card_rarity[7],
            card_rarity[8],
            card_rarity[9],
            str(self.COLOUR_position[0]),
            str(self.COLOUR_position[1]),
            str(self.COLOUR_position[2]),
            str(self.COLOUR_position[3]),
            str(self.COLOUR_position[4]),
            str(self.COLOUR_position[5]),
            str(self.COLOUR_position[6]),
            str(self.COLOUR_position[7]),
            str(self.COLOUR_position[8]),
            str(self.COLOUR_position[9]),
            chara_name[0],
            chara_name[1],
            chara_name[2],
            chara_name[3],
            chara_name[4],
            chara_name[5],
            chara_name[6],
            chara_name[7],
            chara_name[8],
            chara_name[9],
            chara_picURL[0],
            chara_picURL[1],
            chara_picURL[2],
            chara_picURL[3],
            chara_picURL[4],
            chara_picURL[5],
            chara_picURL[6],
            chara_picURL[7],
            chara_picURL[8],
            chara_picURL[9],
            COL,
            GOL,
            SLI,
            float(COL_Probability),
            NAME,
            self.event
        )

    def Capsule_end(self,input_message):
        COLOUR_copy = self.COLOUR.copy()
        SLIVER_copy = self.SLIVER.copy()
        if input_message in ['#抽卡','#抽']:
            COL_Probability = 25
            return self.Ordinary_Draw(COL_Probability,self.COLOUR,self.SLIVER,"白金轉蛋")
    #公主祭
        elif '公主' in input_message:
            COLOUR_copy.update(self.PRINCESS_FES)
            if '自訂' in input_message:
                #加入try except防止使用者輸入自訂卻沒輸入數字的錯誤
                try:
                    input_message =''.join([x for x in input_message if x.isdigit()])
                    COL_Probability = float(input_message)*10
                    return self.Ordinary_Draw(COL_Probability,COLOUR_copy,self.SLIVER,"自訂公主祭")
                except:
                    COL_Probability = 50
            elif any(judger in input_message for judger in('2倍','加倍','雙倍')):
                COL_Probability = 100
                return self.Ordinary_Draw(COL_Probability,COLOUR_copy,self.SLIVER,"雙倍公主Fes")
            else:
                COL_Probability = 50
            return self.Ordinary_Draw(COL_Probability,COLOUR_copy,self.SLIVER,"公主祭Fes")
    #新年池
        elif any(judger in input_message for judger in('新年','正月')):
            COLOUR_copy.update(self.NEW_YEAR3)
            SLIVER_copy.update(self.NEW_YEAR1)
            if '自訂' in input_message:
                try:
                    input_message =''.join([x for x in input_message if x.isdigit()])
                    COL_Probability = float(input_message)*10
                    return self.Ordinary_Draw(COL_Probability,COLOUR_copy,SLIVER_copy,"自訂新年池")
                except:
                    COL_Probability = 25
            elif any(judger in input_message for judger in('2倍','加倍','雙倍')):
                COL_Probability = 50
                return self.Ordinary_Draw(COL_Probability,COLOUR_copy,SLIVER_copy,"雙倍新年")
            else:
                COL_Probability = 25
            return self.Ordinary_Draw(COL_Probability,COLOUR_copy,SLIVER_copy,"新年正月")
    #情人池
        elif '情人' in input_message:
            COLOUR_copy.update(self.VALENTINE_DAYS3)
            SLIVER_copy.update(self.VALENTINE_DAYS1)
            if '自訂' in input_message:
                try:
                    input_message =''.join([x for x in input_message if x.isdigit()])
                    COL_Probability = float(input_message)*10
                    return self.Ordinary_Draw(COL_Probability,COLOUR_copy,SLIVER_copy,"自訂情人池")
                except:
                    COL_Probability = 25
            elif any(judger in input_message for judger in('2倍','加倍','雙倍')):
                COL_Probability = 50
                return self.Ordinary_Draw(COL_Probability,COLOUR_copy,SLIVER_copy,"加倍情人節")
            else:
                COL_Probability = 25
            return self.Ordinary_Draw(COL_Probability,COLOUR_copy,SLIVER_copy,"情人節")
    #泳裝池 
        elif any(judger in input_message for judger in('夏日','泳裝')):
            COLOUR_copy.update(self.SUMMER3)
            SLIVER_copy.update(self.SUMMER1)
            if '自訂' in input_message:
                try:
                    input_message =''.join([x for x in input_message if x.isdigit()])
                    COL_Probability = float(input_message)*10
                    return self.Ordinary_Draw(COL_Probability,COLOUR_copy,SLIVER_copy,"自訂泳裝池")
                except:
                    COL_Probability = 25 
            elif any(judger in input_message for judger in('2倍','加倍','雙倍')):
                COL_Probability = 50
                return self.Ordinary_Draw(COL_Probability,COLOUR_copy,SLIVER_copy,"加倍泳裝妹紙")
            else:
                COL_Probability = 25
            return self.Ordinary_Draw(COL_Probability,COLOUR_copy,SLIVER_copy,"夏日泳裝")
    #萬聖池
        elif '萬聖' in input_message:
            COLOUR_copy.update(self.HALLOWEEN3)
            SLIVER_copy.update(self.HALLOWEEN1)
            if '自訂' in input_message:
                try:
                    input_message =''.join([x for x in input_message if x.isdigit()])
                    COL_Probability = float(input_message)*10
                    return self.Ordinary_Draw(COL_Probability,COLOUR_copy,SLIVER_copy,"自訂萬聖池")
                except:
                    COL_Probability = 25
            elif any(judger in input_message for judger in('2倍','加倍','雙倍')):
                COL_Probability = 50
                return self.Ordinary_Draw(COL_Probability,COLOUR_copy,SLIVER_copy,"加倍萬聖")
            else:
                COL_Probability = 25
            return self.Ordinary_Draw(COL_Probability,COLOUR_copy,SLIVER_copy,"萬聖節")
    #聖誕池
        elif '聖誕' in input_message:
            COLOUR_copy.update(self.CHRISTMAS3)
            SLIVER_copy.update(self.CHRISTMAS1)
            if '自訂' in input_message:
                try:
                    input_message =''.join([x for x in input_message if x.isdigit()])
                    COL_Probability = float(input_message)*10
                    return self.Ordinary_Draw(COL_Probability,COLOUR_copy,SLIVER_copy,"自訂聖誕池")
                except:
                    COL_Probability = 25
            elif any(judger in input_message for judger in('2倍','加倍','雙倍')):
                COL_Probability = 50
                return self.Ordinary_Draw(COL_Probability,COLOUR_copy,SLIVER_copy,"加倍聖誕")
            else:
                COL_Probability = 25
            return self.Ordinary_Draw(COL_Probability,COLOUR_copy,SLIVER_copy,"聖誕節")
    #奇幻池 
        elif any(judger in input_message for judger in('奇幻','wonder','不可思議','夢')):
            COLOUR_copy.update(self.WONDERLAND3)
            SLIVER_copy.update(self.WONDERLAND1)
            if '自訂' in input_message:
                try:
                    input_message =''.join([x for x in input_message if x.isdigit()])
                    COL_Probability = float(input_message)*10
                    return self.Ordinary_Draw(COL_Probability,COLOUR_copy,SLIVER_copy,"自訂奇幻池")
                except:
                    COL_Probability = 25
            elif any(judger in input_message for judger in('2倍','加倍','雙倍')):
                COL_Probability = 50
                return self.Ordinary_Draw(COL_Probability,COLOUR_copy,SLIVER_copy,"加倍夢境")
            else:
                COL_Probability = 25
            return self.Ordinary_Draw(COL_Probability,COLOUR_copy,SLIVER_copy,"不可思議之國")
    #偶大池 
        elif any(judger in input_message for judger in('偶','灰姑娘','新世代','CGSS','Cgss','cgss')):
            COLOUR_copy.update(self.CINDERELLA3)
            SLIVER_copy.update(self.CINDERELLA1)
            if '自訂' in input_message:
                try:
                    input_message =''.join([x for x in input_message if x.isdigit()])
                    COL_Probability = float(input_message)*10
                    return self.Ordinary_Draw(COL_Probability,COLOUR_copy,SLIVER_copy,"自訂偶大池")
                except:
                    COL_Probability = 25
            elif any(judger in input_message for judger in('2倍','加倍','雙倍')):
                COL_Probability = 50
                return self.Ordinary_Draw(COL_Probability,COLOUR_copy,SLIVER_copy,"加倍灰姑娘")
            else:
                COL_Probability = 25
            return self.Ordinary_Draw(COL_Probability,COLOUR_copy,SLIVER_copy,"偶像大師")
    #天使池
        elif '天使' in input_message :
            COLOUR_copy.update(self.ANGEL)
            if '自訂' in input_message:
                try:
                    input_message =''.join([x for x in input_message if x.isdigit()])
                    COL_Probability = float(input_message)*10
                    return self.Ordinary_Draw(COL_Probability,COLOUR_copy,self.SLIVER,"自訂天使池")
                except:
                    COL_Probability = 25
            elif any(judger in input_message for judger in('2倍','加倍','雙倍')):
                COL_Probability = 50
                return self.Ordinary_Draw(COL_Probability,COLOUR_copy,self.SLIVER,"加倍天使")
            else:
                COL_Probability = 25
            return self.Ordinary_Draw(COL_Probability,COLOUR_copy,self.SLIVER,"惡魔天使")
    #支那池
        elif any(judger in input_message for judger in('支那','國服','環奈')):
            COLOUR_copy.update(self.CN)
            if '自訂' in input_message:
                try:
                    input_message =''.join([x for x in input_message if x.isdigit()])
                    COL_Probability = float(input_message)*10
                    return self.Ordinary_Draw(COL_Probability,COLOUR_copy,self.SLIVER,"自訂國服池")
                except:
                    COL_Probability = 25
            elif any(judger in input_message for judger in('2倍','加倍','雙倍')):
                COL_Probability = 50
                return self.Ordinary_Draw(COL_Probability,COLOUR_copy,self.SLIVER,"加倍環奈")
            else:
                COL_Probability = 25
            return self.Ordinary_Draw(COL_Probability,COLOUR_copy,self.SLIVER,"環奈限定池")
#抽全角色池，記得要更新 
        elif any(judger in input_message for judger in('大混','全','大雜燴')):
            self.COLOUR.update(self.PRINCESS_FES)
            self.COLOUR.update(self.NEW_YEAR3)
            self.SLIVER.update(self.NEW_YEAR1)
            self.COLOUR.update(self.VALENTINE_DAYS3)
            self.SLIVER.update(self.VALENTINE_DAYS1)
            self.COLOUR.update(self.SUMMER3)
            self.SLIVER.update(self.SUMMER1)
            self.COLOUR.update(self.HALLOWEEN3)
            self.SLIVER.update(self.HALLOWEEN1)
            self.COLOUR.update(self.CHRISTMAS3)
            self.SLIVER.update(self.CHRISTMAS1)
            self.COLOUR.update(self.WONDERLAND3)
            self.SLIVER.update(self.WONDERLAND1)
            self.COLOUR.update(self.CINDERELLA3)
            self.SLIVER.update(self.CINDERELLA1)
            self.COLOUR.update(self.ANGEL)
            if '自訂' in input_message:
                try:
                    input_message =''.join([x for x in input_message if x.isdigit()])
                    COL_Probability = float(input_message)*10
                    return self.Ordinary_Draw(COL_Probability,self.COLOUR,self.SLIVER,"自訂大混池")
                except:
                    COL_Probability = 25
            elif any(judger in input_message for judger in('2倍','加倍','雙倍')):
                COL_Probability = 50
                return self.Ordinary_Draw(COL_Probability,self.COLOUR,self.SLIVER,"加倍混亂...")
            else:
                COL_Probability = 25
            return self.Ordinary_Draw(COL_Probability,self.COLOUR,self.SLIVER,"大混池")

        elif any(judger in input_message for judger in('2倍','加倍','雙倍')):
            COL_Probability = 50
            return self.Ordinary_Draw(COL_Probability,self.COLOUR,self.SLIVER,"加倍轉蛋")

        elif '自訂' in input_message:
            try:
                input_message =''.join([x for x in input_message if x.isdigit()])
                COL_Probability = float(input_message)*10
            except:
                COL_Probability = 25
            return self.Ordinary_Draw(COL_Probability,self.COLOUR,self.SLIVER,"自定義池")

        else:
            COL_Probability = 25
            return self.Ordinary_Draw(COL_Probability,self.COLOUR,self.SLIVER,"白金轉蛋")
#Cap = Capsule_Cul()
#Cap.Ordinary_Draw()