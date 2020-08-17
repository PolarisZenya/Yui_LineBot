#============================================================
import random
#============================================================
from FlexMessage import *
#============================================================
#進行計算

class Capsule_Cul:
    def __init__(self):
        #global變數，常駐池
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
            1  : ["杏奈",       'https://i.imgur.com/dMn5fZb.jpg'],
            2  : ["真步",       'https://i.imgur.com/GUTDc8E.jpg'],
            3  : ["璃乃",       'https://i.imgur.com/tmoLmFU.jpg'],
            4  : ["初音",       'https://i.imgur.com/mEaeUv2.jpg'],
            5  : ["霞",         'https://i.imgur.com/oJP4AVi.jpg'],
            6  : ["伊緒",       'https://i.imgur.com/ijleQFV.jpg'],
            7  : ["咲戀",       'https://i.imgur.com/Li6PEV3.jpg'],
            8  : ["小望",       'https://i.imgur.com/MYVEygy.jpg'],
            9  : ["妮諾",       'https://i.imgur.com/1JTz0rk.jpg'],
            10 : ["秋乃",       'https://i.imgur.com/uzkF32k.jpg'],
            11 : ["鏡華",       'https://i.imgur.com/1ww8OeH.jpg'],
            12 : ["智",         'https://i.imgur.com/qvJZ5It.jpg'],
            13 : ["真琴",       'https://i.imgur.com/WZE20Tz.jpg'],
            14 : ["伊莉亞",     'https://i.imgur.com/2MMZaDw.jpg'],
            15 : ["嘉夜",       'https://i.imgur.com/HlQ2Hlu.jpg'],
            16 : ["純",         'https://i.imgur.com/sJOjm6G.jpg'],
            17 : ["靜流",       'https://i.imgur.com/G3eOqQn.jpg'],
            18 : ["莫妮卡",     'https://i.imgur.com/F2G3bUR.jpg'],
            19 : ["流夏",       'https://i.imgur.com/QJGjmzo.jpg'],
            20 : ["吉塔",       'https://i.imgur.com/JYmWQdw.jpg'],
            21 : ["亞里莎",     'https://i.imgur.com/kwPUVoT.jpg'],
            22 : ["安",         'https://i.imgur.com/BaRggvy.jpg'],
            23 : ["古蕾雅",     'https://i.imgur.com/sm5CShx.jpg'],
            24 : ["江戶空花",   'https://i.imgur.com/tzPfVIq.jpg'],
            25 : ["江戶妮諾",   'https://i.imgur.com/3TBrKaS.jpg'],
            26 : ["學院碧",     'https://i.imgur.com/73oSybt.jpg'],
            27 : ["克蘿依",     'https://i.imgur.com/wbo5P0W.jpg'],
            28 : ["優妮",       'https://i.imgur.com/7xFJhQX.jpg'],
            29 : ["萬聖美美",   'https://i.imgur.com/c5B2ahO.jpg'],
            30 : ["露娜",       'https://i.imgur.com/kLRm0BK.jpg'],
            31 : ["魔法少女霞", 'https://i.imgur.com/kuC8w00.jpg'],
            32 : ["遊俠鈴",     'https://i.imgur.com/SrcLrD2.jpg'],
        }
        #彩卡光環位置存取值
        # top / offsetStart
        self.COLOUR_position = [300,300,300,300,300,300,300,300,300,300]

    def Ordinary_Draw(self,COL_Probability):
        #存亂數取出值
        card_rarity = [0]*10
        chara_name = [0]*10
        chara_picURL = [0]*10
        SLI = 0
        GOL = 0
        COL = 0
        for i in range (0,10):
            #從某稀有度抽一，flag抽稀有度 (彩2.5%，金18%，銀79.5%)
            SLIVER_num = random.randint(1,len(self.SLIVER))
            GOLDEN_num = random.randint(1,len(self.GOLDEN))
            COLOUR_num = random.randint(1,len(self.COLOUR))
            flag = random.randint(1,1000)
            #第十抽保底金起跳
            if(i!=9):
                if(flag <= COL_Probability):
                    pos_counter = 50*i
                    if(pos_counter>=250):
                        pos_counter = 50*(i-5)
                    self.COLOUR_position[i] = pos_counter
                    COL += 1
                    card_rarity[i]  = 'https://i.imgur.com/u94s9So.png'
                    chara_name[i]   = self.COLOUR[COLOUR_num][0]
                    chara_picURL[i] = self.COLOUR[COLOUR_num][1]
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
                    chara_name[i]   = self.SLIVER[SLIVER_num][0]
                    chara_picURL[i] = self.SLIVER[SLIVER_num][1]
                    #print("銀，"+ chara_name[i] +"，"+ chara_picURL[i])
            else:
                if(flag <= COL_Probability):
                    self.COLOUR_position[i] = 200
                    COL += 1
                    card_rarity[i] = 'https://i.imgur.com/u94s9So.png'
                    chara_name[i]   = self.COLOUR[COLOUR_num][0]
                    chara_picURL[i] = self.COLOUR[COLOUR_num][1]
                    #print("彩，"+ chara_name[i] +"，"+ chara_picURL[i])
                else:
                    GOL += 1
                    card_rarity[i] = 'https://i.imgur.com/pHfHyhV.png'
                    chara_name[i]   = self.GOLDEN[GOLDEN_num][0]
                    chara_picURL[i] = self.GOLDEN[GOLDEN_num][1]
                    #print("金，"+ chara_name[i] +"，"+ chara_picURL[i])
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
            float(COL_Probability)
        )

    def Capsule_end(self,input_message):
        if input_message in ['#抽卡','#抽']:
            return self.Ordinary_Draw(COL_Probability = 25)
        elif '自訂' in input_message:
            input_message =''.join([x for x in input_message if x.isdigit()])
            return self.Ordinary_Draw(COL_Probability = int(input_message)*10)
        elif '十抽' in input_message or '10抽' in input_message:
            return self.Ordinary_Draw(COL_Probability = 25)
        elif '2倍' in input_message or '加倍' in input_message or '雙倍' in input_message:
            return self.Ordinary_Draw(COL_Probability = 50)
        elif '4倍' in input_message:
            return self.Ordinary_Draw(COL_Probability = 100)

#Cap = Capsule_Cul()
#Cap.Ordinary_Draw()