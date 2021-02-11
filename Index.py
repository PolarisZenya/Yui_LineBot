#============================================================
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *
import random
import time
#============================================================
from FlexMessage import *  
from Animation import *  
from Res_Hentai import *  
from Capsule import * 
from Quick_Reply import * 
from Insert_Sheet_Data import *
import Globals    
#============================================================ 
class Index_Judgment:
    def __init__(self):
        self.GS = Google_Sheet_DataBase()
        self.localtime = time.localtime(time.time())
        self.localhour = self.localtime.tm_hour
        if(self.localhour+8>24):        # heroku server jetlag 
            self.localhour=self.localhour-16
        else:
            self.localhour=self.localhour+8
        self.access=1
    def Judgment (self,line_bot_api,input_message,event):
        i = random.randint(0,10800)

        if input_message in ['#log','#指令']:
            message = Log(event)
            line_bot_api.reply_message(event.reply_token,message)
            return

        elif input_message in ['#求圖','#隨機','#random','#ランダム']:
            value_i = [
                ['惡魔偽王國軍'],['茜里'],['布丁'],['忍'],['伊莉亞'],['依里'],
                ['美食殿'],['凱留'],['佩可'],['可可蘿'],['祐樹'],['謝菲'],['孝心逐漸變質'],
                ['慈樂之音'],['紡希'],['小望'],['千歌'],
                ['優妮們'],['優妮'],['克蘿依'],['切嚕'],
                ['墨丘利財團'],['秋乃'],['優花梨'],['美冬'],['珠希'],['無人島'],
                ['美里'],['碧'],['初音'],
                ['克莉絲提娜'],['矛依未'],['似似花'],['尾狗刀'],['拉比林斯達'],['愛梅斯'],
                ['哞哞自衛隊'],['真步'],['霞'],['真琴'],['香織'],
                ['小小甜心'],['鏡華'],['美美'],['禊'],['五等分的蘿莉'],
                ['暮光流星群'],['杏奈'],['流夏'],['深月'],['七七香'],['惠理子'],
                ['Re:0'],['愛蜜莉雅'],['雷姆'],['拉姆'],
                ['破曉之星'],['優衣'],['日和'],['怜'],
                ['拉比林斯'],['靜流'],['璃乃'],['姊妹'],
                ['咲戀救護院'],['咲戀'],['鈴莓'],['綾音'],['胡桃'],
                ['王宮騎士團'],['純'],['智'],['茉莉'],['團長們'],
                ['月光學院'],['伊緒'],['鈴奈'],['美咲'],
                ['栞'],['真陽'],['鈴'],['莉瑪'],
                ['純白之翼'],['莫妮卡'],['小雪'],['妮諾'],['空花'],['步未'],
                ['魔法少女'],['終戰'],['公主連結'],
                ['馬納歷亞'],['古蕾雅'],['安'],['露'],
                ['吉塔'],['亞里莎'],['露娜'],['愛梅斯'],
                ['龍族巢穴'],['帆稀'],['嘉夜'],['祈梨'],
                ['偶像大師灰姑娘女孩'],['卯月'],['凜'],['未央'],
                ['美空']
            ]
            self.access+=1
            input_message = value_i[i%len(value_i)][0]

        elif input_message in ['#問題回報','#回報問題','#回報','#聯絡作者']:
            value_i = [
                "新功能、更多的彩蛋、更大的隨機性、更多對騎士君的愛~~~\n新版本逐漸更新上來了\n到作者的巴哈小屋一探究竟吧：\nhttps://m.gamer.com.tw/home/creationDetail.php?sn=4873921",
                "騎士君有找到彩蛋嗎?\n聽說作者塞了一堆給人家呢\n巴哈小屋：https://m.gamer.com.tw/home/creationDetail.php?sn=4873921",     
                "如果有什麼對優衣的建議可以到作者君的巴哈留言給他呦\n他的巴哈小屋：https://m.gamer.com.tw/home/creationDetail.php?sn=4873921",
                "吶吶 可以告訴優衣騎士君要找作者做什麼咩?\n他的巴哈小屋：https://m.gamer.com.tw/home/creationDetail.php?sn=4873921",
                "無能作者大大的巴哈呦~~\n作者的巴哈小屋：https://m.gamer.com.tw/home/creationDetail.php?sn=4873921",
                "咦咦!!人家出現問題了嗎？\n\n趕快去他的巴哈小屋告訴她：https://m.gamer.com.tw/home/creationDetail.php?sn=4873921",
                "騎士君，如果人家出現問題可以到作者大大的來幹爆作者呦\n\nhttps://m.gamer.com.tw/home/creationDetail.php?sn=4873921 ",
                "為什麼只有巴哈呢？\n是作者君沒有在玩dc呦~\nhttps://m.gamer.com.tw/home/creationDetail.php?sn=4873921 ",
                "新版本的優衣更新記都丟在那邊了，去找吧！\nhttps://home.gamer.com.tw/creationDetail.php?sn=4914939",
                "有什麼話想跟作者大大說嗎？可以用 #建議 xxxx 傳訊息給他哦\n順便附上人家的日誌：https://home.gamer.com.tw/creationDetail.php?sn=4914939",
                "騎士君那麼想看人家的日誌嗎？\nhttps://home.gamer.com.tw/creationDetail.php?sn=4914939",
                "更新日誌：https://home.gamer.com.tw/creationDetail.php?sn=4914939\n巴哈小屋：https://m.gamer.com.tw/home/creationDetail.php?sn=4873921",
            ]
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text = value_i[i% len(value_i)]))
            return

        elif input_message in ['#建議','#提議','#許願'] and event.source.type != 'group': 
            value_i = [
                "不對呦騎士君，後面要打出你想要對作者大大說的話",
                "踴躍發言哦，給的建議要寫在後面哦",     
                "要私訊作者的話加在後面哦，作者會回覆你的私訊吶"
            ]
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text = value_i[i% len(value_i)]))
            return

        elif input_message[:3] in ['#建議','#提議','#許願'] and event.source.type != 'group': 
            input_message = input_message.replace("#提議",'')
            input_message = input_message.replace("#建議",'')
            input_message = input_message.replace("#許願",'')
            value_i = [
                "恩，騎士君的"+input_message+"\n優衣收到了喔!",
                input_message+"嗎？\n已經傳送給作者了哦",     
                "嗯，確實收到騎士君的建議了"
            ]
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text = value_i[i% len(value_i)]))
            self.GS.Sheet_Advice(event.source.user_id,input_message)
            return

        elif input_message in ['#刪除建議','#刪除提議','#刪除許願']: 
            self.GS.Sheet_Advice_Del()
            line_bot_api.reply_message(event.reply_token,TextMess("已閱資料皆已刪除!!\nhttps://docs.google.com/spreadsheets/d/1PkO_53TKlHprD4HQXX0rPFneJ2i71TvRIPY0LhY0f-Y/edit#gid=0"))
            return

        elif input_message in ['#權限']:
            if(event.source.type=='user'):
                if(event.source.user_id in Globals.Yui_denied_group):
                    cent = Globals.Searcher(event.source.user_id)
            elif(event.source.type=='group'):
                if(event.source.group_id in Globals.Yui_denied_group):
                    cent = Globals.Searcher(event.source.group_id)
            try:
                reply=Access_Denied_Level_Flex(Globals.Yui_denied_access[cent])
            except:
                if(event.source.type=='user'):
                    reply=Access_Denied_Level_Flex(0)
                elif(event.source.type=='group'):
                    reply=Access_Denied_Level_Flex(1)
            line_bot_api.reply_message(event.reply_token,reply) 
            return

        elif input_message[:3] in ['#權限'] and len(input_message) <= 5:
            num =''.join([x for x in input_message if x.isdigit()])
            if(event.source.type=='user'):
                if eval(num)<=3 and eval(num)>0:
                    if(event.source.user_id not in Globals.Yui_denied_group):
                        value_i = [
                            "咦 人家做錯了什麼嗎?",
                            "我，太多嘴了嗎?",     
                            "如果這樣能幫到騎士君的話...",
                            "咦 要保持距離嗎...",
                            "是因為疫情要保持距離嗎...",
                            "*優衣的發言已被遮蔽*"
                        ]
                        line_bot_api.reply_message(event.reply_token,TextSendMessage(text = value_i[i% len(value_i)]))
                        self.GS.Denied_Insert(event.source.user_id,event.source.type,eval(num),line_bot_api.get_profile(event.source.user_id).display_name)
                        Globals.Yui_denied_group.append(event.source.user_id)
                        Globals.Yui_denied_access.append(num)
                        return
                    elif(event.source.user_id in Globals.Yui_denied_group):
                        value_i = [
                            "嗚嗚嗚...QQ",
                            "*嗚嘴*",
                            "*優衣的發言仍然被遮蔽*"
                        ]
                        line_bot_api.reply_message(event.reply_token,TextSendMessage(text = value_i[i% len(value_i)]))
                        Globals.Yui_denied_access[Globals.Searcher(event.source.user_id)]=eval(num)
                        self.GS.Denied_Change(event.source.user_id,eval(num))
                        return
                elif eval(num)==0 and event.source.user_id in Globals.Yui_denied_group:
                    value_i = [
                            "謝謝你 騎士君",
                            "歡迎回來~",
                            "就算是這樣 我也相信著騎士君"
                    ]
                    line_bot_api.reply_message(event.reply_token,TextSendMessage(text = value_i[i% len(value_i)]))
                    i = Globals.Searcher(event.source.user_id)
                    del Globals.Yui_denied_group[i]
                    del Globals.Yui_denied_access[i]
                    self.GS.Denied_Change(event.source.user_id,eval(num))
                    return
            if(event.source.type=='group'):
                if eval(num)<=3 and eval(num)>0:
                    print("Line reply")
                    if(event.source.group_id not in Globals.Yui_denied_group):
                        value_i = [
                            "咦 人家做錯了什麼嗎?",
                            "公開場合下被騎士君拒絕...",     
                            "如果這樣能幫到騎士君們的話...",
                            "我，太多嘴了嗎?",
                            "騎士君們都這樣集體欺凌人家的嗎?",
                            "*優衣的發言已被遮蔽*"
                        ]
                        line_bot_api.reply_message(event.reply_token,TextSendMessage(text = value_i[i% len(value_i)]))
                        self.GS.Denied_Insert(event.source.group_id,event.source.type,eval(num),line_bot_api.get_profile(event.source.user_id).display_name)
                        Globals.Yui_denied_group.append(event.source.group_id)
                        Globals.Yui_denied_access.append(num)
                        return
                    elif(event.source.group_id in Globals.Yui_denied_group):
                        value_i = [
                            "嗚嗚嗚...QQ",
                            "*嗚嘴*",
                            "*優衣的發言仍然被遮蔽*"
                        ]
                        line_bot_api.reply_message(event.reply_token,TextSendMessage(text = value_i[i% len(value_i)]))
                        Globals.Yui_denied_access[Globals.Searcher(event.source.group_id)]=eval(num)
                        self.GS.Denied_Change(event.source.group_id,eval(num))
                        return
                elif eval(num)==0 and event.source.group_id in Globals.Yui_denied_group:
                    value_i = [
                            "謝謝你 騎士君",
                            "好久沒回到騎士君們的小屋了~",
                            "啊...謝謝你! 那個...謝禮在..."
                    ]
                    line_bot_api.reply_message(event.reply_token,TextSendMessage(text = value_i[i% len(value_i)]))
                    i = Globals.Searcher(event.source.group_id)
                    del Globals.Yui_denied_group[i]
                    del Globals.Yui_denied_access[i]
                    self.GS.Denied_Change(event.source.group_id,eval(num))
                    return
                
        elif input_message[:2] == '#抽' and len(input_message)<=16:
            value_i = [
                "底下的角色頭像可以點擊呦~~",
                "騎士君你已經有我了還想要更多的後宮嗎？",     
                "與50幾位可愛公主們的冒險物語？\n\n有人家就足夠了呦~",
                "接下來是可以預期的結果呢",
                "咦?欸!\n抽這麼多不會太貪心了嗎?",
                "欸秀，看人家施展爆死魔法呦~",
                "各個卡池都可以抽呦(公主祭、新年、泳裝、情人節、萬聖節、聖誕節...)\n在後面輸入 自訂+機率 可設定出彩卡的機率呦",
            ]
            line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)]),Capsule_Cul(event).Capsule_end(input_message)])
            return

        elif input_message[:3] == '#漫畫' or input_message == '#漫畫 隨機': 
            try:
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = "譯者：阮敬珩"),ImageMessageURL(Manga_Reply(input_message,i))])
            except:
                line_bot_api.reply_message(event.reply_token,TextSendMessage(text = "騎士君你輸入的話數不是尚未更新就是輸入錯誤哦！"))
            return

        elif input_message[:3] == '#動畫': 
            try:
                line_bot_api.reply_message(event.reply_token,Anime_View(input_message))
            except:
                line_bot_api.reply_message(event.reply_token,TextSendMessage(text = "輸入錯誤哦，目前無此動畫"))
            return

        elif input_message[0] == '#' and len(input_message) <=5 :
            value_i = [
                "指令錯誤呦，要不要再檢查一下呢",    #文字+圖片(陣列值為2)
                "騎士君~優衣不認識這個指令",     
                "目前沒有這條指令呦，可以跟作者大大聯絡，看能不能新增這項指令~\n(但依他的尿性八成又懶得去改了...)",
                "騎士君~人家的指令功能少之又少\n但有什麼辦法呢，作者不知道又跑去哪偷懶了啦"
            ]
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text = value_i[i% len(value_i)]))
            return
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------        
        try:
            if (event.source.user_id in Globals.Yui_denied_group) and event.source.type == 'user':
                if int(Globals.Yui_denied_access[Globals.Searcher(event.source.user_id)]) >= 3 :
                    self.access-=1
                elif int(Globals.Yui_denied_access[Globals.Searcher(event.source.user_id)]) == 2 :
                    self.access-=2
            elif (event.source.group_id in Globals.Yui_denied_group) and event.source.type == 'group':
                    if int(Globals.Yui_denied_access[Globals.Searcher(event.source.group_id)]) >= 3 :
                        self.access-=1
                    elif int(Globals.Yui_denied_access[Globals.Searcher(event.source.group_id)]) == 2 :
                        self.access-=2
        except:
            try:
                if (event.source.user_id in Globals.Yui_denied_group) and event.source.type == 'user':
                    if int(Globals.Yui_denied_access[Globals.Searcher(event.source.user_id)]) >= 3 :
                        self.access-=1
                    elif int(Globals.Yui_denied_access[Globals.Searcher(event.source.user_id)]) == 2 :
                        self.access-=2
            except:
                if (event.source.group_id in Globals.Yui_denied_group) and event.source.type == 'group':
                    if int(Globals.Yui_denied_access[Globals.Searcher(event.source.group_id)]) >= 3 :
                        self.access-=1
                    elif int(Globals.Yui_denied_access[Globals.Searcher(event.source.group_id)]) == 2 :
                        self.access-=2

        if(self.access>=1):

            if all(judger in input_message for judger in('世界','幸福','女孩')) and len(input_message)<13:
                value_i = [
                    ["如此溫暖的幸福，唯有騎士君呢~~","https://i.imgur.com/vbyBSHq.jpg"],   #文字+圖片(陣列值為2)
                    "只要學姊們的消失，優衣就一定是世界上最幸福的女孩",     
                    "珂朵莉?不~不~\n\n死人可沒有感受呢~~",
                    "こんなにも、たくさんの幸せをあの人に分けてもらった\n\nだから、きっと\n今の、私は\n誰が何と言おうと\n\n世界一、幸せな女の子だ",
                    "當然是優衣了啊，不然還有誰呢? (笑www舉刀~~",
                    "恩恩，我知道是人家呦",
                    "如果沒有學姊們的話...",
                    "嘻嘻，有騎士君的陪伴\n這時的我 才是世界上最幸福的女孩",
                    "這份幸福，陪伴著我，成為騎士君的力量",
                ]
                if(len(value_i[i% len(value_i)])==2):  #判斷 文字+圖片 陣列值為2
                    line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
                else:
                    line_bot_api.reply_message(event.reply_token,TextSendMessage(text = value_i[i% len(value_i)]))

            elif any(judger in input_message for judger in('發車','wnacg','nhentai','18comic','老司機','色情','上車','色圖','車圖','本本','做愛')):
                value_i = [
                    ImageMessageURL("https://i.imgur.com/ybuvdJN.jpg"),
                    ImageMessageURL("https://i.imgur.com/0lZtQR7.jpg"),
                    TextSendMessage(text="發車了發車了(叮叮叮!!")
                ]
                line_bot_api.reply_message(event.reply_token,value_i[i% len(value_i)])

            elif any(judger in input_message for judger in('NTR','ntr')):
                value_i = [
                    "有誰提到了NTR嗎？",
                    "咦？NTR？\n騎士君~♡優衣再給你一次機會說清楚呦",
                    "騎士君為什麼又要說出NTR這個詞...",
                    "騎士君你說到了NTR嗎?\n不過在Line的世界...\n一個群組只能存在一個機器人\n學姊x騎士君也不會存在\n也代表著在這裡...\n騎士君身邊的機器人只能有優衣呦~~♡"
                ]
                line_bot_api.reply_message(event.reply_token,TextSendMessage(text=value_i[i% len(value_i)]))

            elif input_message in ["優衣我愛你","我愛你優衣","我愛你","我喜歡你","我愛優衣"] and event.source.type == 'group':
                value_i = [
                    "騎...騎士君，這裡人有點多",
                    "咦咦...在群組人這麼多的地方嗎///",
                    "哇啊啊~\n騎士君這麼突然的在群組告白會讓其他騎士君們忌妒的哦",
                ]
                line_bot_api.reply_message(event.reply_token,TextSendMessage(text=value_i[i% len(value_i)]))

            elif input_message in ['阿嘿顏','阿黑顏','アヘ顔','あへがお','O-Face','啊嘿顏']:
                value_i = [
                    "https://i.imgur.com/BqQX7KL.jpg",   
                    "https://i.imgur.com/iFe5eiN.jpg",  
                    "https://i.imgur.com/XR2iUcD.jpg",
                    "https://i.imgur.com/9uOIoXH.jpg",
                    "https://i.imgur.com/4bs4XQN.jpg"
                ]
                line_bot_api.reply_message(event.reply_token,ImageMessageURL(value_i[i% len(value_i)]))

            elif any(judger in input_message for judger in('射爆','爆射')) or input_message in ['射','射了','社保']:
                value_i = [
                    "https://i.imgur.com/VEmKBTm.jpg",   
                    "https://i.imgur.com/nhWCFTP.jpg",  
                    "https://i.imgur.com/lWzPVq4.jpg",
                    "https://i.imgur.com/m043hLL.jpg",
                    "https://i.imgur.com/fG7fJ2e.jpg",
                    "https://i.imgur.com/Ny71JoP.jpg",
                    "https://i.imgur.com/bqNJce8.jpg",
                    "https://i.imgur.com/NEVZ5eG.jpg",
                ]
                line_bot_api.reply_message(event.reply_token,ImageMessageURL(value_i[i% len(value_i)]))

            elif input_message in ['怕爆','怕']:
                value_i = [
                    "https://i.imgur.com/Qww9qPE.jpg",   
                    "https://i.imgur.com/vhbLxU4.jpg",  
                    "https://i.imgur.com/I9u5jID.jpg",
                    "https://i.imgur.com/H72pl7m.png",
                    "https://i.imgur.com/dplH8Es.jpg"
                ]
                line_bot_api.reply_message(event.reply_token,ImageMessageURL(value_i[i% len(value_i)]))

            elif input_message in ['A','a']:
                value_i = [
                    "https://i.imgur.com/PFuuwzd.jpg",   
                    "https://i.imgur.com/waewwce.jpg",
                    "https://i.imgur.com/O94ET1r.jpg",
                ]
                line_bot_api.reply_message(event.reply_token,ImageMessageURL(value_i[i% len(value_i)]))

            elif input_message in ['窩不知道','我不知道','不知道','母雞到']:
                value_i = [
                    "https://i.imgur.com/eIMpcI0.jpg",   
                    "https://i.imgur.com/3L7Kal8.jpg",  
                    "https://i.imgur.com/HF1BaSm.jpg",
                    "https://i.imgur.com/SuYDfrG.jpg"
                ]
                line_bot_api.reply_message(event.reply_token,ImageMessageURL(value_i[i% len(value_i)]))

            elif '我婆' in input_message:
                value_i = [
                    "https://i.imgur.com/OnDeK8f.jpg",   
                    "https://i.imgur.com/rWcQJwD.jpg",  
                    "https://i.imgur.com/8ne7OeN.jpg",
                    "https://i.imgur.com/gVl6v1z.jpg",
                    "https://i.imgur.com/Ebvx2LH.jpg"
                ]
                line_bot_api.reply_message(event.reply_token,ImageMessageURL(value_i[i% len(value_i)]))

            elif input_message in ['佬','大佬'] :
                value_i = [
                    "https://i.imgur.com/oH7jUmZ.jpg",   
                    "https://i.imgur.com/Mn7QLMR.jpg",  
                    "https://i.imgur.com/K3lkjyv.jpg",
                    "https://i.imgur.com/8niUWf6.jpg"
                ]
                line_bot_api.reply_message(event.reply_token,ImageMessageURL(value_i[i% len(value_i)]))

            elif input_message in ['奶子','是什麼蒙蔽了我的雙眼','奶','巨乳','大奶','大奶子','おっぱい'] :
                value_i = [
                    "https://i.imgur.com/lLanAHP.jpg",   
                    "https://i.imgur.com/BXRoBtm.jpg",  
                    "https://i.imgur.com/5oM7q7O.jpg"
                ]
                line_bot_api.reply_message(event.reply_token,ImageMessageURL(value_i[i% len(value_i)]))

            elif input_message in ['舔','舔爆'] :
                value_i = [
                    "https://i.imgur.com/SOVbAW0.jpg",   
                    "https://i.imgur.com/t75A3vZ.jpg",  
                    "https://i.imgur.com/v3DpiAK.jpg",
                    "https://i.imgur.com/MFztjKa.jpg",
                    "https://i.imgur.com/Tftmj8R.jpg",
                    "https://i.imgur.com/ez5oOLL.jpg",
                    "https://i.imgur.com/Rrwb9E9.jpg",
                ]
                line_bot_api.reply_message(event.reply_token,ImageMessageURL(value_i[i% len(value_i)]))

            elif all(judger in input_message for judger in('道歉','露')):
                value_i = [
                    "https://i.imgur.com/HZLp9n5.jpg",   
                    "https://i.imgur.com/mJ5u9FR.jpg",  
                    "https://i.imgur.com/TwiqUp5.jpg",
                    "https://i.imgur.com/TjkbiNZ.jpg"
                ]
                line_bot_api.reply_message(event.reply_token,ImageMessageURL(value_i[i% len(value_i)]))

            elif all(judger in input_message for judger in('本','說','但','算')) and len(input_message)<16:
                value_i = [
                    ["繪師: 寂月-pixiv",   "https://i.imgur.com/ZmCBYs0.jpg"],   
                    ["https://i.imgur.com/6YVj7ky.jpg"],  
                    ["https://i.imgur.com/mZ7Cf8B.jpg"],
                    ["https://i.imgur.com/KdiazlQ.jpg"]
                ]
                if(len(value_i[i% len(value_i)])==2): 
                    line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
                else:
                    line_bot_api.reply_message(event.reply_token,ImageMessageURL(value_i[i% len(value_i)][0]))

            elif  input_message in ['鴨沒肉','やめろ','ヤメロ'] :
                value_i = [
                    "https://i.imgur.com/uyLpJfG.jpg",   
                    "https://i.imgur.com/64zdyMp.jpg",  
                    "https://i.imgur.com/WOG91NS.jpg",
                    "https://i.imgur.com/iAO2wRh.png"
                ]
                line_bot_api.reply_message(event.reply_token,ImageMessageURL(value_i[i% len(value_i)]))

            elif  input_message in ['咕嚕靈波','咕嚕凌波']:
                value_i = [
                    "https://i.imgur.com/IXGLGXU.jpg",   
                    "https://i.imgur.com/rRAEQWI.jpg",  
                    "https://i.imgur.com/XsUTL7o.jpg",
                    "https://i.imgur.com/jlVp4ph.jpg",
                    "https://i.imgur.com/y8pHoyY.jpg",   
                    "https://i.imgur.com/LioJCLn.jpg",  
                    "https://i.imgur.com/l4GNzDx.jpg",
                    "https://i.imgur.com/nB9t44h.jpg"
                ]
                line_bot_api.reply_message(event.reply_token,ImageMessageURL(value_i[i% len(value_i)]))

            elif  input_message in ['接頭','接頭霸王']:
                value_i = [
                    ['https://i.imgur.com/qHWC2Tu.jpg','https://i.imgur.com/BlYRywQ.jpg'],
                    ['https://i.imgur.com/0bVJvvv.jpg'],
                    ['https://i.imgur.com/kTih1Ht.jpg'],
                ]
                if(len(value_i[i% len(value_i)])==2): 
                    line_bot_api.reply_message(event.reply_token,[ImageMessageURL(value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
                else:
                    line_bot_api.reply_message(event.reply_token,ImageMessageURL(value_i[i% len(value_i)][0]))

            elif  input_message in ['課金','魔法小卡'] :
                value_i = [
                    "https://i.imgur.com/EdayZQQ.jpg",   
                    "https://i.imgur.com/6EJ9fI8.jpg",  
                    "https://i.imgur.com/g7KgiFY.jpg",
                    "https://i.imgur.com/ZMNl8wb.jpg",
                    "https://i.imgur.com/KGNxybo.jpg",
                    "https://i.imgur.com/sipuNE8.jpg",
                    "https://i.imgur.com/Yi6VARl.jpg",
                    ["繪師: だんなんだ-pixiv",   "https://i.imgur.com/BOMKsKV.jpg"],
                    ["真步開心",                "https://i.imgur.com/imuPBNv.jpg"]
                ]
                if(len(value_i[i% len(value_i)])==2): 
                    line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
                else:
                    line_bot_api.reply_message(event.reply_token,ImageMessageURL(value_i[i% len(value_i)]))

            elif  input_message in ['爆死','綠色惡魔','花凜','保底','抽爆','母豬石','銀紙']:
                value_i = [
                    "https://i.imgur.com/SuPGWfM.jpg",   
                    "https://i.imgur.com/HmhqVvi.jpg",  
                    "https://i.imgur.com/48iPeaK.jpg",
                    "https://i.imgur.com/e3Jq6Fm.jpg",
                    "https://i.imgur.com/VnHG8mp.jpg",   
                    "https://i.imgur.com/wSATqcr.jpg",  
                    "https://i.imgur.com/6Vhl6F5.jpg",
                    "https://i.imgur.com/daXeV4b.jpg",
                    "https://i.imgur.com/o8rO3n1.jpg",   
                    "https://i.imgur.com/267Ssh5.jpg",  
                    "https://i.imgur.com/9Tt4qJp.jpg",
                    "https://i.imgur.com/ctZT1kg.jpg",
                    "https://i.imgur.com/RRWeKtN.jpg",
                    "https://i.imgur.com/chxKxsG.jpg",
                    "https://i.imgur.com/pWY8jVP.jpg",
                    "https://i.imgur.com/ChF4Znh.jpg",   
                    "https://i.imgur.com/Q8yr0a2.jpg",  
                    "https://i.imgur.com/vm7ekUp.jpg",
                    "https://i.imgur.com/HxuU6fW.jpg",
                    "https://i.imgur.com/1jtV5XT.jpg"
                ]
                line_bot_api.reply_message(event.reply_token,ImageMessageURL(value_i[i% len(value_i)]))

            elif input_message in ['你沒有妹妹','妹妹','いもうと']:
                value_i = [
                    ImageMessageURL("https://i.imgur.com/Hb24JxT.jpg"),
                    TextSendMessage(text = "那種東西不存在的呦~~"), 
                    TextSendMessage(text = "是指璃乃醬還是茜里醬又或者是栞栞呢？"),
                    ImageMessageURL("https://i.imgur.com/rix94rm.jpg"),
                    VideoMessageURL("https://i.imgur.com/cEV6Xmb")
                ]
                line_bot_api.reply_message(event.reply_token,value_i[i% len(value_i)])

            elif input_message[:2] == '我就' and len(input_message)<=6 :
                if input_message[2] == '爛':
                    value_i = [
                        'https://i.imgur.com/ZqjhK79.jpg',   
                        'https://i.imgur.com/nXsxbUW.jpg'
                    ]
                    line_bot_api.reply_message(event.reply_token,ImageMessageURL(value_i[i% len(value_i)]))
                else:
                    value_i = [
                        'https://i.imgur.com/4I79zqs.png',   
                        'https://i.imgur.com/88pRc9Q.png',  
                        'https://i.imgur.com/2OfFdhk.png'
                    ]
                    value_color = [
                        'https://i.imgur.com/I7VUOz5.png',   
                        'https://i.imgur.com/wxgQArs.png',  
                        'https://i.imgur.com/G4PNCSM.png',
                        'https://scdn.line-apps.com/n/channel_devcenter/img/flexsnapshot/clip/clip15.png',  
                        'https://i.imgur.com/sXetQPr.png'
                    ]
                    line_bot_api.reply_message(event.reply_token,image_bubble_message(value_i[i% len(value_i)],input_message,value_color[i% len(value_color)]))
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    ### 伊麗莎白牧場 ###
    ### エリザベスパーク牧場 ###
    ### 伊麗莎白牧場 ###
            elif input_message in ['栞','小栞','西歐力','シオリ','病弓','栞栞']:
                value_i = [
                    ['繪師: GaaRa-pixiv',          'https://i.imgur.com/7TXClz2.jpg'],
                    ['繪師: Mobu-pixiv',           'https://i.imgur.com/rGLO0Po.jpg'],
                    ['繪師: 桜庭ロイヤル-pixiv',    'https://i.imgur.com/bEdh6hw.jpg'],
                    ['繪師: 心みんとん-pixiv',      'https://i.imgur.com/G2Lp8sK.jpg'],
                    ['繪師: @tamakaga-twitter',    'https://i.imgur.com/mLejb61.jpg'],
                    ['繪師: @yantaro5446-twitter', 'https://i.imgur.com/YJhCqJ5.jpg'],
                    ['繪師: @YAZI114-twitter',     'https://i.imgur.com/BDH0f10.jpg'],
                    ['繪師: しぇるてぃー-pixiv',    'https://i.imgur.com/O39Sjdk.jpg'],
                    ['繪師: アイダ-pixiv',          'https://i.imgur.com/h19VB6a.jpg'],
                    ['繪師: aono-pixiv',           'https://i.imgur.com/bZdjH05.jpg'],
                    ['繪師: 紫桐シート-pixiv',      'https://i.imgur.com/GsZ8AOa.jpg'],
                    ['繪師: ダーゴ-pixiv',          'https://i.imgur.com/waFo95L.jpg'],
                    ['繪師: まりぴ-pixiv',          'https://i.imgur.com/Xe1DAOC.jpg'],
                    ['繪師: まりぴ-pixiv',          'https://i.imgur.com/3JQbmuO.jpg'],
                    ['繪師: たく庵-pixiv',          'https://i.imgur.com/NkPh6LN.jpg'],
                    ['繪師: ペヤンキー-pixiv',      'https://i.imgur.com/Bgn3DWb.jpg'],
                    ['繪師: @Mali_apex-twitter',   'https://i.imgur.com/svUIcft.jpg'],
                    ['繪師: 室町アツシ-pixiv',      'https://i.imgur.com/uW2nT6R.jpg'],
                    ['繪師: 室町アツシ-pixiv',      'https://i.imgur.com/QfZkQ3i.jpg'],
                    ['繪師: 室町アツシ-pixiv',      'https://i.imgur.com/0pQ0MJ2.jpg'],
                    ['繪師: @yantaro5446-twitter', 'https://i.imgur.com/ehHOj1N.jpg'],
                    ['繪師: @minatoaya-twitter',   'https://i.imgur.com/y6tc0NH.jpg'],
                    ['繪師: @AraiGyuren-twitter',  'https://i.imgur.com/EAq3v57.jpg'],
                    ['繪師: @AraiGyuren-twitter',  'https://i.imgur.com/WxzH08h.jpg'],
                    ['繪師: あんず-pixiv',          'https://i.imgur.com/1bC2LeP.jpg'],
                    ['繪師: @mata065026-twitter',  'https://i.imgur.com/QQpeAmy.jpg',  'https://i.imgur.com/2e869YB.jpg']
                ]
                if(len(value_i[i% len(value_i)])==3):
                    line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1]),ImageMessageURL(value_i[i% len(value_i)][2])])
                elif(len(value_i[i% len(value_i)])==2): 
                    line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
            elif input_message in ['真陽','マヒル','奶牛']:
                value_i = [
                    ['繪師: うまるつふり-pixiv',            'https://i.imgur.com/4ezsFUo.jpg'],
                    ['繪師: つきしろ やよい-pixiv',         'https://i.imgur.com/edYYsYN.jpg']
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
            elif input_message in ['鈴','リン','森近鈴','松鼠','遊俠鈴']:
                value_i = [
                    ['繪師: Zn-pixiv',             'https://i.imgur.com/9tSsHEF.jpg'],
                    ['繪師: ダーゴ-pixiv',         'https://i.imgur.com/8kyQmGJ.jpg'],
                    ['繪師: ジヤス-pixiv',         'https://i.imgur.com/fLy85C0.jpg'],
                    ['繪師: ヒーロー-pixiv',       'https://i.imgur.com/vC8ZmEr.jpg'],
                    ['繪師: たぬこ-pixiv',         'https://i.imgur.com/i8K8RmM.jpg'],
                    ['繪師: ねこまんま先生-pixiv',  'https://i.imgur.com/OXHf69V.jpg'],
                    ['繪師: Kiosk-pixiv',          'https://i.imgur.com/HrynwoW.jpg']
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
            elif input_message in ['莉瑪','リマ','羊駝']:
                value_i = [
                    ['繪師: ワタフジマコト-pixiv',   'https://i.imgur.com/dqeN5SV.jpg'],
                    ['繪師: gabo-pixiv',            'https://i.imgur.com/WmTQrGL.jpg'],
                    ['繪師: Kakao346-pixiv',        'https://i.imgur.com/aG3WL1j.jpg'],
                    ['繪師: 빙구-pixiv',            'https://i.imgur.com/yfhu5tu.jpg'],
                    ['繪師: かぼちゃ兎-pixiv',      'https://i.imgur.com/R13jfYh.jpg'],
                    ['繪師: ripe.C-pixiv',         'https://i.imgur.com/W88M1Ph.jpg',        'https://i.imgur.com/pUXMGKC.jpg']
                ]
                if len(value_i[i% len(value_i)])==3 :
                    line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1]),ImageMessageURL(value_i[i% len(value_i)][2])])
                elif len(value_i[i% len(value_i)])==2 :
                    line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
    ### 月光學院 ###
    ### ルーセント学院 ###
    ### 月光學院 ###
            elif input_message in ['月光學院','ルーセント学院']:
                value_i = [
                    ['繪師: 菖蒲-pixiv',         'https://i.imgur.com/vvzNgXT.jpg'],
                    ['繪師: S.U.-pixiv',        'https://i.imgur.com/2ayupbZ.jpg'],
                    ['繪師: Itoichi-pixiv',     'https://i.imgur.com/AsV2SJ2.jpg'],
                    ['繪師: ヤチモト-pixiv',     'https://i.imgur.com/NEuDpHQ.jpg'],
                    ['繪師: 関西ジン-pixiv',     'https://i.imgur.com/OUqJ5YL.jpg'],
                    ['繪師: やまだσ-pixiv',      'https://i.imgur.com/iGOKQtN.jpg']
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
            elif input_message in ['美咲','ミサキ','玉泉美咲','眼球法','萬聖美咲']:
                value_i = [
                    ['繪師: レオナート-pixiv',      'https://i.imgur.com/rDrtVAC.jpg'],
                    ['繪師: うましお-pixiv',        'https://i.imgur.com/CRQH9Ek.jpg'],
                    ['繪師: うまるつふり-pixiv',    'https://i.imgur.com/omIhOs8.jpg'],
                    ['繪師: しもん-pixiv',         'https://i.imgur.com/kKBE1aO.jpg'],
                    ['繪師: アイダ-pixiv',         'https://i.imgur.com/MU4Hykc.jpg']
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
            elif input_message in ['伊緒','イオ','支倉伊緒','魅魔','老師','伊歐派','泳裝伊緒']:
                value_i = [
                    ['繪師: 92M-pixiv',           'https://i.imgur.com/Ohkd2DO.jpg'],
                    ['繪師: りりか-pixiv',         'https://i.imgur.com/lev3VPT.jpg'],
                    ['繪師: ヤマブキイロ-pixiv',   'https://i.imgur.com/aWyGiYL.jpg'],
                    ['繪師: ひとつのなか-pixiv',   'https://i.imgur.com/DHUDWbD.jpg'],
                    ['繪師: みすコン-pixiv',       'https://i.imgur.com/zjAQsUn.jpg'],
                    ['繪師: sonchi-pixiv',        'https://i.imgur.com/m3qNyco.jpg']
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
            elif input_message in ['鈴奈','スズナ','美波鈴奈','暴弓','爆弓','模特兒','數學白癡','泳裝鈴奈']:
                value_i = [
                    ['繪師: ひとつのなか-pixiv',     'https://i.imgur.com/EjcU0Im.jpg'],
                    ['繪師: 結城辰也-pixiv',         'https://i.imgur.com/MkOrjea.jpg'],
                    ['繪師: YH-pixiv',              'https://i.imgur.com/JrrgGN6.jpg'],
                    ['繪師: 天雷-pixiv',            'https://i.imgur.com/e7OsQRB.jpg'],
                    ['繪師: ダーゴ-pixiv',          'https://i.imgur.com/ILNauCi.jpg'],
                    ['繪師: Rona-pixiv',            'https://i.imgur.com/fm0Pk7i.jpg'],
                    ['繪師: 電解水-pixiv',          'https://i.imgur.com/Wykgysq.jpg'],
                    ['繪師: フジフジ-pixiv',        'https://i.imgur.com/bXNXfuR.jpg'],
                    ['繪師: PoLa-pixiv',           'https://i.imgur.com/hxJbcud.jpg'],
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
    ### 拉比林斯 ###
    ### ラビリンス ###
    ### 拉比林斯 ###
            elif input_message in ['拉比林斯','ラビリンス']:
                value_i = [
                    ['繪師: みず-pixiv',          'https://i.imgur.com/F9SXxTp.jpg'],
                    ['繪師: ユキタカ-pixiv',      'https://i.imgur.com/iQVOxk2.jpg'],
                    ['繪師: みどりのちゃ-pixiv',  'https://i.imgur.com/2wbKiAy.jpg'],
                    ['繪師: 秋月リア-pixiv',      'https://i.imgur.com/NRgmRRj.jpg']
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
            elif input_message in ['靜流','シズル','星野靜流','姐姐','姊姊','弟控','情人節靜流']:
                value_i = [
                    ['繪師: watchdog_rol-pixiv',   'https://i.imgur.com/Xu8PE9b.jpg'],
                    ['繪師: まよ丼-pixiv',         'https://i.imgur.com/nF8bib2.jpg'],
                    ['繪師: ナ²-pixiv',            'https://i.imgur.com/a8BLBak.jpg'],
                    ['繪師: セーラ-pixiv',         'https://i.imgur.com/e9sXXu5.jpg'],
                    ['繪師: 坊橋夜泊-pixiv',       'https://i.imgur.com/YklV0js.jpg'],
                    ['繪師: ロアン-pixiv',         'https://i.imgur.com/hAK5NYP.jpg'],
                    ['繪師: みず-pixiv',           'https://i.imgur.com/oU6wWfr.jpg'],
                    ['繪師: ひとつのなか-pixiv',    'https://i.imgur.com/IlnJe8Z.jpg'],
                    ['繪師: 千里凌酱-pixiv',       'https://i.imgur.com/qcKvMcr.jpg'],
                    ['繪師: 千里凌酱-pixiv',       'https://i.imgur.com/1ANXoEU.jpg'],
                    ['繪師: ddolggol-pixiv',      'https://i.imgur.com/kBRxhWE.jpg'],
                    ['繪師: RYUKI-pixiv',         'https://i.imgur.com/Hzf2VCF.jpg'],
                    ['繪師: Itoichi-pixiv',       'https://i.imgur.com/3hf7n4q.jpg'],
                    ['繪師: horosuku-pixiv',      'https://i.imgur.com/aLWX0XE.png'],
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
            elif input_message in ['妹弓','梨乃','璃乃','リノ','智障','笨蛋','衣之咲璃乃','奇幻璃乃']:
                value_i = [
                    ['https://i.imgur.com/1eLEkSN.jpg'],
                    ['繪師: 真崎ケイ-pixiv',           'https://i.imgur.com/uKiWtdI.jpg'],
                    ['繪師: Mauve-pixiv',              'https://i.imgur.com/3SBQq5o.jpg'],
                    ['繪師: HIROKAZU-pixiv',           'https://i.imgur.com/BWXJYH8.jpg'],
                    ['繪師: HIROKAZU-pixiv',           'https://i.imgur.com/OlNs5LG.jpg'],
                    ['繪師: HIROKAZU-pixiv',           'https://i.imgur.com/lD2qFUi.jpg'],
                    ['繪師: HIROKAZU-pixiv',           'https://i.imgur.com/qSiPpAc.jpg'],
                    ['繪師: HIROKAZU-pixiv',           'https://i.imgur.com/hJitlbn.jpg'],
                    ['繪師: みず-pixiv',               'https://i.imgur.com/ul5x7d4.jpg'],
                    ['繪師: アイダ-pixiv',             'https://i.imgur.com/RTySuyH.jpg'],
                    ['繪師: @hirokazutw-twitter',      'https://i.imgur.com/U2MBZb8.jpg'],
                    ['繪師: @yantaro5446-twitter',     'https://i.imgur.com/eCSCr5x.jpg']
                ]
                if(len(value_i[i% len(value_i)])==2): 
                    line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
                else:
                    line_bot_api.reply_message(event.reply_token,ImageMessageURL(value_i[i% len(value_i)][0]))
    ### 森林守衛 ###
    ### フォレスティエ ###
    ### 森林守衛 ###
            elif input_message in ['美里','愛川美里','ミサト','聖母','美里老師','水母','泳裝美里']:
                value_i = [
                    ['繪師: @monmon_shimon_-twitter',   'https://i.imgur.com/QsArrQW.jpg'],
                    ['繪師: @Hello_pty-twitter',        'https://i.imgur.com/88X1SpO.jpg'],
                    ['繪師: @shotenana-twitter',        'https://i.imgur.com/671lWeD.jpg'],
                    ['繪師: @teffish-twitter',          'https://i.imgur.com/gyiQlHA.jpg'],
                    ['繪師: @92M-twitter',              'https://i.imgur.com/SdgoaDF.jpg'],
                    ['繪師: ヤマブキイロ-pixiv',         'https://i.imgur.com/zdgNpBt.jpg'],
                    ['繪師: ぼたやん-pixiv',             'https://i.imgur.com/iK5bus4.jpg'],
                    ['繪師: らんち-pixiv',               'https://i.imgur.com/PR3QIKs.jpg'],
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
            elif input_message in ['碧','アオイ','雙葉碧','香菜弓'] or (input_message[:2] == '邊緣' and len(input_message) <= 4) :
                value_i = [
                    ['繪師: @kurororo_rororo-twitter',     'https://i.imgur.com/B9I4bm1.jpg'],
                    ['繪師: ミチル-pixiv',                 'https://i.imgur.com/FVpUqpf.jpg'],
                    ['繪師: やま兎-pixiv',                 'https://i.imgur.com/7B82lli.jpg'],
                    ['繪師: すけsk-pixiv',                 'https://i.imgur.com/Mmw25L7.jpg'],
                    ['繪師: 秋ナス-pixiv',                 'https://i.imgur.com/cUPv6eu.jpg'],
                    ['繪師: 桜木ゆうき-pixiv',             'https://i.imgur.com/kiHg9WS.jpg'],
                    ['繪師: 鳩家-pixiv',                   'https://i.imgur.com/2J64V6T.jpg'],
                    ['繪師: mare II-pixiv',               'https://i.imgur.com/jQ9NYWp.jpg'],
                    ['繪師: @oriknp-twitter',             'https://i.imgur.com/Hgn9YeX.jpg'],
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
            elif input_message in ['初音','ハツネ','柏崎初音','睡美人','泳裝初音']:
                value_i = [
                    ['繪師: ヤンタロウ-pixiv',          'https://i.imgur.com/QQ5alwd.jpg'],
                    ['繪師: TYTS-pixiv',               'https://i.imgur.com/jTo5qH3.jpg'],
                    ['繪師: 結城辰也-pixiv',            'https://i.imgur.com/UtkMYdI.jpg'],
                    ['繪師: ゆりりん-pixiv',            'https://i.imgur.com/5E6XgR8.jpg'],
                    ['繪師: ジャンク堂-pixiv',          'https://i.imgur.com/WTIywxi.jpg'],
                    ['繪師: meel-pixiv',               'https://i.imgur.com/xN2lnOm.jpg'],
                    ['繪師: 天雷-pixiv',               'https://i.imgur.com/F788xfj.jpg'],
                    ['繪師: sonchi-pixiv',             'https://i.imgur.com/AXTx6rO.jpg'],
                    ['繪師: ゆんみ-pixiv',              'https://i.imgur.com/2DJUfQU.jpg'],
                    ['繪師: ひことう(彥灯)-pixiv',      'https://i.imgur.com/5JawGjF.jpg'],
                    ['繪師: @men0105-twitter',         'https://i.imgur.com/MQxElt8.jpg'],
                    ['繪師: @EN6cUMxx0rE6FFz-twitter', 'https://i.imgur.com/QxdVINo.jpg'],
                    ['繪師: Misekiss-pixiv',           'https://i.imgur.com/t6cncRh.jpg'],
                    ['繪師: @AraiGyuren-twitter',      'https://i.imgur.com/9oAUgeY.jpg'],
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
    ### 純白之翼 蘭德索爾分部 ###
    ### ヴァイスフリューゲル ランドソル支部 ###
    ### 純白之翼 ###
            elif input_message in ['純白之翼','ヴァイスフリューゲル ランドソル支部','純白之翼 蘭德索爾分部','奇葩公會']:
                value_i = [
                    ['繪師: ぬるぷよ-pixiv',          'https://i.imgur.com/tio37LX.jpg'],
                    ['繪師: なかひま-pixiv',          'https://i.imgur.com/hyxY4Hi.jpg'],
                    ['繪師: うせつ（右折）-pixiv',     'https://i.imgur.com/DANzNSk.jpg']
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
            elif input_message in ['妮諾','ニノン','扇子','忍者','江戶妮諾']:
                value_i = [
                    ['繪師: たてじまうり-pixiv',      'https://i.imgur.com/e1CEWSd.jpg'],
                    ['繪師: ぬるぷよ-pixiv',          'https://i.imgur.com/UMpxZQ7.jpg'],
                    ['繪師: S.U.-pixiv',             'https://i.imgur.com/8YWxDvV.jpg'],
                    ['繪師: phobishu-pixiv',         'https://i.imgur.com/1vWMYAr.jpg']
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
            elif input_message in ['莫妮卡','モニカ','毛二力','Monika','monika','魔法少女莫妮卡']:
                value_i = [
                    ['跳到just monika彩蛋'],
                    ['繪師: まぉー。-pixiv',        'https://i.imgur.com/pHPN52u.jpg'],
                    ['繪師: 浣狸-pixiv',            'https://i.imgur.com/IZgpNuR.jpg'],
                    ['繪師: 水無月みず-pixiv',      'https://i.imgur.com/uqUbiik.jpg'],
                    ['繪師: 紅薙ようと-pixiv',      'https://i.imgur.com/8XffJLz.jpg'],
                    ['繪師: 引きニート-pixiv',      'https://i.imgur.com/duJmuoQ.jpg'],
                    ['繪師: AJ-pixiv',             'https://i.imgur.com/idWxFcC.jpg'],
                    ['繪師: さくじ-pixiv',          'https://i.imgur.com/ootpbPh.jpg'],
                    ['繪師: まぉー。-pixiv',        'https://i.imgur.com/id3cEAo.jpg'],
                ]
                try:
                    line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
                except:
                    value_i = [
                        ['騎士...君......\nj̶̧̄u̸̬͌s̸̡̋t̴̬͘ ̴̣̀m̸̪͘ỏ̶̺n̵̙̕ȉ̷̢ǩ̷̜ã̷̠',    '繪師: Yampa-pixiv',            'https://i.imgur.com/arYgHgh.jpg'],
                        ['騎士...君......\nj̶̧̄u̸̬͌s̸̡̋t̴̬͘ ̴̣̀m̸̪͘ỏ̶̺n̵̙̕ȉ̷̢ǩ̷̜ã̷̠',    '繪師: ヒシ馬-pixiv',           'https://i.imgur.com/QHIY62W.jpg'],
                        ['騎士...君......\nj̶̧̄u̸̬͌s̸̡̋t̴̬͘ ̴̣̀m̸̪͘ỏ̶̺n̵̙̕ȉ̷̢ǩ̷̜ã̷̠',    '繪師: 麦飴 アンプ-pixiv',       'https://i.imgur.com/v8Cu6fX.jpg'],
                        ['騎士...君......\nj̶̧̄u̸̬͌s̸̡̋t̴̬͘ ̴̣̀m̸̪͘ỏ̶̺n̵̙̕ȉ̷̢ǩ̷̜ã̷̠',    '繪師: Tsunゼイ-pixiv',         'https://i.imgur.com/GeiKkKn.jpg'],
                        ['騎士...君......\nj̶̧̄u̸̬͌s̸̡̋t̴̬͘ ̴̣̀m̸̪͘ỏ̶̺n̵̙̕ȉ̷̢ǩ̷̜ã̷̠',    '繪師: Sasoura-pixiv',          'https://i.imgur.com/B9FumFa.jpg'],
                        ['騎士...君......\nj̶̧̄u̸̬͌s̸̡̋t̴̬͘ ̴̣̀m̸̪͘ỏ̶̺n̵̙̕ȉ̷̢ǩ̷̜ã̷̠',    '繪師: Heaven’s Melody-pixiv',  'https://i.imgur.com/V7QaIkI.jpg'],
                        ['騎士...君......\nj̶̧̄u̸̬͌s̸̡̋t̴̬͘ ̴̣̀m̸̪͘ỏ̶̺n̵̙̕ȉ̷̢ǩ̷̜ã̷̠',    '繪師: 麦飴 アンプ-pixiv',       'https://i.imgur.com/j8JOeW8.jpg'],
                        ['騎士...君......\nj̶̧̄u̸̬͌s̸̡̋t̴̬͘ ̴̣̀m̸̪͘ỏ̶̺n̵̙̕ȉ̷̢ǩ̷̜ã̷̠',    '繪師: Satchel-pixiv',          'https://i.imgur.com/MB0QAZv.jpg'],
                        ['騎士...君......\nj̶̧̄u̸̬͌s̸̡̋t̴̬͘ ̴̣̀m̸̪͘ỏ̶̺n̵̙̕ȉ̷̢ǩ̷̜ã̷̠',    '繪師: HOmme-pixiv',            'https://i.imgur.com/Wop3hWH.jpg']
                    ]
                    line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)][0]),TextSendMessage(text = value_i[i% len(value_i)][1]),ImageMessageURL(value_i[i% len(value_i)][2])])
            elif input_message in ['空花','クウカ','抖M','抖m','江戶空花'] :
                value_i = [
                    ['繪師: ダーゴ-pixiv',        'https://i.imgur.com/JagI34h.jpg'],
                    ['繪師: ジヤス-pixiv',        'https://i.imgur.com/J8pKPT0.jpg'],
                    ['繪師: 桶乃かもく-pixiv',    'https://i.imgur.com/u5OAmLp.jpg'],
                    ['繪師: たぐ-pixiv',          'https://i.imgur.com/2gUWFwE.jpg'],
                    ['繪師: えぴ-pixiv',          'https://i.imgur.com/HkxfmUi.jpg'],
                    ['繪師: S.U.-pixiv',          'https://i.imgur.com/VVWeLcP.jpg']
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
            elif input_message in ['步未','アユミ','石橋步未','路人妹' ,'路人','奇幻步未'] :
                value_i = [
                    ['繪師: あやみゆき-pixiv',      'https://i.imgur.com/wugza8u.jpg'],
                    ['繪師: セランポーレ-pixiv',    'https://i.imgur.com/YgCOdxJ.jpg'],
                    ['繪師: Acuma-pixiv',          'https://i.imgur.com/2L8K0D4.jpg'],
                    ['繪師: 巧克力酱嗷-pixiv',      'https://i.imgur.com/HVaTlao.jpg'],
                    ['繪師: セーリュー-pixiv',      'https://i.imgur.com/eAt5NmX.jpg'],
                    ['繪師: スギユウ-pixiv',        'https://i.imgur.com/pf414Hl.jpg'],
                    ['繪師: 関西ジン-pixiv',        'https://i.imgur.com/n33p8Nr.jpg'],
                    ['繪師: ぐま-pixiv',            'https://i.imgur.com/cKwmATV.jpg'],
                    ['繪師: スギユウ-pixiv',        'https://i.imgur.com/fG2T97o.jpg']
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
            elif input_message in ['雪','アユミ','小雪','虹村雪','雪哥','偽娘','女装大佬','自戀狂'] :
                value_i = [
                    ['繪師: ダーゴ-pixiv',      'https://i.imgur.com/5WVPTLL.jpg'],
                    ['繪師: ねこちゃん-pixiv',   'https://i.imgur.com/6eQnJpA.jpg'],
                    ['繪師: りこ-pixiv',        'https://i.imgur.com/qQi6c2M.jpg'],
                    ['繪師: りこ-pixiv',        'https://i.imgur.com/aoMKsKA.jpg'],
                    ['繪師: ASLE-pixiv',        'https://i.imgur.com/ptmTKlR.jpg'],
                    ['繪師: みさき-pixiv',      'https://i.imgur.com/5FBxwBT.jpg'],
                    ['繪師: ぐっち庵-pixiv',    'https://i.imgur.com/AeoEaDd.jpg']
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
    ### 咲戀救護院 ###
    ### サレンディア救護院 ###
    ### 救護院 ###
            elif input_message in ['咲戀救護院','サレンディア救護院','救護院']:
                value_i = [
                    ['繪師: S.U.-pixiv',       'https://i.imgur.com/7gMuqoy.jpg'],
                    ['繪師: AJ-pixiv',         'https://i.imgur.com/tzQswOy.jpg'],
                    ['繪師: ヤチモト-pixiv',    'https://i.imgur.com/BQpIStn.jpg']
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
            elif input_message in ['咲戀','咲戀媽媽','充電寶','泳媽','媽','サレン','泳裝咲戀','聖誕咲戀']:
                value_i = [
                    ['繪師: らんち-pixiv',              'https://i.imgur.com/JV5BTEz.jpg'],
                    ['繪師: hemachi-pixiv',            'https://i.imgur.com/2teJ0AL.jpg'],
                    ['繪師: SeeUmai-pixiv',            'https://i.imgur.com/8jiJdzM.jpg'],
                    ['繪師: カケル-pixiv',              'https://i.imgur.com/LM8RSJw.jpg'],
                    ['繪師: つかさ-pixiv',              'https://i.imgur.com/vvwxljH.jpg'],
                    ['繪師: アリア-pixiv',              'https://i.imgur.com/HcHuwDl.jpg'],
                    ['繪師: atychi-pixiv',             'https://i.imgur.com/z8WnFpy.jpg'],
                    ['繪師: あんべよしろう-pixiv',      'https://i.imgur.com/3J0rt2k.jpg'],
                    ['繪師: EpicLoot-pixiv',           'https://i.imgur.com/C7PEdmq.jpg'],
                    ['繪師: ヒーロー-pixiv',            'https://i.imgur.com/HANfFFb.jpg'],
                    ['繪師: ZN (あえん)-pixiv',         'https://i.imgur.com/MI7NZIS.jpg'],
                    ['繪師: @MtxzBNBROukHQzl-twitter', 'https://i.imgur.com/CbGxQO3.jpg'],
                    ['繪師: ZN (あえん)-pixiv',         'https://i.imgur.com/UFMHwZb.jpg'],
                    ['繪師: むらさめしん-pixiv',        'https://i.imgur.com/j29GiaM.jpg'],
                    ['繪師: むらさめしん-pixiv',        'https://i.imgur.com/AYLcF6I.jpg'],
                    ['繪師: らんち-pixiv',              'https://i.imgur.com/C2Zkm3B.jpg'],
                    ['繪師: らんち-pixiv',              'https://i.imgur.com/ihylo6y.jpg'],
                    ['繪師: あむりた様2号-pixiv',       'https://i.imgur.com/pCqVbRJ.jpg'],
                    ['繪師: @_mi_rei-twitter',         'https://i.imgur.com/tCMlVhe.jpg']
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
            elif input_message in ['鈴莓','スズメ','女僕','恐怖份子','天野鈴莓','正月鈴莓','泳裝鈴莓']:
                value_i = [
                    ['繪師: ダーゴ-pixiv',     'https://i.imgur.com/Mj7Vxxc.jpg'],
                    ['繪師: ダーゴ-pixiv',     'https://i.imgur.com/YJMAbHJ.jpg'],
                    ['繪師: ダーゴ-pixiv',     'https://i.imgur.com/QduwCSX.jpg'],
                    ['繪師: ROIN-pixiv',      'https://i.imgur.com/k4weIQw.jpg'],
                    ['繪師: りこ-pixiv',      'https://i.imgur.com/zvnXYcT.jpg'],
                    ['繪師: Set-pixiv',       'https://i.imgur.com/z5wHpnK.jpg'],
                    ['繪師: 天雷-pixiv',      'https://i.imgur.com/yx82sjg.jpg'],
                    ['繪師: sonchi-pixiv',    'https://i.imgur.com/tAIXB6g.jpg']
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
            elif input_message in ['綾音','アヤネ','北條綾音','熊錘','噗吉','聖誕綾音']:
                value_i = [
                    ['繪師: 夢乃杜-pixiv',          'https://i.imgur.com/G4lAvYH.jpg'],
                    ['繪師: うまるつふり-pixiv',    'https://i.imgur.com/T0IabEQ.jpg'],
                    ['繪師: 世音-pixiv',           'https://i.imgur.com/vVMd7HJ.jpg'],
                    ['繪師: けいらん-pixiv',        'https://i.imgur.com/vZI82po.jpg'],
                    ['繪師: うまるつふり-pixiv',    'https://i.imgur.com/sA2s1hL.jpg'],
                    ['繪師: 天雷-pixiv',           'https://i.imgur.com/q4WHogN.png'],
                    ['繪師: ダーゴ-pixiv',         'https://i.imgur.com/Lz3mk9N.jpg']
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
            elif input_message in ['胡桃','クルミ','栗林胡桃','聖誕胡桃']:
                value_i = [
                    ['繪師: 関西ジン-pixiv',            'https://i.imgur.com/h5SinVW.jpg'],
                    ['繪師: ミュー-pixiv',              'https://i.imgur.com/CtTm2kO.jpg'],
                    ['繪師: AJ-pixiv',                  'https://i.imgur.com/iZlOaV3.jpg'],
                    ['繪師: えむ-pixiv',                'https://i.imgur.com/1mYlZ9n.jpg'],
                    ['繪師: RYUKI-pixiv',               'https://i.imgur.com/G64Xivs.jpg'],
                    ['繪師: ダーゴ-pixiv',              'https://i.imgur.com/YTTNWgL.jpg'],
                    ['繪師: @gucchiponponpon-twitter',  'https://i.imgur.com/Uj0jVzB.jpg'],
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
    ### 墨丘利財團 ###
    ### メルクリウス財団 ###
    ### 財團 ###
            elif input_message in ['墨丘利財團','メルクリウス財団','財團']:
                value_i = [
                    ['繪師: AJ-pixiv',           'https://i.imgur.com/S3Ld3So.jpg'],
                    ['繪師: 夜凪朝妃-pixiv',      'https://i.imgur.com/ZsHkXJm.jpg'],
                    ['繪師: ヤチモト-pixiv',      'https://i.imgur.com/Zo5tJYw.jpg'],
                    ['繪師: HIROKAZU-pixiv',     'https://i.imgur.com/7VNue19.jpg'],
                    ['繪師: 夜凪朝妃-pixiv',      'https://i.imgur.com/kVkppDM.jpg'],
                    ['繪師: AJ-pixiv',           'https://i.imgur.com/VJEvtlM.jpg'],
                    ['繪師: あかざてり-pixiv',    'https://i.imgur.com/LGWONXZ.jpg'],
                    ['繪師: こうちゃ。-pixiv',    'https://i.imgur.com/1eKDiOg.jpg']
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
            elif input_message in ['秋乃','アキノ','聖誕秋乃','墨丘利財團唯一指定三星','財團之恥']:
                value_i = [
                    ['繪師: みずなし-pixiv',           'https://i.imgur.com/nLPrz2D.jpg'],
                    ['繪師: ダーゴ-pixiv',             'https://i.imgur.com/8PEV511.jpg'],
                    ['繪師: 真宮原ヒトシゲ-pixiv',      'https://i.imgur.com/5wbSJ5G.jpg'],
                    ['繪師: ヒーロー-pixiv',           'https://i.imgur.com/0Ibk5HR.jpg'],
                    ['繪師: 天雷-pixiv',               'https://i.imgur.com/Pp7pMVe.jpg'],
                    ['繪師: sonchi-pixiv',             'https://i.imgur.com/b2w8CMp.jpg'],
                    ['繪師: ぐっち庵-pixiv',           'https://i.imgur.com/PM02VxP.jpg'],
                    ['繪師: @3gita219_-twitter',       'https://i.imgur.com/Cf8xbgM.jpg'],
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
            elif input_message in ['優花梨','聖誕優花梨','ユカリ','酒鬼']:
                value_i = [
                    ['繪師: けんぴゃっ-pixiv',              'https://i.imgur.com/3grit6p.jpg'],
                    ['繪師: 石川健太-pixiv',                'https://i.imgur.com/e28UBg8.jpg'],
                    ['繪師: 天雷-pixiv',                   'https://i.imgur.com/2ShceE9.jpg'],
                    ['繪師: 鳩尾-pixiv',                   'https://i.imgur.com/kFqvMMn.jpg'],
                    ['繪師: 昌未-pixiv',                   'https://i.imgur.com/Dv4rJgh.jpg'],
                    ['繪師: りこ-pixiv',                   'https://i.imgur.com/LQRJRp7.jpg'],
                    ['繪師: 7010-pixiv',                   'https://i.imgur.com/sU3Ceak.jpg'],
                    ['繪師: sonchi-pixiv',                 'https://i.imgur.com/5eHL47t.jpg'],
                    ['繪師: まぉー。-pixiv',                'https://i.imgur.com/x4WaX1b.jpg'],
                    ['繪師: ぐっち庵-pixiv',                'https://i.imgur.com/2n2O2q3.jpg'],
                    ['繪師: PTD-pixiv',                    'https://i.imgur.com/Hefwndh.jpg'],
                    ['繪師: ミュー-pixiv',                  'https://i.imgur.com/7bVx6fN.jpg'],
                    ['繪師: @srm_chi-twitter',             'https://i.imgur.com/cqoR7cE.jpg'],
                    ['繪師: @dosukoi_fresh-twitter',       'https://i.imgur.com/n4cY09W.jpg'],
                    ['繪師: @Akao_kito-twitter',           'https://i.imgur.com/rlmKHjU.jpg'],
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
            elif input_message in ['珠希','タマキ','宮坂珠希','貓劍','貓賊','泳裝珠希']:
                value_i = [
                    ['https://i.imgur.com/Y6Hubmx.jpg'],
                    ['繪師: Donutman-pixiv',       'https://i.imgur.com/7fsnRcy.jpg'],
                    ['繪師: トプ-pixiv',           'https://i.imgur.com/adKZbm0.jpg'],
                    ['繪師: 水無月みず-pixiv',      'https://i.imgur.com/IodPy4h.jpg'],
                    ['繪師: ROIN-pixiv',           'https://i.imgur.com/hgc0rr5.jpg'],
                    ['繪師: あんず-pixiv',         'https://i.imgur.com/uPj8mrO.jpg'],
                    ['繪師: ぐっち庵-pixiv',       'https://i.imgur.com/xKXragw.jpg'],
                    ['繪師: ダーゴ-pixiv',         'https://i.imgur.com/llc5HX0.jpg']
                ]
                if(len(value_i[i% len(value_i)])==2): 
                    line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
                else:
                    line_bot_api.reply_message(event.reply_token,ImageMessageURL(value_i[i% len(value_i)][0]))
            elif input_message in ['美冬','ユカリ','大神美冬','屠龍者','打工仔','泳裝美冬']:
                value_i = [
                    ['繪師: AJ-pixiv',             'https://i.imgur.com/YwHKCSK.jpg'],
                    ['繪師: ぐっち庵-pixiv',        'https://i.imgur.com/t0AagIv.jpg'],
                    ['繪師: プトン-pixiv',          'https://i.imgur.com/1I33uq2.jpg'],
                    ['繪師: れつな-pixiv',          'https://i.imgur.com/TiCccLi.jpg'],
                    ['繪師: あんず-pixiv',          'https://i.imgur.com/51bzHBf.jpg'],
                    ['繪師: リブッチ-pixiv',        'https://i.imgur.com/2hCLlqE.jpg'],
                    ['繪師: 水ようかん-pixiv',      'https://i.imgur.com/vOyBmZB.jpg'],
                    ['繪師: ミュー-pixiv',          'https://i.imgur.com/aAxUlIQ.jpg']
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
            elif input_message == '無人島':
                value_i = [
                    ['繪師: 161803393-pixiv',      'https://i.imgur.com/XYGSCyu.jpg'],
                    ['繪師: AJ-pixiv',             'https://i.imgur.com/yxXnL0e.jpg'],
                    ['繪師: あかざてり-pixiv',      'https://i.imgur.com/o2JUEOw.jpg']
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
    ### 自衛團 ###
    ### カォン自警団 ###
    ### 哞哞自衛隊 ###
            elif input_message in ['哞哞自衛隊','自衛隊','カォン自警団']:
                value_i = [
                    ['繪師: AJ-pixiv',                 'https://i.imgur.com/i9BKQpj.jpg'],
                    ['繪師: ぬるぷよ-pixiv',            'https://i.imgur.com/5BnCetn.jpg'],
                    ['繪師: AJ-pixiv',                 'https://i.imgur.com/EwCexQp.jpg'],
                    ['繪師: WaterRing-pixiv',          'https://i.imgur.com/qQGcoBX.jpg'],
                    ['繪師: MaJiang-pixiv',            'https://i.imgur.com/dArZxel.jpg'],
                    ['繪師: konigstigerchan-pixiv',    'https://i.imgur.com/kkNl4dX.jpg']
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
            elif input_message in ['真步','マホ','姬宫真步','真步公主','公主病','泳裝真步']:
                value_i = [
                    ['繪師: S.U.-pixiv',           'https://i.imgur.com/yfgrop2.jpg'],
                    ['繪師: ぺろんちょ-pixiv',      'https://i.imgur.com/npCDt3p.jpg'],
                    ['繪師: 猫小渣-pixiv',          'https://i.imgur.com/SLSkhAO.jpg'],
                    ['繪師: yamchu-pixiv',         'https://i.imgur.com/nbs4CXK.jpg'],
                    ['繪師: JMao-pixiv',           'https://i.imgur.com/qo2wk18.jpg'],
                    ['繪師: ダーゴ-pixiv',          'https://i.imgur.com/dn9kpoN.jpg'],
                    ['繪師: 水無月みず-pixiv',      'https://i.imgur.com/iNKJY7T.jpg'],
                    ['繪師: 傻蛋喵-pixiv',          'https://i.imgur.com/mp8YBnO.jpg'],
                    ['繪師: 傻蛋喵-pixiv',          'https://i.imgur.com/5ttEoW0.jpg'],
                    ['繪師: 7010-pixiv',           'https://i.imgur.com/7LNxWXT.jpg'],
                    ['繪師: 凤鸢-pixiv',            'https://i.imgur.com/PCK4fdC.jpg']
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
            elif input_message in ['霞','カスミ','驢妹','偵探','水瀨祈','魔法少女霞','阿里巴巴大霞','阿里巴巴大俠']:
                value_i = [
                    ['繪師: AJ-pixiv',                 'https://i.imgur.com/i9BKQpj.jpg'],
                    ['繪師: aono-pixiv',               'https://i.imgur.com/vTNr4Ow.jpg'],
                    ['RANK4霞，繪師: Mauve-pixiv',     'https://i.imgur.com/RY2NT5k.jpg'],
                    ['RANK7霞，繪師: Mauve-pixiv',     'https://i.imgur.com/4rmJYo4.jpg'],
                    ['RANK9霞，繪師: Mauve-pixiv',     'https://i.imgur.com/SNMRaLm.jpg'],
                    ['RANK10霞，繪師: Mauve-pixiv',    'https://i.imgur.com/wu8SXNS.jpg'],
                    ['繪師: みり-pixiv',               'https://i.imgur.com/MFPwEbM.jpg'],
                    ['繪師: ゆりりん-pixiv',           'https://i.imgur.com/xNXb4pA.jpg'],
                    ['繪師: あめ。-pixiv',             'https://i.imgur.com/mSfnH5W.jpg'],
                    ['繪師: 骨カワ-pixiv',             'https://i.imgur.com/cn6i63j.jpg'],
                    ['繪師: あやみゆき-pixiv',         'https://i.imgur.com/FQhW6Iw.jpg'],
                    ['繪師: 紫桐シート-pixiv',         'https://i.imgur.com/4zQde23.jpg'],
                    ['繪師: ド赤-pixiv',               'https://i.imgur.com/M57ENmC.jpg'],
                    ['繪師: みり-pixiv',               'https://i.imgur.com/gcywpch.jpg'],
                    ['繪師: @K_mugura-twitter',        'https://i.imgur.com/7xRISix.jpg'],
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
            elif input_message in ['真琴','マコト','安藝真琴','月月','泳裝真琴']:
                value_i = [
                    ['繪師: ヤチモト-pixiv',        'https://i.imgur.com/YTdk5FP.jpg'],
                    ['繪師: S.U.-pixiv',           'https://i.imgur.com/36q2Zwa.jpg'],
                    ['繪師: 大仲いと-pixiv',        'https://i.imgur.com/0craZVx.jpg'],
                    ['繪師: まりぴ-pixiv',          'https://i.imgur.com/nSF7lBr.jpg'],
                    ['繪師: たく庵-pixiv',          'https://i.imgur.com/iZGjsku.jpg'],
                    ['繪師: オウカ-pixiv',          'https://i.imgur.com/05eKQMD.jpg'],
                    ['繪師: イロナツキ-pixiv',      'https://i.imgur.com/cZCALd1.jpg'],
                    ['繪師: 菖蒲-pixiv',            'https://i.imgur.com/TrrZPmM.jpg'],
                    ['繪師: たく庵-pixiv',          'https://i.imgur.com/iBf5yCm.jpg'],
                    ['繪師: T.R-pixiv',             'https://i.imgur.com/BKZqUcK.jpg'],
                    ['繪師: @yamabuki003-twitter',  'https://i.imgur.com/euzOAdo.jpg'],
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
            elif input_message in ['香織','カオリ','琉球犬','狗拳','喜屋武香織','一拳超狗','泳裝香織'] :
                value_i = [
                    ['繪師: スギユウ-pixiv',        'https://i.imgur.com/FZIyjVx.jpg',      'https://i.imgur.com/aZiz6j3.jpg'],
                    ['繪師: S.U.-pixiv',           'https://i.imgur.com/WZjeK8G.jpg'],
                    ['繪師: ダーゴ-pixiv',          'https://i.imgur.com/wQa9Lxe.jpg'],
                    ['繪師: PlatiSU-pixiv',        'https://i.imgur.com/qDzfshJ.jpg'],
                    ['繪師: 水無月みず-pixiv',      'https://i.imgur.com/caFCsLp.jpg'],
                    ['繪師: スギユウ-pixiv',        'https://i.imgur.com/8bkYhUV.jpg'],
                    ['繪師: 鎖ノム-pixiv',          'https://i.imgur.com/QPEq9Sd.jpg'],
                    ['繪師: ダーゴ-pixiv',          'https://i.imgur.com/Y4jssR3.jpg'],
                    ['繪師: たく庵-pixiv',          'https://i.imgur.com/nu6whzU.jpg'],
                    ['繪師: B-PANG-pixiv',         'https://i.imgur.com/Jg3g95l.jpg']
                ]
                if len(value_i[i% len(value_i)])==3 :
                    line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1]),ImageMessageURL(value_i[i% len(value_i)][2])])
                elif len(value_i[i% len(value_i)])==2 :
                    line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
            elif (input_message[:2]=="霞你" or input_message[:3]=="霞 你") and len(input_message) <= 10 and len(input_message) > 3 :
                value_i = [
                    'https://i.imgur.com/cLEBJRb.jpg',
                    'https://i.imgur.com/kHctfll.jpg',
                    'https://i.imgur.com/vB6O4Cn.jpg',
                    'https://i.imgur.com/dpeNj7w.jpg',
                    'https://i.imgur.com/q5UCplw.jpg',
                    'https://i.imgur.com/xZ5dbJE.jpg',
                    'https://i.imgur.com/bq2SGqc.jpg',
                    'https://i.imgur.com/jlPUSW7.jpg',
                    'https://i.imgur.com/PNC4GzD.jpg',
                    'https://i.imgur.com/K3a5KOg.jpg',
                ]
                line_bot_api.reply_message(event.reply_token,ImageMessageURL(value_i[i% len(value_i)]))
    ### 暮光流星群 ###
    ### トワイライトキャラバン ###
    ### 暮光流星群 ###
            elif input_message in ['暮光流星群','トワイライトキャラバン']:
                value_i = [
                    ['繪師: ともす-pixiv',         'https://i.imgur.com/zNTr1xq.jpg'],
                    ['繪師: AJ-pixiv',            'https://i.imgur.com/dDVrb23.jpg'],
                    ['繪師: ぐっち庵-pixiv',       'https://i.imgur.com/Y467BCt.jpg'],
                    ['繪師: セーリュー-pixiv',     'https://i.imgur.com/CPf1OMX.jpg'],
                    ['繪師: 天雷-pixiv',          'https://i.imgur.com/Sm9Slhx.jpg'],
                    ['繪師: phobishu-pixiv',      'https://i.imgur.com/KvypMFZ.jpg']
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
            elif input_message in ['中二','アンナ','杏奈','修特帕魯','疾風之冥姬','泳裝杏奈']:
                value_i = [
                    ['繪師: Sora-pixiv',              'https://i.imgur.com/HA4G2C6.jpg'],
                    ['繪師: ヒーロー-pixiv',           'https://i.imgur.com/ZkSFlQj.jpg'],
                    ['繪師: amaxa-pixiv',             'https://i.imgur.com/GG4vtha.jpg'],
                    ['繪師: しゅーくりいむ-pixiv',     'https://i.imgur.com/n61bHaS.jpg'],
                    ['繪師: しもん-pixiv',            'https://i.imgur.com/P7EI8P1.jpg'],
                    ['繪師: とも-pixiv',              'https://i.imgur.com/BCbLSNq.jpg'],
                    ['繪師: ガンバリーノ-pixiv',       'https://i.imgur.com/l4xW0QX.jpg'],
                    ['繪師: 竹村コウ-pixiv',          'https://i.imgur.com/1oz6l3d.jpg'],
                    ['繪師: レオナート-pixiv',        'https://i.imgur.com/HORyxNH.jpg'],
                    ['繪師: ミュー-pixiv',            'https://i.imgur.com/WD6zeRF.jpg'],
                    ['繪師: ひとつのなか-pixiv',      'https://i.imgur.com/8MMhoYT.jpg']
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
            elif input_message in ['流夏','ルカ','太刀洗流夏','大姐頭','流夏姐','泳裝流夏']:
                value_i = [
                    ['繪師: 天雷-pixiv',           'https://i.imgur.com/GMqJfYJ.jpg'],
                    ['繪師: ヒーロー-pixiv',       'https://i.imgur.com/SSuCGN5.jpg'],
                    ['繪師: ヒーロー-pixiv',       'https://i.imgur.com/6ZveKLb.jpg'],
                    ['繪師: sonchi-pixiv',        'https://i.imgur.com/1BQz6Ww.jpg'],
                    ['繪師: けんぴゃっ-pixiv',     'https://i.imgur.com/X03bPbh.jpg'],
                    ['繪師: @sub6o173-twitter',   'https://i.imgur.com/yNK5FlZ.jpg'],
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
            elif input_message in ['惠理子','エリコ','病嬌','情人節惠理子']:
                value_i = [
                    ['繪師: [新刊予約中]-pixiv',          'https://i.imgur.com/uRvRgVd.jpg'],
                    ['繪師: こしあん（たいやき）-pixiv',   'https://i.imgur.com/H2H57FL.jpg'],
                    ['繪師: 松倉N-pixiv',                 'https://i.imgur.com/wKhntyZ.jpg'],
                    ['繪師: めひしば-pixiv',              'https://i.imgur.com/dkilTgI.jpg'],
                    ['繪師: 一二三千代子-pixiv',          'https://i.imgur.com/18h4NHn.jpg'],
                    ['繪師: みィむ-pixiv',               'https://i.imgur.com/I7RaZgp.jpg'],
                    ['繪師: ひとつのなか-pixiv',          'https://i.imgur.com/EJobar4.jpg'],
                    ['繪師: Alisia-pixiv',               'https://i.imgur.com/7EmzmG9.jpg'],
                    ['繪師: MISACHU-pixiv',              'https://i.imgur.com/OfL7p6A.jpg'],
                    ['繪師: いず-pixiv',                 'https://i.imgur.com/zYcxoKw.jpg'],
                    ['繪師: Kinjin-pixiv',               'https://i.imgur.com/PLE4xYE.jpg'],
                    ['繪師: sonchi-pixiv',               'https://i.imgur.com/NzE7Fe9.jpg']
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
            elif input_message in ['七七香','ナナカ','丹野七七香','收藏家','nnk','眼鏡法','77香','泳裝七七香']:
                value_i = [
                    ['繪師: ぐっち庵-pixiv',    'https://i.imgur.com/mAYPjo6.jpg'],
                    ['繪師: t-pixiv',          'https://i.imgur.com/NpR0ldi.jpg'],
                    ['繪師: ぐっち庵-pixiv',    'https://i.imgur.com/mz2yvzn.jpg'],
                    ['繪師: ☆-pixiv',          'https://i.imgur.com/Zi9h7ao.jpg']
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
            elif input_message in ['深月','ミツキ','宵濱深月','獨眼惡魔','藥劑師']:
                value_i = [
                    ['繪師: @orange_mix7-twitter',    'https://i.imgur.com/D7PTeVz.jpg'],
                    ['繪師: 関西ジン-pixiv',           'https://i.imgur.com/IZCAmHv.jpg']
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
    ### 慈樂之音 ###
    ### 偶像團 ###
    ### カルミナ ###
            elif input_message in ['慈樂之音','偶像團','カルミナ']:
                value_i = [
                    ['繪師: しぇるてぃー-pixiv',    'https://i.imgur.com/jdMLi5b.jpg'],
                    ['繪師: AJ-pixiv',             'https://i.imgur.com/mBRquki.jpg'],
                    ['繪師: Sora-pixiv',           'https://i.imgur.com/z6zzyTr.jpg'],
                    ['繪師: カツラギ-pixiv',        'https://i.imgur.com/gijrjyq.jpg'],
                    ['繪師: カツラギ-pixiv',        'https://i.imgur.com/ySfq705.jpg'],
                    ['繪師: カツラギ-pixiv',        'https://i.imgur.com/lYlhSEd.jpg'],
                    ['繪師: 天雷-pixiv',            'https://i.imgur.com/gHOXVVH.jpg']
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
            elif input_message in ['紡希','ツムギ','繭宮紡希','萬聖紡希']:
                value_i = [
                    ['繪師: ひとつのなか-pixiv',   'https://i.imgur.com/Lhk5Uxh.jpg'],
                    ['繪師: 竹村コウ-pixiv',       'https://i.imgur.com/pqU4Yk2.jpg'],
                    ['繪師: むぐら-pixiv',         'https://i.imgur.com/54XO9cK.jpg'],
                    ['繪師: むぐら-pixiv',         'https://i.imgur.com/3VvuAmV.jpg'],
                    ['繪師: カツラギ-pixiv',       'https://i.imgur.com/vvtliTH.jpg'],
                    ['繪師: 竹村コウ-pixiv',       'https://i.imgur.com/k34TQEO.jpg'],
                    ['繪師: むぐら-pixiv',         'https://i.imgur.com/9mzwRdQ.jpg'],
                    ['繪師: ダーゴ-pixiv',         'https://i.imgur.com/AhkLOWp.png'],
                    ['繪師: むぐら-pixiv',         'https://i.imgur.com/zclpp4e.jpg'],
                    ['繪師: 桜庭ロイヤル-pixiv',    'https://i.imgur.com/n5sgyPI.jpg'],
                    ['繪師: ひとつのなか-pixiv',    'https://i.imgur.com/Pp3lTbh.jpg'],
                    ['繪師: @imonazun-twitter',    'https://i.imgur.com/1Lojpmp.jpg'],
                    ['繪師: @katukone-twitter',    'https://i.imgur.com/Wwxuf8k.jpg'],
                    ['繪師: @yukarite-twitter',    'https://i.imgur.com/ilE2xEN.jpg'],
                    ['繪師: 室町アツシ-pixiv',      'https://i.imgur.com/mLtmCiB.jpg'],
                    ['繪師: sonchi-pixiv',         'https://i.imgur.com/JOrbnjZ.jpg'],
                    ['繪師: @ryukisukune-twitter', 'https://i.imgur.com/XVX7FNf.jpg'],
                    ['繪師: @rekeysk-twitter',     'https://i.imgur.com/VDnCPOI.jpg'],
                    ['繪師: 浅りり介-pixiv',        'https://i.imgur.com/chwLBEy.jpg'],
                    ['繪師: a-（あーぼう）-pixiv',  'https://i.imgur.com/9Psb7Sa.jpg'],
                    ['繪師: しもん-pixiv',         'https://i.imgur.com/lRvWjGn.jpg'],
                    ['繪師: らんち-pixiv',         'https://i.imgur.com/ZHdeYGg.jpg',       'https://i.imgur.com/Iqw0nby.jpg'],
                ]
                if(len(value_i[i% len(value_i)])==3):
                    line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1]),ImageMessageURL(value_i[i% len(value_i)][2])])
                elif(len(value_i[i% len(value_i)])==2):
                    line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
            elif input_message in ['千歌','聖千','チカ','聖歌','聖誕千歌']:
                value_i = [
                    ['繪師: Sora-pixiv',           'https://i.imgur.com/2pOtito.png'],
                    ['繪師: 桜庭ロイヤル-pixiv',    'https://i.imgur.com/rOJ2zmG.png'],
                    ['繪師: 猫小渣-pixiv',         'https://i.imgur.com/obBJN0Q.jpg'],
                    ['繪師: いとね-pixiv',         'https://i.imgur.com/gUsae4d.jpg'],
                    ['繪師: 桜庭ロイヤル-pixiv',    'https://i.imgur.com/w1CzOB3.jpg'],
                    ['繪師: 天雷-pixiv',           'https://i.imgur.com/mQ8PXf3.png',    'https://i.imgur.com/JQGTauO.png'],
                    ['繪師: 天雷-pixiv',           'https://i.imgur.com/URkST7E.png']
                ]
                if(len(value_i[i% len(value_i)])==3):
                    line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1]),ImageMessageURL(value_i[i% len(value_i)][2])])
                elif(len(value_i[i% len(value_i)])==2):
                    line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
            elif input_message in ['小望','望','ノゾミ','偶像','櫻井望','公車','公車望','聖誕小望']:
                value_i = [
                    ['繪師: 天雷-pixiv',           'https://i.imgur.com/psEsocd.jpg'],
                    ['繪師: 桜庭ロイヤル-pixiv',   'https://i.imgur.com/XTyOttf.jpg'],
                    ['繪師: Mauve-pixiv',         'https://i.imgur.com/ACYRXh2.jpg'],
                    ['繪師: RYUKI-pixiv',         'https://i.imgur.com/0KGM43S.jpg'],
                    ['繪師: むぐら-pixiv',         'https://i.imgur.com/uAXCp1U.jpg'],
                    ['繪師: カツラギ-pixiv',       'https://i.imgur.com/7cjV2Aq.jpg'],
                    ['繪師: カツラギ-pixiv',       'https://i.imgur.com/pSSieQv.png'],
                    ['繪師: 天雷-pixiv',           'https://i.imgur.com/7sikqLO.png',    'https://i.imgur.com/woTEPVS.png'],
                    ['繪師: 天雷-pixiv',           'https://i.imgur.com/U1CkoZa.png',    'https://i.imgur.com/CW93OzQ.png'],
                    ['繪師: 天雷-pixiv',           'https://i.imgur.com/oNEwPwd.png'],
                    ['繪師: 天雷-pixiv',           'https://i.imgur.com/IGz2Grs.png'],
                    ['繪師: @nyum_serori-twitter', 'https://i.imgur.com/VhHDkgK.png'],
                ]
                if(len(value_i[i% len(value_i)])==3):
                    line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1]),ImageMessageURL(value_i[i% len(value_i)][2])])
                elif(len(value_i[i% len(value_i)])==2):
                    line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
    ### Diabolos ###
    ### 惡魔偽王國軍 ###
    ### ディアボロス ###
            elif input_message in ['惡魔偽王國軍','ディアボロス','Diabolos']:
                value_i = [
                    ['繪師: WaterRing-pixiv',    'https://i.imgur.com/rvhkokt.jpg'],
                    ['繪師: AJ-pixiv',           'https://i.imgur.com/YzifEB8.jpg'],
                    ['繪師: まゃ～吾郎-pixiv',    'https://i.imgur.com/uM6jzvU.jpg'],
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
            elif input_message in ['茜里','妹法','アカネ','惡魔雙子','雙子惡魔','天使茜里']:
                value_i = [
                    ['繪師: ROIN-pixiv',               'https://i.imgur.com/r3yBD71.jpg'],
                    ['繪師: ヤンタロウ-pixiv',          'https://i.imgur.com/QaAUaca.jpg'],
                    ['繪師: 六丸いなみ-pixiv',          'https://i.imgur.com/4BqqYmI.jpg'],
                    ['繪師: Chel-pixiv',               'https://i.imgur.com/vy9LI9P.jpg'],
                    ['繪師: ダーゴ-pixiv',              'https://i.imgur.com/BCdFbsb.jpg'],
                    ['繪師: Alpha-pixiv',              'https://i.imgur.com/00EaNly.jpg'],
                    ['繪師: ヒシ馬-pixiv',              'https://i.imgur.com/m0wqkKG.jpg'],
                    ['繪師: RYUKI-pixiv',              'https://i.imgur.com/cTrVg8W.jpg'],
                    ['繪師: @PK_PKP_PPK-twitter',      'https://i.imgur.com/Dg1bV2v.jpg'],
                    ['繪師: @ryukisukune-twitter',     'https://i.imgur.com/owbzSG6.jpg'],
                    ['繪師: @yantaro5446-twitter',     'https://i.imgur.com/x6Fknvq.jpg'],
                    ['繪師: 綾瀬水音-pixiv',            'https://i.imgur.com/x6Fknvq.jpg'],
                    ['繪師: GaaRa-pixiv',              'https://i.imgur.com/npB3vE4.jpg'],
                    ['繪師: @monmon_shimon_-twitter',  'https://i.imgur.com/ZYp0jro.jpg'],
                    ['繪師: Misekiss-pixiv',           'https://i.imgur.com/tDpQFlI.jpg'],
                    ['繪師: しもん-pixiv',              'https://i.imgur.com/vXay9QY.jpg'],
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
            elif input_message in ['依里','ヨリ','姐法','姊法','天使依里']:
                value_i = [
                    ['繪師: 桜木ゆうき-pixiv',         'https://i.imgur.com/rKMZZ9p.jpg'],
                    ['繪師: せら少佐-pixiv',           'https://i.imgur.com/qFyyK0f.jpg'],
                    ['繪師: せら少佐-pixiv',           'https://i.imgur.com/LqJJ3Wl.jpg'],
                    ['繪師: 水無川レイ-pixiv',         'https://i.imgur.com/DxmFDs2.jpg'],
                    ['繪師: 雪-pixiv',                'https://i.imgur.com/yAIAyq6.jpg'],
                    ['繪師: @diotheworld78-twitter',  'https://i.imgur.com/S9F6Bdi.jpg'],
                    ['繪師: @hirokazutw-twitter',     'https://i.imgur.com/oxNAS10.jpg'],
                    ['繪師: @rekeysk-twitter',        'https://i.imgur.com/POPNQ06.jpg'],
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
            elif input_message in ['台女','布丁','ミヤコ','宮子','幽靈','子宮','萬聖宮子']:
                value_i = [
                    ['https://i.imgur.com/czGSi5r.jpg'],
                    ['https://i.imgur.com/T6GdEjS.jpg'],
                    ['https://i.imgur.com/FlMnRvL.jpg'],
                    ['https://i.imgur.com/lBrFXU2.jpg'],
                    ['繪師: ダーゴ-pixiv',         'https://i.imgur.com/urboS8A.jpg'],
                    ['https://i.imgur.com/2y4LEhM.jpg'],
                    ['https://i.imgur.com/pHNzeHo.jpg'],
                    ['繪師: じゅんまぁち。-pixiv',  'https://i.imgur.com/ZhQRQWX.jpg'],
                    ['繪師: とゆり-pixiv',         'https://i.imgur.com/UBj2jpk.jpg'],
                    ['繪師: Saiste-pixiv',        'https://i.imgur.com/g8LGcjz.jpg'],
                    ['繪師: LUNIA-pixiv',         'https://i.imgur.com/1weUved.jpg'],
                    ['繪師: Tama-pixiv',          'https://i.imgur.com/BTpk9Yq.jpg',      'https://i.imgur.com/Vrh7bAy.jpg'],
                    ['繪師: ぬるぷよ-pixiv',       'https://i.imgur.com/wiuzd3A.jpg'],
                    ['繪師: 浣狸-pixiv',          'https://i.imgur.com/Jk5rN3V.jpg'],
                    ['繪師: ジヤス-pixiv',        'https://i.imgur.com/bxSfwej.jpg'],
                    ['繪師: ヒシ馬-pixiv',        'https://i.imgur.com/0KKeRJ9.jpg']
                ]
                if(len(value_i[i% len(value_i)])==3):
                    line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1]),ImageMessageURL(value_i[i% len(value_i)][2])])
                elif(len(value_i[i% len(value_i)])==2):
                    line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
                elif(len(value_i[i% len(value_i)])==1):
                    line_bot_api.reply_message(event.reply_token,ImageMessageURL(value_i[i% len(value_i)][0]))
            elif input_message in ['忍','シノブ','鬼父','上喜忍','骷髏老爸','萬聖忍']:
                value_i = [
                    ['繪師: Chel-pixiv',       'https://i.imgur.com/Ecyy4Lo.jpg'],
                    ['繪師: オウカ-pixiv',     'https://i.imgur.com/HsqExFk.jpg'],
                    ['繪師: あいち志保-pixiv',  'https://i.imgur.com/Uuh1OmA.jpg'],
                    ['繪師: けんせい-pixiv',    'https://i.imgur.com/t8KXMFH.jpg'],
                    ['繪師: Melings-pixiv',    'https://i.imgur.com/vlKcKzf.jpg'],
                    ['繪師: WaterRing-pixiv',  'https://i.imgur.com/xsA6n4v.jpg'],
                    ['繪師: 菖蒲-pixiv',       'https://i.imgur.com/L9xOGr6.jpg']
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
            elif input_message in ['伊莉亞','伊莉雅','イリヤ','吸血鬼','自爆','伊莉亞·奧恩斯坦','聖誕伊莉亞']:
                value_i = [
                    ['繪師: ハロン-pixiv',       'https://i.imgur.com/uoCNST9.jpg'],
                    ['繪師: 月満懐空-pixiv',     'https://i.imgur.com/JrgtzcM.jpg'],
                    ['繪師: HaneRu-pixiv',      'https://i.imgur.com/louJwWr.jpg'],
                    ['繪師: sonchi-pixiv',      'https://i.imgur.com/LNc1gxP.jpg'],
                    ['繪師: ごましを-pixiv',     'https://i.imgur.com/Y9KyKfW.jpg'],
                    ['繪師: SeeUmai-pixiv',     'https://i.imgur.com/M3U1cp9.jpg'],
                    ['繪師: ウエハラ蜂-pixiv',   'https://i.imgur.com/fUSYDa9.jpg'],
                    ['繪師: ROIN-pixiv',        'https://i.imgur.com/Ae3iVBz.jpg'],
                    ['繪師: まぉー。-pixiv',     'https://i.imgur.com/VjL6hUw.jpg'],
                    ['繪師: ぬるぷよ-pixiv',     'https://i.imgur.com/geVaLcE.jpg'],
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
    ### 破曉之星 ###
    ### トゥインクルウィッシュ ###
    ### 破曉之星 ###
            elif input_message in ['破曉之星','トゥインクルウィッシュ']:
                value_i = [
                    ['繪師: AJ-pixiv',         'https://i.imgur.com/sOsPvma.png'],
                    ['繪師: ﾘﾝ-pixiv',         'https://i.imgur.com/OSl2Oxy.jpg'],
                    ['繪師: ゆずゆい-pixiv',    'https://i.imgur.com/ajaKb2s.jpg'],
                    ['繪師: セーリュー-pixiv',  'https://i.imgur.com/R7Fm78o.jpg'],
                    ['繪師: ﾘﾝ-pixiv',         'https://i.imgur.com/aOq9p3O.jpg'],
                    ['繪師: だしごはん-pixiv',  'https://i.imgur.com/0CuWj4w.jpg']
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
            elif input_message in ['優衣','ユイ','草野優衣','ue','UE','Ue','公主優衣','正月優衣','儀式服優衣']:
                value_i = [
                    "https://i.imgur.com/vbyBSHq.jpg",
                    "https://i.imgur.com/GnNlRFB.jpg",
                    "https://i.imgur.com/QZSMdBh.jpg",
                    "https://i.imgur.com/fr1fgLH.jpg",
                    ['繪師: @Renian_-twitter',                'https://i.imgur.com/VYT9zWL.jpg'],
                    ['繪師: 狼巴子原型机-pixiv',               'https://i.imgur.com/GnPmRql.jpg'],
                    ['繪師: Itoichi-pixiv',                   'https://i.imgur.com/hQAJHCM.jpg'],
                    ['繪師: 佐倉のび太-pixiv',                 'https://i.imgur.com/5Og2eiV.jpg'],
                    ['繪師: どうたぬき＋3-pixiv',              'https://i.imgur.com/HaQCAZj.jpg'],
                    ['繪師: ゆりりん-pixiv',                   'https://i.imgur.com/KkmJwCP.jpg'],
                    ['繪師: HIROKAZU-pixiv',                   'https://i.imgur.com/taTPJjm.jpg'],
                    ['繪師: HIROKAZU-pixiv',                   'https://i.imgur.com/gYi5WRV.jpg'],
                    ['繪師: HIROKAZU-pixiv',                   'https://i.imgur.com/HYUSfq6.jpg'],
                    ['繪師: HIROKAZU-pixiv',                   'https://i.imgur.com/p3KsySu.jpg'],
                    ['繪師: HIROKAZU-pixiv',                   'https://i.imgur.com/JJsKQCY.jpg'],
                    ['繪師: HIROKAZU-pixiv',                   'https://i.imgur.com/6iBeNJE.jpg'],
                    ['繪師: HIROKAZU-pixiv',                   'https://i.imgur.com/N92Z60L.jpg'],
                    ['繪師: とも-pixiv',                       'https://i.imgur.com/dD8yXeo.jpg'],
                    ['為什麼，明明是初次見面\n我的心卻如此苦澀',  'https://i.imgur.com/x1Ggdnw.jpg'],
                    ['繪師: @shucream7777-twitter',            'https://i.imgur.com/KU2QcRe.jpg'],
                    ['繪師: 天雷-pixiv',                       'https://i.imgur.com/G3VKdFY.png'],
                    ['繪師: じゅんまぁち。-pixiv',              'https://i.imgur.com/jpSaEf6.png'],
                    ['繪師: たまかが-pixiv',                    'https://i.imgur.com/TEaqose.png'],
                    ['繪師: タモ-pixiv',                       'https://i.imgur.com/tzSIphi.png'],
                    ['繪師: 浅りり介-pixiv',                   'https://i.imgur.com/oIxsOID.png'],
                    ['繪師: らいでん-pixiv',                   'https://i.imgur.com/Ew6AxsU.png'],
                    ['繪師: 葉桜しょーは-pixiv',               'https://i.imgur.com/ZabcTz6.png'],
                    ['繪師: 山桂贰-pixiv',                     'https://i.imgur.com/MrMH7h6.png'],
                    ['繪師: サインこす-pixiv',                 'https://i.imgur.com/Z2cnTPz.png'],
                ]
                if(len(value_i[i% len(value_i)])==2): 
                    line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
                else:
                    line_bot_api.reply_message(event.reply_token,ImageMessageURL(value_i[i% len(value_i)]))
            elif input_message in ['日和','ヒヨリ','春咲日和','貓拳','正月日和','公主日和']:
                value_i = [
                    ['繪師: 薬草-pixiv',        'https://i.imgur.com/rqoos26.jpg'],
                    ['繪師: けんぴゃっ-pixiv',  'https://i.imgur.com/jyI0Ab7.jpg'],
                    ['繪師: K-y-pixiv',        'https://i.imgur.com/qGar6FW.jpg'],
                    ['繪師: 終わらない-pixiv',  'https://i.imgur.com/LsMnoio.jpg'],
                    ['繪師: 天雷-pixiv',        'https://i.imgur.com/8Z1ruEc.png'],
                    ['繪師: ダーゴ-pixiv',      'https://i.imgur.com/XqQEiS9.png'],
                    ['繪師: 赤尾キト-pixiv',    'https://i.imgur.com/4hmxmNx.png'],
                    ['繪師: まぉー。-pixiv',    'https://i.imgur.com/pGJJoVW.jpg',     'https://i.imgur.com/lQrWmEE.jpg'],
                ]
                if(len(value_i[i% len(value_i)])==2): 
                    line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
                elif(len(value_i[i% len(value_i)])==3):
                    line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1]),ImageMessageURL(value_i[i% len(value_i)][2])])
            elif input_message in ['怜','レイ','士條怜','怜大人','正月怜','萬聖怜']:
                value_i = [
                    ['繪師: 天雷-pixiv',           'https://i.imgur.com/Kx01yVD.png'],
                    ['繪師: ペヤンキー-pixiv',     'https://i.imgur.com/ECzvAdL.jpg'],
                    ['繪師: 四字熟語-pixiv',       'https://i.imgur.com/4bheK7u.jpg'],
                    ['繪師: 四字熟語-pixiv',       'https://i.imgur.com/CsStf0f.jpg'],
                    ['繪師: 四字熟語-pixiv',       'https://i.imgur.com/v5xplKt.jpg'],
                    ['繪師: あまな-pixiv',         'https://i.imgur.com/qWb9ieI.jpg'],
                    ['繪師: しもん-pixiv',         'https://i.imgur.com/e5bY3QZ.jpg'],
                    ['繪師: 浅りり介-pixiv',       'https://i.imgur.com/fpzSXsN.jpg'],
                    ['繪師: @yukin0128-twitter',  'https://i.imgur.com/bLfH0Vv.jpg'],
                    ['繪師: @yukin0128-twitter',  'https://i.imgur.com/oe3qV5i.jpg'],
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
            elif (input_message in ['對不起']) or (any(judger in input_message for judger in('對不起','ごめん')))and(any(judger in input_message for judger in('優衣','ユイ','UE','ue','優依'))):
                value_i = [
                    ['https://i.imgur.com/9pX6RP9.jpg',    '春咲日和同學...\n本來我還把你當作朋友的，但就算明天你就要死了，我也不會再去救你的'],
                    ['https://i.imgur.com/aNZsoIo.jpg',    '恩，我會守護好騎士君不讓害蟲靠近的'],
                    ['https://i.imgur.com/qALShyp.jpg',    '沒關係的，騎士君也希望我選擇原諒的吧 (舉槍~'],
                    ['https://i.imgur.com/kMY3H09.jpg',    '迫害優衣的繪師twitter: @yumeoi1884'],
                    ['https://i.imgur.com/QRAX6tt.jpg',    '糟蹋優衣的繪師: 翔たろう-pixiv'],
                    ['https://i.imgur.com/oR7M58R.jpg',    '欺凌優衣的繪師: ないん-pixiv'],
                    ['https://i.imgur.com/sDtxdxp.jpg',    '玩弄優衣的繪師: Apoidea-pixiv'],
                    ['https://i.imgur.com/BX8qxHs.jpg',    '捉弄優衣的繪師: Apoidea-pixiv'],
                    ['https://i.imgur.com/Vc1W7OA.jpg',    '偏愛真琴的繪師: 坊橋夜泊-pixiv'],
                    ['https://i.imgur.com/Jwqp2NT.jpg',    '學...學姊 明明是人家先來的'],
                    ['https://i.imgur.com/NvcMOxC.jpg',    '霞你真的是髒死了！！'],
                ]
                line_bot_api.reply_message(event.reply_token,[ImageMessageURL(value_i[i% len(value_i)][0]),TextSendMessage(text= value_i[i% len(value_i)][1])])
            elif '優依' in input_message and len(input_message)<=36:
                value_i = [
                    "騎士君開始連我的名字都記錯了嗎...",
                    "咦？是誰？",     
                    "不對不對，是優衣哦",
                    "罰寫三次哦，是優衣不是優依",
                    "哇啊啊，騎士君沒問題嗎？都叫錯人家的名字了",
                    "騎士君！記錯女孩子的名字可是很失禮的"
                ]
                line_bot_api.reply_message(event.reply_token,TextSendMessage(text = value_i[i% len(value_i)]))
    ### 小小甜心 ###
    ### リトルリリカル ###
    ### 小小甜心 ###
            elif input_message in ['小小甜心','リトルリリカル','27歲']:
                value_i = [
                    ['繪師: 鈴音れな-pixiv',      'https://i.imgur.com/aj1YCpG.jpg'],
                    ['繪師: けんぴゃっ-pixiv',    'https://i.imgur.com/hl1DEJ2.jpg'],
                    ['繪師: ひづき夜宵-pixiv',    'https://i.imgur.com/jCF6U7G.jpg'],
                    ['繪師: てれん-pixiv',        'https://i.imgur.com/6Wzr3NT.jpg'],
                    ['繪師: 音琶-pixiv',          'https://i.imgur.com/vtATPer.jpg'],
                    ['繪師: たかつ-pixiv',        'https://i.imgur.com/03vHTgr.jpg'],
                    ['繪師: 日下氏-pixiv',        'https://i.imgur.com/2IFsEOD.jpg'],
                    ['繪師: 関西ジン-pixiv',      'https://i.imgur.com/nbfL5h2.jpg'],
                    ['繪師: ねむいひと-pixiv',    'https://i.imgur.com/Ig53ubp.jpg'],
                    ['繪師: u_U-pixiv',          'https://i.imgur.com/C3O8gts.jpg'],
                    ['繪師: anno-pixiv',         'https://i.imgur.com/kSCbzaD.jpg'],
                    ['繪師: 結城辰也-pixiv',      'https://i.imgur.com/q3G8QlE.jpg'],
                    ['繪師: みどりのちゃ-pixiv',  'https://i.imgur.com/hoFZQxH.jpg'],
                    ['繪師: なつめえり-pixiv',    'https://i.imgur.com/Q7eQ5yq.jpg'],
                    ['繪師: しもん-pixiv',        'https://i.imgur.com/1J8qD4m.jpg']
                ]
                if(len(value_i[i% len(value_i)])==2): 
                    line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
                else:
                    line_bot_api.reply_message(event.reply_token,ImageMessageURL(value_i[i% len(value_i)]))
            elif input_message in ['8歲','八歲','キョウカ','冰川鏡華','鏡華','噴水蘿','鏡華媽媽','小倉唯' ,'傲嬌蘿','萬聖鏡華'] :
                value_i = [
                    'https://i.imgur.com/t9OWzlK.jpg',
                    'https://i.imgur.com/WyVngW7.jpg', 
                    'https://i.imgur.com/Xkj3sZB.jpg',
                    ['繪師: うめた-pixiv',                  'https://i.imgur.com/762cQ5O.jpg'],
                    ['繪師: @kazukiadumi-twitter',          'https://i.imgur.com/nkQhkYF.jpg'],
                    ['繪師: 真崎ケイ-pixiv',                'https://i.imgur.com/xhAOxG0.jpg'],
                    ['繪師: @koma_momozu-twitter',         'https://i.imgur.com/Hrcg9ej.jpg'],
                    ['繪師: @ryukisukune-twitter',         'https://i.imgur.com/yfLLbF7.jpg'],
                    ['繪師: @usagicandy_taku-twitter',     'https://i.imgur.com/sdnjww4.jpg'],
                    ['繪師: 真崎ケイ-pixiv',                'https://i.imgur.com/yx7vql2.jpg'],
                    ['繪師: ROIN-pixiv',                   'https://i.imgur.com/LeNI4fi.jpg'],
                    ['繪師: ほにゃる-pixiv',                'https://i.imgur.com/2bxofr2.jpg'],
                    ['繪師: 天雷-pixiv',                    'https://i.imgur.com/2ijIX5l.jpg'],
                    ['繪師: ひづき夜宵-pixiv',              'https://i.imgur.com/GFA4wh4.jpg']
                ]
                if(len(value_i[i% len(value_i)])==2): 
                    line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
                else:
                    line_bot_api.reply_message(event.reply_token,ImageMessageURL(value_i[i% len(value_i)]))
            elif input_message in ['美美','ミミ','茜美美','10歲','十歲','兔子','兔兔','天兔霸斷劍','人參霸斷劍','萬聖美美']:
                value_i = [
                    ['繪師: PoLa-pixiv',              'https://i.imgur.com/ztNebvM.jpg'],
                    ['繪師: PoLa-pixiv',              'https://i.imgur.com/ztNebvM.jpg'],
                    ['繪師: Chanifge-pixiv',          'https://i.imgur.com/f0YQOlU.jpg'],
                    ['繪師: えぴ-pixiv',              'https://i.imgur.com/I45pDDB.jpg'],
                    ['繪師: えぴ-pixiv',              'https://i.imgur.com/PzGh7bS.jpg'],
                    ['繪師: u_U-pixiv',               'https://i.imgur.com/Pws5qXb.jpg'],
                    ['繪師: Azel司令官-pixiv',         'https://i.imgur.com/Q8A9XBD.jpg'],
                    ['繪師: rokico-pixiv',            'https://i.imgur.com/m9MEYQU.jpg'],
                    ['繪師: rokico-pixiv',            'https://i.imgur.com/ux4WWXp.jpg'],
                    ['繪師: PTD-pixiv',               'https://i.imgur.com/2pbrdSi.jpg'],
                    ['繪師: ジヤス-pixiv',            'https://i.imgur.com/jZ6lkdk.jpg'],
                    ['繪師: u_U-pixiv',               'https://i.imgur.com/cYYGLEg.jpg'],
                    ['繪師: u_U-pixiv',               'https://i.imgur.com/LtqyIUC.jpg'],
                    ['繪師: rokico-pixiv',            'https://i.imgur.com/zbscNBC.jpg'],
                    ['繪師: @patrietta-twitter',      'https://i.imgur.com/myryFfF.jpg'],
                    ['繪師: @suzunonerena2-twitter',  'https://i.imgur.com/9BPXHg9.jpg'],
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
            elif input_message in ['禊','ミソギ','9歲','九歲','穗高禊','炸彈','屁孩','惡作劇','萬聖禊']:
                value_i = [
                    ['繪師: さくも-pixiv',        'https://i.imgur.com/sQdHme7.jpg'],
                    ['繪師: 秋鳩むぎ-pixiv',      'https://i.imgur.com/3kvw53A.jpg'],
                    ['繪師: とも-pixiv',          'https://i.imgur.com/plAbio1.jpg'],
                    ['繪師: とも-pixiv',          'https://i.imgur.com/Nd8jVpX.jpg'],
                    ['繪師: レオナート-pixiv',    'https://i.imgur.com/zKa4Av9.jpg'],
                    ['繪師: aono-pixiv',         'https://i.imgur.com/JQ5s2RI.jpg'],
                    ['繪師: レオナート-pixiv',    'https://i.imgur.com/8OlaltN.jpg'],
                    ['繪師: たかつ-pixiv',        'https://i.imgur.com/SDe1vYT.jpg'],
                    ['繪師: rokico-pixiv',       'https://i.imgur.com/NX02QeB.jpg'],
                    ['繪師: PoLa-pixiv',         'https://i.imgur.com/4vtP0W2.jpg'],
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
            elif  input_message in ['蘿莉','五等分的蘿莉','五等分的花嫁'] :
                value_i = [
                    "https://i.imgur.com/31NBFBl.png",   
                    "https://i.imgur.com/ZYYiagm.jpg",
                    ["繪師: たかつ-pixiv",      "https://i.imgur.com/5pojuIY.jpg"]
                ]
                if(len(value_i[i% len(value_i)])==2): 
                    line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
                else:
                    line_bot_api.reply_message(event.reply_token,ImageMessageURL(value_i[i% len(value_i)]))
    ### 優妮們 ###
    ### 好朋友社 ###
    ### なかよし部 ###
            elif input_message in ['優妮們','好朋友社','なかよし部','好朋友部']:
                value_i = [
                    ['繪師: 谷川犬兎-pixiv',       'https://i.imgur.com/tNSLFAv.jpg'],
                    ['繪師: 谷川犬兎-pixiv',       'https://i.imgur.com/g8peBoI.jpg'],
                    ['繪師: アイダ-pixiv',         'https://i.imgur.com/Y8b9KpL.jpg'],
                    ['繪師: カッシュ-pixiv',       'https://i.imgur.com/o5bjJkO.jpg'],
                    ['繪師: やま兎-pixiv',         'https://i.imgur.com/iChYvja.jpg'],
                    ['繪師: 竹四兎-pixiv',         'https://i.imgur.com/XW6Ilhi.jpg'],
                    ['繪師: ヒーロー-pixiv',       'https://i.imgur.com/18Wr2SL.jpg'],
                    ['繪師: ヒーロー-pixiv',       'https://i.imgur.com/6H3N2oi.jpg'],
                    ['繪師: みどりのちゃ-pixiv',   'https://i.imgur.com/rORyTAo.jpg'],
                    ['繪師: RYUKI-pixiv',         'https://i.imgur.com/vW28Kah.jpg'],
                    ['繪師: RYUKI-pixiv',         'https://i.imgur.com/7gQ2mvE.jpg'],
                    ['繪師: 夢追人形-pixiv',       'https://i.imgur.com/kKqICUL.jpg'],
                    ['繪師: @zuhonyanko-twitter', 'https://i.imgur.com/fOGFnLj.jpg'],
                    ['繪師: AJ-pixiv',            'https://i.imgur.com/q3rH2Nh.jpg']
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
            elif input_message in ['優妮','優尼','ユニ','前輩','優妮先輩','優妮學姊','真行寺由仁'] :
                value_i = [
                    ['繪師: 7010-pixiv',               'https://i.imgur.com/PgefTbO.jpg',      'https://i.imgur.com/Dd3cm46.jpg'],
                    ['繪師: @augment_girl-twitter',    'https://i.imgur.com/pvC5roc.jpg'],
                    ['繪師: もつ煮-pixiv',             'https://i.imgur.com/vqYJWmP.jpg'],
                    ['繪師: SeeRo-pixiv',              'https://i.imgur.com/qW0whyw.jpg'],
                    ['繪師: オウカ-pixiv',             'https://i.imgur.com/bayYULx.jpg'],
                    ['繪師: かのら-pixiv',             'https://i.imgur.com/8enbxjq.jpg'],
                    ['繪師: SeeUmai-pixiv',            'https://i.imgur.com/2KUXbMb.jpg'],
                    ['繪師: ばくP-pixiv',              'https://i.imgur.com/oRKXEqB.jpg'],
                    ['繪師: ヒーロー-pixiv',           'https://i.imgur.com/qGunDiI.jpg'],
                    ['繪師: うしむ-pixiv',             'https://i.imgur.com/y9rMskm.jpg'],
                    ['繪師: @Nabyssor-twitter',        'https://i.imgur.com/JkdzOu5.jpg'],
                    ['繪師: ジヤス-pixiv',             'https://i.imgur.com/yxUVHJp.jpg'],
                    ['繪師: ぼたやん-pixiv',           'https://i.imgur.com/90CfbfI.jpg'],
                    ['繪師: Misekiss-pixiv',          'https://i.imgur.com/11NxM0z.jpg'],
                    ['繪師: あむりた様2号-pixiv',      'https://i.imgur.com/18YKo54.png'],
                    ['繪師: Chariot Fish-FB',         'https://i.imgur.com/YNypBH8.png'],
                    ['繪師: PoLa-pixiv',              'https://i.imgur.com/ycGBb05.png'],
                    ['https://i.imgur.com/we20ZAK.jpg'],
                ]
                if len(value_i[i% len(value_i)])==3 :
                    line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1]),ImageMessageURL(value_i[i% len(value_i)][2])])
                elif len(value_i[i% len(value_i)])==2 :
                    line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
                elif len(value_i[i% len(value_i)])==1 :
                    line_bot_api.reply_message(event.reply_token,ImageMessageURL(value_i[i% len(value_i)][0]))
            elif input_message in ['克蘿依','黑江花子','花子','クロエ','華哥','不良','B80']:
                value_i = [
                    ['繪師: 92M-pixiv',            'https://i.imgur.com/XpHrtHx.jpg'],
                    ['繪師: むらさめしん-pixiv',    'https://i.imgur.com/2XBnrXb.jpg'],
                    ['繪師: あめ。-pixiv',         'https://i.imgur.com/iJLxVtr.jpg'],
                    ['繪師: あめ。-pixiv',         'https://i.imgur.com/WJtF51h.jpg'],
                    ['繪師: ねこ鳴都-pixiv',       'https://i.imgur.com/QwjcxRH.jpg'],
                    ['繪師: あめ。-pixiv',         'https://i.imgur.com/GKbJNJ0.jpg'],
                    ['繪師: 飛蝗-pixiv',           'https://i.imgur.com/qV6FfSV.jpg'],
                    ['繪師: やま兎-pixiv',         'https://i.imgur.com/B8ibPoy.jpg'],
                    ['繪師: 鉄人桃子-pixiv',       'https://i.imgur.com/CzUXDYU.jpg'],
                    ['繪師: ROIN-pixiv',          'https://i.imgur.com/VGBkgS2.jpg'],
                    ['繪師: ヒーロー-pixiv',       'https://i.imgur.com/qHRmLHL.jpg'],
                    ['繪師: ROIN-pixiv',          'https://i.imgur.com/8onaczp.jpg'],
                    ['繪師: やま兎-pixiv',         'https://i.imgur.com/dathr2M.jpg'],
                    ['繪師: AJ-pixiv',            'https://i.imgur.com/ITDNtcZ.jpg'],
                    ['繪師: まだら-pixiv',         'https://i.imgur.com/GVxFuSd.jpg'],
                    ['繪師: あめ。-pixiv',         'https://i.imgur.com/9yby12s.jpg'],
                    ['繪師: HIROKAZU-pixiv',      'https://i.imgur.com/z042FKZ.png'],
                    ['繪師: a-（あーぼう）-pixiv', 'https://i.imgur.com/RIRhzpM.png'],
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
            elif input_message in ['琪愛兒','風間千惠瑠','チエル','切嚕','ちぇるーん']:
                value_i = [
                    ['繪師: Kobi-pixiv',                'https://i.imgur.com/2XHfz4W.jpg'],
                    ['繪師: るがつき-pixiv',            'https://i.imgur.com/qqEU0LG.jpg'],
                    ['繪師: 玉蒔良-pixiv',              'https://i.imgur.com/YCMAVRl.jpg'],
                    ['繪師: AJ-pixiv',                  'https://i.imgur.com/ZiUEWJ6.jpg'],
                    ['繪師: カツラギ-pixiv',             'https://i.imgur.com/OgvJcSV.jpg'],
                    ['繪師: @momozizizi-twitter',       'https://i.imgur.com/KDYBz2m.jpg'],
                    ['繪師: DDDsunsky-pixiv',           'https://i.imgur.com/938DLHs.jpg'],
                    ['繪師: @fis8-twitter',             'https://i.imgur.com/o8JZoNX.jpg'],
                    ['繪師: @momozizizi-twitter',       'https://i.imgur.com/WkqDgdx.jpg'],
                    ['繪師: @meiya_pururun-twitter',    'https://i.imgur.com/1OxWYv9.jpg'],
                    ['繪師: @momozizizi-twitter',       'https://i.imgur.com/R9lb7d1.jpg'],
                    ['繪師: @momozizizi-twitter',       'https://i.imgur.com/Gnh0Kxw.jpg'],
                    ['繪師: @momozizizi-twitter',       'https://i.imgur.com/uyCku5o.jpg'],
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
            elif input_message == '空有無用知識的戀母情結小矮子':
                value_i = [
                    ['https://i.imgur.com/noYjwsL.jpg'],
                    ['繪師: RYUKI-pixiv',       'https://i.imgur.com/PJLI6TF.jpg'],
                    ['繪師: 理紅-pixiv',        'https://i.imgur.com/0Ai4zso.jpg']
                ]
                if len(value_i[i% len(value_i)])==2 :
                    line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
                elif len(value_i[i% len(value_i)])==1 :
                    line_bot_api.reply_message(event.reply_token,ImageMessageURL(value_i[i% len(value_i)][0]))
    ### 龍族巢穴 ###
    ### ドラゴンズネスト ###
    ### 龍族巢穴 ###
            elif input_message in ['龍族巢穴','ドラゴンズネスト']:
                value_i = [
                    ['繪師: やま兎-pixiv',     'https://i.imgur.com/ap4y30N.jpg'],
                    ['繪師: 関西ジン-pixiv',   'https://i.imgur.com/Y7UyJg8.jpg']
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
            elif input_message in ['帆稀','ホマレ']:
                value_i = [
                    ['繪師: 六丸いなみ-pixiv',     'https://i.imgur.com/hhtu7FX.jpg'],
                    ['繪師: 六丸いなみ-pixiv',     'https://i.imgur.com/ogQAyCh.jpg'],
                    ['繪師: うね-pixiv',          'https://i.imgur.com/IgoBITE.jpg']
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
            elif input_message in ['嘉夜','カヤ','鬼道嘉夜','卡雅','龍拳']:
                value_i = [
                    ['繪師: ヒーロー-pixiv',        'https://i.imgur.com/FWw5JLj.jpg'],
                    ['繪師: やま兎。-pixiv',        'https://i.imgur.com/HcDAD8a.jpg'],
                    ['繪師: しもん-pixiv',          'https://i.imgur.com/ZWhYldI.jpg'],
                    ['繪師: Miyamoya-pixiv',       'https://i.imgur.com/9I8paC4.jpg'],
                    ['繪師: @ryukisukune-twitter', 'https://i.imgur.com/Q1xLQgV.jpg'],
                    ['繪師: @cottonlife_c-twitter','https://i.imgur.com/nPB6qGl.jpg']
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
            elif input_message in ['祈梨','イノリ','一之瀨祈梨','祈','龍錘','龍槌']:
                value_i = [
                    ['繪師: こしあん-pixiv',        'https://i.imgur.com/5ZQ0r6b.jpg'],
                    ['繪師: 竹村コウ-pixiv',        'https://i.imgur.com/zU2H4Pf.jpg'],
                    ['繪師: ナナ稲-pixiv',          'https://i.imgur.com/wzT1Orh.jpg'],
                    ['繪師: 黒羽UMA-pixiv',         'https://i.imgur.com/F4sAEzZ.jpg'],
                    ['繪師: すなねこ-pixiv',        'https://i.imgur.com/qyZmeHC.jpg'],
                    ['繪師: こしあん-pixiv',        'https://i.imgur.com/Rrj5sTL.jpg',      'https://i.imgur.com/ukv934D.jpg'],
                    ['繪師: マルタ-pixiv',          'https://i.imgur.com/b0WjGwW.jpg'],
                    ['繪師: 浅りり介-pixiv',        'https://i.imgur.com/ej77ibg.jpg'],
                    ['繪師: @173_roku-twitter',    'https://i.imgur.com/puKOnGj.jpg'],
                    ['繪師: @sukeasa-twitter',     'https://i.imgur.com/0JKTvGW.jpg'],
                ]
                if(len(value_i[i% len(value_i)])==3):
                    line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1]),ImageMessageURL(value_i[i% len(value_i)][2])])
                elif(len(value_i[i% len(value_i)])==2):
                    line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
    ### 王宮騎士團 ###
    ### 騎士團 ###
    ### 王宮騎士団 ###
            elif input_message in ['王宮騎士團','騎士團','王宮騎士団']:
                value_i = [
                    ['繪師: 六丸いなみ-pixiv',    'https://i.imgur.com/0IVEQIG.jpg'],
                    ['繪師: 菖蒲-pixiv',         'https://i.imgur.com/lOPI6vv.jpg'],
                    ['繪師: @sub6o173-twitter',  'https://i.imgur.com/G7Z4cKZ.jpg'],
                    ['繪師: @SD_BigPie-twitter', 'https://i.imgur.com/arfgePJ.jpg']
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
            elif input_message in ['純','黑騎','ジュン','白銀純','黑Saber','泳裝純']:
                value_i = [
                    ['繪師: 六丸いなみ-pixiv',    'https://i.imgur.com/2U9tece.jpg'],
                    ['繪師: MoQi-pixiv',         'https://i.imgur.com/oVgUVJR.jpg'],
                    ['繪師: KMH-pixiv',          'https://i.imgur.com/IHKGTp6.jpg'],
                    ['繪師: Tahnya-pixiv',       'https://i.imgur.com/lQbq5uu.jpg'],
                    ['繪師: 六丸いなみ-pixiv',    'https://i.imgur.com/6sN2xaO.jpg'],
                    ['繪師: 六丸いなみ-pixiv',    'https://i.imgur.com/c0YaxWB.jpg'],
                    ['繪師: 六丸いなみ-pixiv',    'https://i.imgur.com/7sgNSyO.jpg'],
                    ['繪師: オウカ-pixiv',        'https://i.imgur.com/8lGFqFp.jpg'],
                    ['繪師: ともす-pixiv',        'https://i.imgur.com/rddL812.jpg'],
                    ['繪師: らま-pixiv',          'https://i.imgur.com/oxC5BAS.jpg'],
                    ['繪師: 六丸いなみ-pixiv',     'https://i.imgur.com/DtgMYm3.jpg'],
                    ['繪師: ダイアル-pixiv',       'https://i.imgur.com/qpV22M9.jpg'],
                    ['繪師: @sub6o173-twitter',   'https://i.imgur.com/E8QltWe.jpg'],
                    ['繪師: @sub6o173-twitter',   'https://i.imgur.com/xJTx9XS.jpg'],
                    ['繪師: 天雷-pixiv',          'https://i.imgur.com/e9Zsajf.jpg',   'https://i.imgur.com/uYd8OXO.jpg'],
                ]
                if(len(value_i[i% len(value_i)])==3):
                    line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1]),ImageMessageURL(value_i[i% len(value_i)][2])])
                elif(len(value_i[i% len(value_i)])==2):
                    line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
            elif input_message in ['智','トモ','御久間智','卜毛','禿毛','魔法少女智']:
                value_i = [
                    ['繪師: ゆんみ-pixiv',       'https://i.imgur.com/zT8PM2v.jpg'],
                    ['繪師: ゆんみ-pixiv',       'https://i.imgur.com/iG8OaxQ.jpg'],
                    ['繪師: 夏菜ゆさく-pixiv',    'https://i.imgur.com/qWEChhw.jpg'],
                    ['繪師: 六丸いなみ-pixiv',    'https://i.imgur.com/jQsBTjp.jpg'],
                    ['繪師: ゆんみ-pixiv',       'https://i.imgur.com/azqfXkv.jpg'],
                    ['繪師: ゆんみ-pixiv',       'https://i.imgur.com/4Gbgott.jpg'],
                    ['繪師: ゆんみ-pixiv',       'https://i.imgur.com/GPjyJMj.jpg'],
                    ['繪師: ゆんみ-pixiv',       'https://i.imgur.com/3nlfDvh.jpg'],
                    ['繪師: @sub6o173-twitter', 'https://i.imgur.com/3nlfDvh.jpg'],
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
            elif input_message in ['茉莉','マツリ' ,'織原茉莉','跳跳虎','萬聖茉莉']:
                value_i = [
                    ['繪師: @sub6o173-pixiv',          'https://i.imgur.com/KO1lfBx.jpg'],
                    ['繪師: ひとつのなか-pixiv',        'https://i.imgur.com/i04aggD.jpg'],
                    ['繪師: 夏菜ゆさく-pixiv',          'https://i.imgur.com/5TwMo5R.jpg'],
                    ['繪師: ゆんみ-pixiv',              'https://i.imgur.com/y6pVSXZ.jpg'],
                    ['繪師: ゆんみ-pixiv',              'https://i.imgur.com/x2pbDlA.jpg'],
                    ['繪師: 夏菜ゆさく-pixiv',          'https://i.imgur.com/rTZaTo9.jpg'],
                    ['繪師: @rokico_usagi-twitter',    'https://i.imgur.com/pxnf9P2.jpg'],
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
            elif input_message in ['團長','團長們','騎士團cp']:
                value_i = [
                    ['繪師: 六丸いなみ-pixiv',    'https://i.imgur.com/e2tRy2c.jpg'],
                    ['繪師: 六丸いなみ-pixiv',    'https://i.imgur.com/jasKCgm.jpg'],
                    ['繪師: 六丸いなみ-pixiv',    'https://i.imgur.com/vbQTnzp.jpg'],
                    ['繪師: 六丸いなみ-pixiv',    'https://i.imgur.com/cVpqbdB.jpg'],
                    ['繪師: 六丸いなみ-pixiv',    'https://i.imgur.com/tFRmHHC.jpg']
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
    ### 美食殿堂 ###
    ### 美食殿 ###
    ### 美食殿堂 ###
            elif input_message[:3] == '美食殿' and len(input_message)<=4:
                value_i = [
                    ['繪師: たなし-pixiv',         'https://i.imgur.com/VZtrbTV.jpg'],
                    ['繪師: 猫小渣-pixiv',         'https://i.imgur.com/4tz9vVW.jpg'],
                    ['繪師: 猫小渣-pixiv',         'https://i.imgur.com/AJNi0Qf.jpg'],
                    ['繪師: msh-pixiv',            'https://i.imgur.com/sVNvxwR.jpg'],
                    ['繪師: QuAn_-pixiv',          'https://i.imgur.com/iYY6otG.jpg'],
                    ['繪師: 高瀬コウ-pixiv',        'https://i.imgur.com/izcQ6oh.jpg'],
                    ['繪師: AJ-pixiv',             'https://i.imgur.com/aIbegIR.jpg'],
                    ['繪師: AJ-pixiv',             'https://i.imgur.com/te6hJJq.jpg'],
                    ['繪師: 昌未-pixiv',           'https://i.imgur.com/A2Qjk82.jpg'],
                    ['繪師: 昌未-pixiv',           'https://i.imgur.com/CfeEEU7.jpg'],
                    ['繪師: msh-pixiv',            'https://i.imgur.com/TBAZxPW.jpg'],
                    ['繪師: ZN (あえん)-pixiv',     'https://i.imgur.com/cGkummU.jpg'],
                    ['繪師: 結城辰也-pixiv',        'https://i.imgur.com/J4XbyXx.jpg'],
                    ['繪師: 夜凪朝妃-pixiv',        'https://i.imgur.com/8wxQ12m.jpg'],
                    ['繪師: とうち-pixiv',          'https://i.imgur.com/gzNmvkA.jpg'],
                    ['繪師: ジヤス-pixiv',          'https://i.imgur.com/kmwSilM.jpg'],
                    ['繪師: にしん-pixiv',          'https://i.imgur.com/Oy5rTFa.jpg'],
                    ['繪師: 室町アツシ-pixiv',      'https://i.imgur.com/hLw826c.jpg'],
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
            elif input_message in ['凱留','接頭霸王','考','黑貓','背骨貓','背骨','背刺貓','背刺','945','臭鼬','百地希留耶','希留耶','キャル' ,'945ml','正月凱留','泳裝凱留']:
                value_i = [
                    ['繪師: たてじまうり-pixiv',        'https://i.imgur.com/9DQ3S5y.jpg'],
                    ['繪師: 灰島-pixiv',               'https://i.imgur.com/HvYE6zv.jpg'],
                    ['繪師: じゅんまぁち。-pixiv',      'https://i.imgur.com/D2NySWD.jpg'],
                    ['繪師: けんぴゃっ-pixiv',          'https://i.imgur.com/ilub54I.jpg'],
                    ['繪師: みり-pixiv',               'https://i.imgur.com/YWmEuA8.jpg'],
                    ['繪師: @fang410693029-twitter',   'https://i.imgur.com/YWmEuA8.jpg'],
                    ['繪師: Je_M-pixiv',               'https://i.imgur.com/dACqudt.jpg'],
                    ['繪師: ごやいん-pixiv',            'https://i.imgur.com/FXZRaqL.jpg'],
                    ['繪師: @CeNanGam-twitter',        'https://i.imgur.com/k1hHShl.jpg'],
                    ['圖源: shadowverse',              'https://i.imgur.com/6EgNtoh.jpg'],
                    ['圖源: shadowverse',              'https://i.imgur.com/kO56BAY.jpg'],
                    ['圖源: shadowverse',              'https://i.imgur.com/h21rScV.jpg'],
                    ['繪師: ねこ鳴都(meito)-pixiv',     'https://i.imgur.com/O50QzvM.jpg'],
                    ['繪師: Panda-pixiv',              'https://i.imgur.com/TXyeTkc.jpg'],
                    ['繪師: puruding-pixiv',           'https://i.imgur.com/3V9s93C.jpg'],
                    ['繪師: @srm_chi-twitter',         'https://i.imgur.com/0RhbiiV.jpg'],
                    ['繪師: @brabrabrat00-twitter',    'https://i.imgur.com/BDIN5pz.jpg'],
                    ['繪師: @dosuo_9-twitter',         'https://i.imgur.com/fW1H4uT.jpg'],
                    ['繪師: たてじまうり-pixiv',        'https://i.imgur.com/la4ji05.jpg'],
                    ['繪師: hi-pixiv',                 'https://i.imgur.com/4qKWhUL.jpg'],
                    ['繪師: PoLa-pixiv',               'https://i.imgur.com/Dbukkg9.jpg'],
                    ['繪師: chocho10-pixiv',           'https://i.imgur.com/Gos21xK.jpg'],
                    ['繪師: ピアール-pixiv',            'https://i.imgur.com/oAz0AsN.jpg'],
                    ['繪師: 结夏祈-pixiv',              'https://i.imgur.com/HRVJRFa.jpg'],
                    ['繪師: かねた-pixiv',              'https://i.imgur.com/pPYrXUf.jpg'],
                    ['繪師: @yun_216-twitter',         'https://i.imgur.com/vQ7Pm6g.jpg'],
                ]
                if(len(value_i[i% len(value_i)])==2): 
                    line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
                else:
                    line_bot_api.reply_message(event.reply_token,ImageMessageURL(value_i[i% len(value_i)]))
            elif input_message in ['佩可','吃貨','大胃王','佩可莉姆','貪吃佩可','ペコリーヌ','公主','尤絲蒂亞娜·F·阿斯特萊亞','尤絲蒂亞娜','ヤバイですね','牙敗','公主佩可','泳裝佩可']:
                value_i = [
                    ['圖源: shadowverse',           "https://i.imgur.com/mtO06wN.jpg"],
                    ['繪師: @DokkoiMigu-twitter',   "https://i.imgur.com/SKsplQ6.jpg"],
                    ['繪師: @mato_kechi-twitter',   "https://i.imgur.com/YYwWhZi.jpg"],
                    ['繪師: ゆりりん-pixiv',         "https://i.imgur.com/i2MU9a7.jpg"],
                    ['繪師: osa-pixiv',             "https://i.imgur.com/GQ5106Q.jpg"],
                    ['繪師: イシノセ-pixiv',         "https://i.imgur.com/mm0qioK.jpg"],
                    ['繪師: イシノセ-pixiv',         "https://i.imgur.com/0Ne7tnn.jpg"],
                    ['繪師: 92M-pixiv',             "https://i.imgur.com/uoHcGkh.jpg"],
                    ['繪師: ゆゆ-pixiv',             "https://i.imgur.com/wPR4lyl.jpg"],
                    ['繪師: たてじまうり-pixiv',     "https://i.imgur.com/cafbX7D.jpg"],
                    ['繪師: ヒャング-pixiv',         "https://i.imgur.com/bDvRTJN.jpg"],
                    ['繪師: BNARI-pixiv',           "https://i.imgur.com/FCNIMbS.jpg"],
                    ['繪師: sonchi-pixiv',          "https://i.imgur.com/vXtXpZa.jpg"],
                    ['繪師: @goumudan-twitter',     "https://i.imgur.com/pjv3xkW.jpg"],
                    ['繪師: hi-pixiv',              "https://i.imgur.com/W3Ip8o5.jpg"],
                    ['繪師: しゅり-pixiv',           "https://i.imgur.com/PQwidGr.jpg"],
                    ['繪師: らんち-pixiv',           "https://i.imgur.com/Mjk5sJD.jpg"],
                    ['繪師: らんち-pixiv',           "https://i.imgur.com/auYAjnv.jpg"],
                    ['繪師: らんち-pixiv',           "https://i.imgur.com/wNqYUlJ.jpg"],
                    ['繪師: らんち-pixiv',           "https://i.imgur.com/iwhhRNk.jpg"],
                    ['繪師: @Tam_U-twitter',         "https://i.imgur.com/ixeP9uF.jpg"],
                    "https://i.imgur.com/zOWI57k.jpg",
                    "https://i.imgur.com/9DqK9ju.jpg",
                ]
                if(len(value_i[i% len(value_i)])==2): 
                    line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
                else:
                    line_bot_api.reply_message(event.reply_token,ImageMessageURL(value_i[i% len(value_i)]))
            elif input_message in ['可可蘿','可蘿','可口蘿','コッコロ','小小嚮導','媽媽','孝心','公主可可蘿','正月可可蘿','泳裝可可蘿','儀式服可可蘿']:
                value_i = [
                    ['https://i.imgur.com/Dbx8O8i.jpg'],
                    ['https://i.imgur.com/nR1ZxgM.jpg'],
                    ['https://i.imgur.com/6YoHLvJ.jpg'],
                    ['繪師: 骨カワ-pixiv',              'https://i.imgur.com/3y17m4w.jpg'],
                    ['繪師: アイダ-pixiv',              'https://i.imgur.com/6IQgnvV.jpg'],
                    ['繪師: 真崎ケイ-pixiv',            'https://i.imgur.com/CGDOWoL.jpg'],
                    ['繪師: @Alisia_0812-twitter',     'https://i.imgur.com/os1zhfw.jpg'],
                    ['繪師: アイダ-pixiv',             'https://i.imgur.com/vcjesG2.jpg'],
                    ['繪師: @osaillust-twitter',       'https://i.imgur.com/72AwIXj.jpg'],
                    ['繪師: @Re_hnk-twitter',          'https://i.imgur.com/Ti9PvVH.jpg'],
                    ['繪師: とも-pixiv',               'https://i.imgur.com/zsskgXH.jpg'],
                    ['繪師: Xeph-pixiv',               'https://i.imgur.com/uEysCSr.jpg'],
                    ['繪師: Xeph-pixiv',               'https://i.imgur.com/bP7r05H.jpg'],
                    ['繪師: sune-pixiv',               'https://i.imgur.com/MMBF02n.jpg'],
                    ['繪師: @SuperPig2046-twitter',    'https://i.imgur.com/K8lQzEO.jpg'],
                    ['繪師: Xeph-pixiv',               'https://i.imgur.com/hLFTFvc.jpg'],
                    ['繪師: @01masami13-twitter',      'https://i.imgur.com/2hzuSL0.jpg'],
                    ['繪師: GaaRa-pixiv',              'https://i.imgur.com/Lrwjo9d.jpg'],
                    ['繪師: @Xeph_Artworks-twitter',   'https://i.imgur.com/t8IthNS.jpg'],
                    ['繪師: @Xeph_Artworks-twitter',   'https://i.imgur.com/WJ1OZum.jpg'],
                    ['繪師: hi-pixiv',                 "https://i.imgur.com/4qKWhUL.jpg"],
                    ['繪師: Misekiss-pixiv',           "https://i.imgur.com/sOt6GMr.jpg"],
                    ['繪師: ZN (あえん)-pixiv',         "https://i.imgur.com/yASNYNQ.jpg"],
                    ['繪師: にゃふ-pixiv',              "https://i.imgur.com/U915HB4.jpg"],
                    ['繪師: ビーム-pixiv',              "https://i.imgur.com/yAphco3.jpg"],
                    ['繪師: あむりた様2号-pixiv',        "https://i.imgur.com/880TZEa.png"],
                    ['繪師: しゅり-pixiv',              "https://i.imgur.com/IXeCxBJ.png"],
                ]
                if(len(value_i[i% len(value_i)])==2): 
                    line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
                else:
                    line_bot_api.reply_message(event.reply_token,ImageMessageURL(value_i[i% len(value_i)][0]))
            elif input_message == '可哥蘿':
                value_i = [
                    TextSendMessage(text= '真是的 騎士君又惹哭可哥蘿了...(咦?'),
                    TextSendMessage(text= '可可萝同志乃我大美食殿堂\n不可分割之固有成员\n骑士君应充分理解和尊重\n美食殿堂的这一立场\n並立即正名"可可蘿"'),
                    ImageMessageURL('https://i.imgur.com/BYrzmF5.jpg'),
                    [TextSendMessage(text= '是可可蘿啦...(可可蘿哭倒路邊'),ImageMessageURL('https://i.imgur.com/gIF9vdY.png')],
                ]
                line_bot_api.reply_message(event.reply_token, value_i[i% len(value_i)])
                    
            elif input_message in ['主角','主人公','柚樹','佑樹','祐樹','騎士君','失智','ユウキ','變態的可疑分子','公主騎士','優衣最愛的']:
                value_i = [
                    ['圖源: shadowverse',               'https://i.imgur.com/dxwXlbZ.jpg'],
                    ['繪師: 千齋-pixiv',                'https://i.imgur.com/lhB9MYO.jpg'],
                    ['繪師: 木咕咕-pixiv',              'https://i.imgur.com/wgWBaOC.jpg'],
                    ['繪師: 飛翔的窩-巴哈',              'https://i.imgur.com/zIdOU5s.jpg'],
                    ['J̵̮́u̷̠͇̎ś̷̛̝̼t̵̜͍̓̑ ̸̪̱̍͝Y̶̦̓͠u̴͎͘i̶͎̕ ̸͕͕̽.̵̖̼͋͝.̸̰͊̔.̴̢̑',                   'https://i.imgur.com/0YenUwM.jpg'],
                    ['繪師: 夏嶋めも-pixiv',            'https://i.imgur.com/XEugdHH.jpg'],
                    ['繪師: 天雷-pixiv',                'https://i.imgur.com/w7jyWqm.jpg'],
                    ['繪師: @kotyamaru-twitter',        'https://i.imgur.com/w7jyWqm.jpg'],
                    ['繪師: @EN6cUMxx0rE6FFz-twitter',  'https://i.imgur.com/beISXnJ.jpg'],
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
            elif input_message in ['謝菲','シェフィ','雪菲','藍龍','冰龍']:
                value_i = [
                    ['繪師: アイダ-pixiv',          'https://i.imgur.com/zj4GQQF.jpg'],
                    ['繪師: こもこも-pixiv',        'https://i.imgur.com/3PUa0jt.jpg'],
                    ['繪師: やじ-pixiv',            'https://i.imgur.com/5UPjSbd.jpg'],
                    ['繪師: Miyamoya-pixiv',       'https://i.imgur.com/iPIVHH9.jpg'],
                    ['繪師: ゆずゆい-pixiv',        'https://i.imgur.com/X3fKJyS.jpg'],
                    ['繪師: やじ-pixiv',            'https://i.imgur.com/jXAa9vC.jpg'],
                    ['繪師: Miyamoya-pixiv',       'https://i.imgur.com/nEHTCm9.jpg'],
                    ['繪師: ゆずゆい-pixiv',        'https://i.imgur.com/R0dz7Fu.jpg'],
                    ['繪師: Kilua 키루아-pixiv',    'https://i.imgur.com/Pa2HvRB.jpg'],
                    ['繪師: いねま-pixiv',          'https://i.imgur.com/hYByARh.jpg'],
                    ['繪師: @YAZI114-twitter',      'https://i.imgur.com/DGYMAB7.jpg'],
                    ['繪師: Azel司令官-pixiv',      'https://i.imgur.com/mL98AKY.jpg'],
                    ['繪師: カッシュ-pixiv',        'https://i.imgur.com/eWPVmU4.jpg'],
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
            elif all(judger in input_message for judger in('孝心','變質')) and len(input_message)<10 :
                value_i = [
                    ['繪師: 92M-pixiv',            'https://i.imgur.com/GfAKT7y.jpg'],
                    ['繪師: 室町アツシ-pixiv',      'https://i.imgur.com/bhXnyCz.jpg'],
                    ['繪師: 弱電波-pixiv',          'https://i.imgur.com/IRN0gLf.jpg'],
                    'https://i.imgur.com/SaAleyw.jpg',
                    'https://i.imgur.com/BYrzmF5.jpg',
                ]
                if(len(value_i[i% len(value_i)])==2): 
                    line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
                else:
                    line_bot_api.reply_message(event.reply_token,ImageMessageURL(value_i[i% len(value_i)]))
    ### 憤怒軍團 ###
    ### レイジ・レギオン ###
    ### 憤怒•軍團 ###
            elif input_message in ['美空','ミソラ']:
                value_i = [
                    ['繪師: sonchi-pixiv',      'https://i.imgur.com/s5AExEM.jpg'],
                    ['繪師: カツラギ-pixiv',     'https://i.imgur.com/3NOjwK5.jpg'],
                    ['繪師: ぴてぃ-pixiv',       'https://i.imgur.com/4TWI8Ht.jpg'],
                    ['繪師: HIROKAZU-pixiv',    'https://i.imgur.com/jPLoOYo.jpg'],
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
    ### 七冠 ###
    ### 桂冠 ###
    ### 七冠 ###
            elif input_message in ['克莉絲提娜','克里斯蒂娜','クリスティーナ','克總','誓約女君','老太婆','副團長','阿姨','製作人','聖誕克莉絲提娜']:
                value_i = [
                    ['繪師: qwerty131154-巴哈',       'https://i.imgur.com/fjYRD4W.jpg'],
                    ['繪師: 双見ゆうき-pixiv',        'https://i.imgur.com/fY5YhrJ.jpg'],
                    ['繪師: ぽむり-pixiv',            'https://i.imgur.com/vhVVBlr.jpg'],
                    ['繪師: 淫傘うさぎ-pixiv',        'https://i.imgur.com/yqV2k5k.jpg'],
                    ['繪師: itaco-pixiv',            'https://i.imgur.com/99cwfub.jpg'],
                    ['繪師: Saha_-pixiv',            'https://i.imgur.com/QRyfHzd.jpg'],
                    ['繪師: しゅーくりいむ-pixiv',    'https://i.imgur.com/A6e9Nv6.jpg'],
                    ['繪師: Hanse-pixiv',            'https://i.imgur.com/tf6sNt6.jpg'],
                    ['繪師: sonchi-pixiv',           'https://i.imgur.com/aQNaclR.jpg'],
                    ['繪師: sonchi-pixiv',           'https://i.imgur.com/4rkG4kz.jpg']
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
            elif input_message in ['矛依未','青蛙','ムイミ','天樓霸斷劍','諾唯姆','姆咪','正月矛依未']:
                value_i = [
                    'https://i.imgur.com/CW1GCBv.jpg',
                    ['繪師: AJ-pixiv',         "https://i.imgur.com/Pgg0fqM.jpg"],
                    ['繪師: 塵-pixiv',         "https://i.imgur.com/QZMeUVh.jpg"],
                    ['繪師: 延ビ-pixiv',       "https://i.imgur.com/S6OSknV.jpg"],
                    ['繪師: Jehyun-pixiv',     "https://i.imgur.com/wZzXQMY.jpg"],
                    ['繪師: カッシュ-pixiv',   "https://i.imgur.com/5890KnY.jpg"],
                    ['繪師: 延ビ-pixiv',       "https://i.imgur.com/wH7RlxR.jpg"],
                    ['繪師: 延ビ-pixiv',       "https://i.imgur.com/P1AKT4r.jpg"],
                    ['繪師: ヒーロー-pixiv',   "https://i.imgur.com/2sAbiD5.jpg"],
                    ['繪師: ヒーロー-pixiv',   "https://i.imgur.com/jBrFpQr.jpg"],
                    ['繪師: 六丸いなみ-pixiv', "https://i.imgur.com/i1FJvTk.jpg"]
                ]
                if(len(value_i[i% len(value_i)])==2): 
                    line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
                else:
                    line_bot_api.reply_message(event.reply_token,ImageMessageURL(value_i[i% len(value_i)]))
            elif input_message in ['似似花','ネネカ','448','nnk','現士實似似花','變貌大妃','正月似似花']:
                value_i = [
                    ['繪師: 蛞蝓SLUG-pixiv',       "https://i.imgur.com/5SuITSA.jpg"],
                    ['繪師: うまるつふり-pixiv',    "https://i.imgur.com/aGDYsI3.jpg"],
                    ['繪師: ヒーロー-pixiv',       "https://i.imgur.com/yGsd9CX.jpg"],
                    ['繪師: Sw(すぅ)-pixiv',       "https://i.imgur.com/ZzUuYHz.jpg"],
                    ['繪師: 1ピコ㍍-pixiv',        "https://i.imgur.com/Xsi8DLf.jpg"],
                    ['繪師: AJ-pixiv',             "https://i.imgur.com/gcbOijd.jpg"],
                    ['繪師: Sw(すぅ)-pixiv',       "https://i.imgur.com/IWWXm2i.jpg"],
                    ['繪師: Sw(すぅ)-pixiv',       "https://i.imgur.com/JIvmhTS.jpg"],
                    ['繪師: 天雷-pixiv',           "https://i.imgur.com/jjsaSVF.jpg"],
                    ['繪師: Sw(すぅ)-pixiv',       "https://i.imgur.com/y0vPH6W.jpg"],
                    ['繪師: Sw(すぅ)-pixiv',       "https://i.imgur.com/rYx1j94.jpg"],
                    ['繪師: けんぴゃっ-pixiv',     "https://i.imgur.com/Gbt0uVO.jpg"]
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
            elif input_message in ['夥伴','伙伴','同伴','相棒','アイボウ','尾狗刀','尾刀狗']:
                value_i = [
                    ['繪師: 塵-pixiv',     "https://i.imgur.com/SneVdIU.jpg"],
                    ['繪師: 塵-pixiv',     "https://i.imgur.com/scnsgWD.jpg"],
                    ['繪師: 塵-pixiv',     "https://i.imgur.com/xMsa8U2.jpg"],
                    ['繪師: 塵-pixiv',     "https://i.imgur.com/I5Qk2cQ.jpg"],
                    ['繪師: 塵-pixiv',     "https://i.imgur.com/AUG6ynv.jpg"],
                    ['繪師: 塵-pixiv',     "https://i.imgur.com/L7I8aOS.jpg"],
                    ['繪師: 塵-pixiv',     "https://i.imgur.com/1StDQPw.jpg"],
                    ['繪師: 塵-pixiv',     "https://i.imgur.com/DRVw6os.jpg"],
                    ['繪師: 延ビ-pixiv',   "https://i.imgur.com/CMeG1rV.jpg"],
                    ['繪師: 延ビ-pixiv',   "https://i.imgur.com/zele47S.jpg"]
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
            elif input_message in ['拉比林斯達','ラビリスタ','模索路晶','晶','迷宮女王','迷路女王']:
                value_i = [
                    ['繪師: オスティ-pixiv',     "https://i.imgur.com/J69aauG.jpg"],
                    ['繪師: オスティ-pixiv',     "https://i.imgur.com/kHF3TOs.jpg"],
                    ['繪師: 谷川犬兎-pixiv',     "https://i.imgur.com/JqOwWXm.jpg"],
                    ['繪師: らる-pixiv',         "https://i.imgur.com/OF7HmOJ.jpg"],
                    ['遊戲繪圖',                 "https://i.imgur.com/9BfhchR.jpg"],
                    ['繪師: ヒーロー-pixiv',     "https://i.imgur.com/lkj81hl.jpg"],
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
            elif input_message == '桂冠':
                value_i = [
                    ImageMessageURL("https://i.imgur.com/5lRyLJy.png"),   
                    TextSendMessage(text ="騎士君是肚子餓了嗎？"),  
                    TextSendMessage(text ="桂冠你媽啦，就跟你說七冠了。\n-布丁")
                ]
                line_bot_api.reply_message(event.reply_token,value_i[i% len(value_i)])
    ### 馬納歷亞 ###
    ### マナリアフレンズ ###
    ### Manaria Friends ###
            elif input_message in ['馬納歷亞','マナリアフレンズ','Manaria Friends','百合公主']:
                value_i = [
                    ['繪師: 92M-pixiv',            'https://i.imgur.com/AtJOEqh.jpg'],
                    ['繪師: とも-pixiv',           'https://i.imgur.com/rqVMy0r.jpg'],
                    ['繪師: 音の绯-pixiv',         'https://i.imgur.com/OYbCg5i.jpg'],
                    ['繪師: ぽんず-pixiv',         'https://i.imgur.com/QARR8iO.jpg'],
                    ['繪師: れんず-pixiv',         'https://i.imgur.com/t9jLBeS.jpg'],
                    ['繪師: にゃー-pixiv',         'https://i.imgur.com/Dl0bf68.jpg'],
                    ['繪師: れっれれ-pixiv',       'https://i.imgur.com/pqQQ1ED.jpg'],
                    ['繪師: みどりのちゃ-pixiv',   'https://i.imgur.com/D6B3wSk.jpg'],
                    ['繪師: AJ-pixiv',            'https://i.imgur.com/JE5MeGW.jpg'],
                    ['繪師: いとね-pixiv',         'https://i.imgur.com/pz8dC3b.jpg']
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
            elif  input_message in ['古蕾雅','グレア','龍姬','古雷雅'] :
                value_i = [
                    ['繪師: KWS-pixiv',          'https://i.imgur.com/aatQVtQ.jpg'],
                    ['繪師: かんかっぴ-pixiv',    'https://i.imgur.com/jYom8yC.jpg'],
                    ['繪師: とも-pixiv',         'https://i.imgur.com/qxe6AtA.jpg'],
                    ['繪師: とも-pixiv',         'https://i.imgur.com/zvolEcL.jpg'],
                    ['繪師: とも-pixiv',         'https://i.imgur.com/7RuuWPm.jpg'],
                    ['繪師: いとね-pixiv',       'https://i.imgur.com/lhXOFCV.jpg'],
                    ['繪師: おもおもも-pixiv',   'https://i.imgur.com/HHuR7AU.jpg']
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
            elif input_message in ['安','アン','55kg','馬納歷亞公主','宏大魔法']:
                value_i = [
                    ['繪師: S.U.-pixiv',         'https://i.imgur.com/TYwLMpV.jpg'],
                    ['繪師: いとね-pixiv',        'https://i.imgur.com/SoSwfNW.jpg'],
                    ['繪師: HotaK-pixiv',        'https://i.imgur.com/sqexcv7.jpg'],
                    ['繪師: セラ-pixiv',         'https://i.imgur.com/pF3oHmc.jpg']
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
            elif input_message in ['露','ルゥ','眼球','補考','補考女帝']:
                value_i = [
                    ['繪師: ぺろんちょ-pixiv',      'https://i.imgur.com/WXCiwFo.jpg'],
                    ['繪師: AJ-pixiv',             'https://i.imgur.com/xcFCKju.jpg'],
                    ['繪師: りこ-pixiv',           'https://i.imgur.com/oFuxXbB.jpg'],
                    ['繪師: なかひま-pixiv',       'https://i.imgur.com/UMZ3jqU.jpg']
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
    ### Re:從零開始的異世界生活 ###
    ### Re:ゼロから始める異世界生活 ###
    ### Re:0 ###
            elif input_message in ['Re:從零開始的異世界生活','Re:ゼロから始める異世界生活','Re0','re0','Re:0','re:0']:
                value_i = [
                    ['繪師: ぽえ-pixiv',            'https://i.imgur.com/zEWwDWx.jpg'],
                    ['繪師: 桃乃きのこ。-pixiv',     'https://i.imgur.com/9sNkqru.jpg'],
                    ['繪師: ChinTora0201-pixiv',    'https://i.imgur.com/JXlERea.jpg'],
                    ['繪師: 喜欢夜宵yayoi-pixiv',    'https://i.imgur.com/RR4bXb2.jpg'],
                    ['繪師: ゆぞうに-pixiv',         'https://i.imgur.com/GlwcKnj.jpg'],
                    ['繪師: えらんと-pixiv',         'https://i.imgur.com/6dltMdz.jpg'],
                    ['繪師: だよ-pixiv',            'https://i.imgur.com/UamOLeJ.jpg'],
                    ['繪師: あろえ-pixiv',          'https://i.imgur.com/3zH6gy7.jpg'],
                    ['繪師: しゃけ沢-pixiv',        'https://i.imgur.com/6GAVLKt.jpg'],
                    ['繪師: しゃけ沢-pixiv',        'https://i.imgur.com/kkweao4.jpg']
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
            elif input_message in ['愛蜜莉雅','艾蜜莉雅','愛蜜莉亞','艾蜜莉亞','エミリア','EMT','emt','莉雅']:
                value_i = [
                    ['繪師: @Seic_Oh-pixiv',    'https://i.imgur.com/Il334iS.jpg'],
                    ['繪師: DABY-pixiv',        'https://i.imgur.com/slm7jSF.jpg'],
                    ['繪師: PiO-pixiv',         'https://i.imgur.com/mBDxyvy.jpg']
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
            elif input_message in ['雷姆','レム','快速動眼期']:
                value_i = [
                    ['繪師: そらほし-pixiv',        'https://i.imgur.com/hrYaNNk.jpg'],
                    ['繪師: DABY-pixiv',           'https://i.imgur.com/SqT0j7K.jpg'],
                    ['繪師: ttosom-pixiv',         'https://i.imgur.com/BTclhHL.jpg'],
                    ['繪師: MOMIN-pixiv',          'https://i.imgur.com/CUh9u9u.jpg'],
                    ['繪師: Bcoca-pixiv',          'https://i.imgur.com/Lhuqtbl.jpg'],
                    ['繪師: Melings-pixiv',        'https://i.imgur.com/MAbMNvB.jpg'],
                    ['繪師: 赤つき-pixiv',          'https://i.imgur.com/qwwmytW.jpg'],
                    ['繪師: ONSEM-pixiv',          'https://i.imgur.com/yxq7Q41.jpg'],
                    ['繪師: pangbai_666-pixiv',    'https://i.imgur.com/nSIZyms.jpg'],
                    ['繪師: 千羽茸みな-pixiv',      'https://i.imgur.com/W3i3XrP.jpg'],
                    ['繪師: はちろく-pixiv',        'https://i.imgur.com/BFjYGja.jpg']
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
            elif input_message in ['拉姆','ラム','記憶體','快取']:
                value_i = [
                    ['繪師: 千羽茸みな-pixiv',     'https://i.imgur.com/170L1AL.jpg'],
                    ['繪師: pigone-pixiv',        'https://i.imgur.com/vCtXAgN.jpg'],
                    ['繪師: MOMIN-pixiv',         'https://i.imgur.com/NABfw4w.jpg'],
                    ['繪師: Suo-pixiv',           'https://i.imgur.com/lco0h8A.jpg'],
                    ['繪師: G.YA-pixiv',          'https://i.imgur.com/G1pGidw.jpg'],
                    ['繪師: mongble-pixiv',       'https://i.imgur.com/yDjYb2W.jpg'],
                    ['繪師: 100wang-pixiv',       'https://i.imgur.com/1V0lN5M.jpg'],
                    ['繪師: ゆぞうに-pixiv',       'https://i.imgur.com/swAQL8v.jpg']
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
            elif input_message in ['碧翠絲','ベアトリス','貝蒂','碧翠子']:
                value_i = [
                    ['繪師: だよ-pixiv',               'https://i.imgur.com/nGQILuC.jpg'],
                    ['繪師: KeG-pixiv',                'https://i.imgur.com/scWOIZi.jpg'],
                    ['繪師: tonowa トノワ-pixiv',      'https://i.imgur.com/0C9ZjXh.jpg'],
                    ['繪師: しゃけ沢-pixiv',           'https://i.imgur.com/rm7jCFZ.jpg'],
                    ['繪師: きんぎん-pixiv',           'https://i.imgur.com/uLWLBqp.jpg'],
                    ['繪師: そらほし-pixiv',           'https://i.imgur.com/0Xqn2Kj.jpg']
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
    ### 偶像大師灰姑娘女孩 ###
    ### アイドルマスターシンデレラガールズ ###
    ### New Generation ###
            elif input_message in ['偶像大師灰姑娘女孩','アイドルマスターシンデレラガールズ','偶大','偶像大師','灰姑娘','新世代','New Generation','new generation']:
                value_i = [
                    ['繪師: シワスタカシ-pixiv',    'https://i.imgur.com/WZMIbDm.jpg'],
                    ['繪師: Blue_Gk-pixiv',        'https://i.imgur.com/oEwb94k.jpg'],
                    ['繪師: nyanya-pixiv',         'https://i.imgur.com/2T86ioj.jpg'],
                    ['繪師: 森倉円-pixiv',          'https://i.imgur.com/V701qlH.jpg'],
                    ['繪師: 森倉円-pixiv',          'https://i.imgur.com/Tttl70z.jpg'],
                    ['繪師: 森倉円-pixiv',          'https://i.imgur.com/pdpPweS.jpg'],
                    ['繪師: 月神るな-pixiv',        'https://i.imgur.com/7ha5BHr.jpg'],
                    ['繪師: @001_Tashia-twitter',   'https://i.imgur.com/sg9Q98D.jpg'],
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
            elif input_message in ['凜','渋谷凛','澀谷凜','蒼之劍士']:
                value_i = [
                    ['繪師: たまかが-pixiv',           'https://i.imgur.com/IHb3Fpq.jpg'],
                    ['繪師: たまかが-pixiv',           'https://i.imgur.com/dEOc4B9.jpg'],
                    ['繪師: たまかが-pixiv',           'https://i.imgur.com/Pn8rJg6.jpg'],
                    ['繪師: すとろα-pixiv',            'https://i.imgur.com/rpLWgZ0.jpg'],
                    ['繪師: たまかが-pixiv',           'https://i.imgur.com/RYqtKt4.jpg'],
                    ['繪師: Appplepie/AP-pixiv',      'https://i.imgur.com/T3XJO0P.jpg'],
                    ['繪師: 遊びに来た人・ｖ・-pixiv',  'https://i.imgur.com/eFryXdz.jpg']
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
            elif input_message in ['卯月','ウヅキ','島村卯月','笑容狂魔','笑容狂魔卯月']:
                value_i = [
                    ['我爸摳爸twitter: @cloba377',     'https://i.imgur.com/LJei46w.jpg'],
                    ['繪師: うらび-pixiv',             'https://i.imgur.com/dUdTGQb.jpg'],
                    ['繪師: 荻pote-pixiv',             'https://i.imgur.com/mm8Yo4p.jpg'],
                    ['繪師: 結城辰也-pixiv',           'https://i.imgur.com/UyrBq7f.jpg'],
                    ['繪師: U35(うみこ)-pixiv',        'https://i.imgur.com/sgquvvJ.jpg'],
                    ['繪師: 芹野いつき-pixiv',         'https://i.imgur.com/tV1mcRw.jpg'],
                    ['繪師: 芹野いつき-pixiv',         'https://i.imgur.com/Y5qeCti.jpg']
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
            elif input_message in ['未央','ミオ','本田未央','醬未央']:
                value_i = [
                    ['繪師: なかむら-pixiv',       'https://i.imgur.com/c7AyD0I.png'],
                    ['繪師: なかむら-pixiv',       'https://i.imgur.com/PSDg4hg.png'],
                    ['繪師: なかむら-pixiv',       'https://i.imgur.com/ytEi5Ch.png'],
                    ['繪師: なかむら-pixiv',       'https://i.imgur.com/oLYkBFq.png'],
                    ['繪師: なかむら-pixiv',       'https://i.imgur.com/3LVm262.png'],
                    ['繪師: なかむら-pixiv',       'https://i.imgur.com/OMM2Nnw.png'],
                    ['繪師: なかむら-pixiv',       'https://i.imgur.com/u5b5jeY.png'],
                    ['繪師: なかむら-pixiv',       'https://i.imgur.com/2NmYR4H.png'],
                    ['繪師: なかむら-pixiv',       'https://i.imgur.com/5kjaeRP.png'],
                    ['繪師: なかむら-pixiv',       'https://i.imgur.com/pjAWB3t.png'],
                    ['繪師: なかむら-pixiv',       'https://i.imgur.com/dcciHxb.png'],
                    ['繪師: なかむら-pixiv',       'https://i.imgur.com/JFsM3G9.png'],
                    ['繪師: なかむら-pixiv',       'https://i.imgur.com/8P5x7yP.png'],
                    ['繪師: なかむら-pixiv',       'https://i.imgur.com/wBYo85z.png'],
                    ['繪師: なかむら-pixiv',       'https://i.imgur.com/MXQ211f.png']
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
    ### 角色 (其他) ###
    ### 角色 (其他) ###
    ### 角色 (其他) ###
            elif input_message in ['吉塔','ジータ','姬塔','騎空士','團長','古戰場逃兵','古戰場','吉他']:
                value_i = [
                    ['繪師: sirohito-pixiv',       'https://i.imgur.com/JQVl13u.jpg'],
                    ['繪師: sirohito-pixiv',       'https://i.imgur.com/Koj0uLM.jpg'],
                    ['繪師: iro-pixiv',            'https://i.imgur.com/H7HCIAP.jpg'],
                    ['繪師: たく庵-pixiv',          'https://i.imgur.com/A2aEn1l.jpg'],
                    ['繪師: iro-pixiv',            'https://i.imgur.com/JbYRjt3.jpg'],
                    ['繪師: まぐ-pixiv',           'https://i.imgur.com/6ZfdF8m.jpg'],
                    ['繪師: とうふぷりん-pixiv',    'https://i.imgur.com/oG0b6Hi.jpg'],
                    ['繪師: みり㍑-pixiv',          'https://i.imgur.com/UCIL06b.jpg'],
                    ['繪師: 葉千はちみつ-pixiv',    'https://i.imgur.com/usc7BWI.jpg']
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
            elif input_message in ['露娜','ルナ','露那','死靈法師','好朋友']: 
                value_i = [
                    ['繪師: Enji-pixiv',          'https://i.imgur.com/ob9Uw8y.jpg'],
                    ['繪師: により-pixiv',         'https://i.imgur.com/HgbgckH.jpg'],
                    ['繪師: HIROKAZU-pixiv',      'https://i.imgur.com/igqmOgB.jpg'],
                    ['繪師: ちてたん-pixiv',       'https://i.imgur.com/SCP6xRn.jpg'],
                    ['繪師: により-pixiv',         'https://i.imgur.com/amVcMiq.jpg'],
                    ['繪師: 小山内-pixiv',         'https://i.imgur.com/BrEu6Vm.jpg'],
                    ['繪師: shoonia-pixiv',       'https://i.imgur.com/oAjAmEe.jpg'],
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
            elif input_message in ['亞里莎','アリサ','亞里瞎','瞎子','羅莎莉亞']: 
                value_i = [
                    ['繪師: 黒井ススム-pixiv',       'https://i.imgur.com/BCu2qYG.jpg'],
                    ['繪師: ヨシノリョウ-pixiv',     'https://i.imgur.com/7NwXZJ2.jpg'],
                    ['繪師: 士雷 Shirai-pixiv',     'https://i.imgur.com/QvQRCLn.jpg'],
                    ['繪師: kieed-pixiv',           'https://i.imgur.com/anYIkmH.jpg'],
                    ['繪師: きち-pixiv',            'https://i.imgur.com/crxmOPm.jpg'],
                    ['繪師: きち-pixiv',            'https://i.imgur.com/FNVMMbH.jpg'],
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
            elif input_message in ['愛梅斯','DD頭子','アメス','艾梅斯']:
                value_i = [
                    ['繪師: aono-pixiv',           'https://i.imgur.com/yk8dzMD.jpg','https://i.imgur.com/uc1XcEF.jpg','https://i.imgur.com/uKWemDs.jpg'],
                    ['繪師: aono-pixiv',           'https://i.imgur.com/hurT0Sk.jpg'],
                    ['繪師: aono-pixiv',           'https://i.imgur.com/9wfDIYY.jpg'],
                    ['繪師: aono-pixiv',           'https://i.imgur.com/M6WlrdB.jpg'],
                    ['繪師: いすとーん-pixiv',      'https://i.imgur.com/VnQ0cPI.jpg'],
                    ['繪師: つちのトン-pixiv',      'https://i.imgur.com/lzKdQtU.jpg'],
                    ['繪師: うまるつふり-pixiv',    'https://i.imgur.com/LKRmGhU.jpg'],
                    ['繪師: みず-pixiv',           'https://i.imgur.com/v2grm1E.jpg'],
                    ['繪師: 結月わらび-pixiv',      'https://i.imgur.com/1VERUPY.jpg'],
                    ['繪師: Sira-pixiv',           'https://i.imgur.com/NMi24Ix.jpg'],
                    ['繪師: aono-pixiv',           'https://i.imgur.com/WG2qVcL.jpg'],
                    ['繪師: ヒーロー-pixiv',        'https://i.imgur.com/xSmm7wk.jpg'],
                ]
                if(len(value_i[i% len(value_i)])==4): 
                    line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1]),ImageMessageURL(value_i[i% len(value_i)][2]),ImageMessageURL(value_i[i% len(value_i)][3])])
                else:
                    line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
            elif input_message in ['對決','決戰','終戰','對峙']:
                value_i = [
                    ['繪師: 天雷-pixiv',                   'https://i.imgur.com/2wM6Fv3.jpg'],
                    ['繪師: KMH-pixiv',                    'https://i.imgur.com/d95pPjB.jpg'],
                    ['繪師: こしあん（たいやき）-pixiv',     'https://i.imgur.com/tuIdVA5.jpg'],
                    ['繪師: ウラズラ-pixiv',                'https://i.imgur.com/mse3aq4.jpg'],
                    ['繪師: @cluseller-twitter',           'https://i.imgur.com/Gzac88E.jpg'],
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
            elif input_message in ['姊妹','姐妹','雙子']:
                value_i = [
                    ['繪師: みず-pixiv',           'https://i.imgur.com/ul5x7d4.jpg'],
                    ['繪師: 結城辰也-pixiv',       'https://i.imgur.com/UtkMYdI.jpg'],
                    ['繪師: ヤンタロウ-pixiv',     'https://i.imgur.com/QaAUaca.jpg'],
                    ['繪師: Chel-pixiv',          'https://i.imgur.com/vy9LI9P.jpg'],
                    ['繪師: ぬるぷよ-pixiv',       'https://i.imgur.com/WH0niD2.jpg'],
                    ['繪師: ゆりりん-pixiv',       'https://i.imgur.com/vuueBKE.jpg'],
                    ['繪師: はちろく-pixiv',       'https://i.imgur.com/BFjYGja.jpg'],
                    ['繪師: pigone-pixiv',        'https://i.imgur.com/vCtXAgN.jpg'],
                    ['繪師: ユキタカ-pixiv',       'https://i.imgur.com/iQVOxk2.jpg'],
                    ['繪師: みどりのちゃ-pixiv',   'https://i.imgur.com/2wbKiAy.jpg'],
                    ['繪師: 秋月リア-pixiv',       'https://i.imgur.com/NRgmRRj.jpg'],
                    ['繪師: RYUKI-pixiv',         'https://i.imgur.com/cTrVg8W.jpg'],
                    ['繪師: cha_chya-pixiv',      'https://i.imgur.com/nle89D8.jpg'],
                    ['繪師: @PK_PKP_PPK-twitter', 'https://i.imgur.com/Dg1bV2v.jpg'],
                    ['繪師: GaaRa-pixiv',         'https://i.imgur.com/npB3vE4.jpg'],
                    ['繪師: しもん-pixiv',         'https://i.imgur.com/vXay9QY.jpg'],
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
            elif input_message in ['魔法少女','馬猴燒酒']:
                value_i = [
                    ['繪師: けんぴゃっ-pixiv',       'https://i.imgur.com/SrlAcry.jpg'],
                    ['繪師: ぐっち庵-pixiv',         'https://i.imgur.com/DiJZGaI.jpg'],
                    ['繪師: AJ-pixiv',              'https://i.imgur.com/QQec9OS.jpg'],
                    ['繪師: 夜凪朝妃-pixiv',         'https://i.imgur.com/GU3Pdtk.jpg'],
                    ['繪師: @mk1122maki-twitter',   'https://i.imgur.com/BeCNUl3.png'],
                    ['繪師: @uranakahima-twitter',  'https://i.imgur.com/zRr1s25.png'],
                    ['繪師: @o_kita915-twitter',    'https://i.imgur.com/o6Mo3d1.png']
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
            elif input_message in ['公主連結','プリコネ','超異域公主連結','公連']:
                value_i = [
                    ['繪師: Lab2-pixiv',       'https://i.imgur.com/YBfyJ36.jpg'],
                    ['繪師: 菖蒲-pixiv',       'https://i.imgur.com/Ljgi7Of.jpg'],
                    ['繪師: 結城辰也-pixiv',   'https://iㄛmgur.com/FXAP2EI.jpg'],
                    ['繪師: 冷蝉-pixiv',       'https://i.imgur.com/S07PioH.jpg'],
                    ['繪師: みどりのちゃ-pixiv','https://i.imgur.com/jkxQSzY.jpg'],
                    ['繪師: みどりのちゃ-pixiv','https://i.imgur.com/UNjZhIs.jpg']
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
        
#其他角色 (非公連登場，存私心)

    ### 碧藍航線 ###
    ### アズールレーン ###
    ### 碧池航線 ###
            elif input_message in ['碧藍航線','アズールレーン','碧池航線']: 
                value_i = [
                    ['繪師: 清里-pixiv',                   'https://i.imgur.com/hONfsMX.jpg'],
                    ['繪師: 玲汰-pixiv',                   'https://i.imgur.com/Pl0P8pK.jpg'],
                    ['繪師: 月満懐空-pixiv',               'https://i.imgur.com/3uZlrvV.jpg'],
                    ['繪師: かぷりちお-pixiv',             'https://i.imgur.com/LU16tpQ.jpg'],
                    ['繪師: @umaiyo_puyoman-twitter',     'https://i.imgur.com/XPKkF7W.jpg']
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
            elif input_message in ['標槍','Javelin','ジャベリン']: 
                value_i = [
                    ['繪師: 紅薙ようと-pixiv',     'https://i.imgur.com/PzKzQCC.jpg'],
                    ['繪師: もうぴい-pixiv',       'https://i.imgur.com/ryUR0N6.jpg'],
                    ['繪師: もうぴい-pixiv',       'https://i.imgur.com/NTmk4IM.jpg'],
                    ['繪師: もうぴい-pixiv',       'https://i.imgur.com/2WxKEDr.jpg'],
                    ['繪師: もうぴい-pixiv',       'https://i.imgur.com/J7o6Htn.jpg'],
                    ['繪師: もうぴい-pixiv',       'https://i.imgur.com/SekN4bL.jpg'],
                    ['繪師: うなっち-pixiv',       'https://i.imgur.com/IO1nx2t.jpg'],
                    ['繪師: まだら-pixiv',         'https://i.imgur.com/Q506e62.jpg'],
                    ['繪師: ちょこころね-pixiv',   'https://i.imgur.com/mJEnaOq.jpg']
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
            elif input_message in ['拉菲','ラフィー','紅酒']: 
                value_i = [
                    ['繪師: TouTou-pixiv',       'https://i.imgur.com/6xrpW1X.jpg'],
                    ['繪師: 月うさぎ-pixiv',      'https://i.imgur.com/peTAQvV.jpg'],
                    ['繪師: まとけち-pixiv',      'https://i.imgur.com/8tHVklt.jpg'],
                    ['繪師: ぽしー-pixiv',        'https://i.imgur.com/tjy0KC3.jpg'],
                    ['繪師: らむち-pixiv',        'https://i.imgur.com/VRFASyP.jpg'],
                    ['繪師: 月うさぎ-pixiv',      'https://i.imgur.com/MB6IDtx.jpg'],
                    ['繪師: 自律金属-pixiv',      'https://i.imgur.com/b7LXyZb.jpg']
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
            elif input_message in ['綾波','アヤナミ','鬼神']: 
                value_i = [
                    ['繪師: rika_39-pixiv',        'https://i.imgur.com/2vNqHVP.jpg'],
                    ['繪師: Kana-pixiv',           'https://i.imgur.com/0I2TKgh.jpg'],
                    ['繪師: 清里-pixiv',            'https://i.imgur.com/bD8S8tB.jpg'],
                    ['繪師: いずもねる-pixiv',      'https://i.imgur.com/cG12rKK.jpg'],
                    ['繪師: シロノーラ-pixiv',      'https://i.imgur.com/Js1wIYn.jpg'],
                    ['繪師: narae-pixiv',          'https://i.imgur.com/udUKVLC.jpg']
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
            elif input_message in ['獨角獸','ユニコーン'] or (input_message[:2] == '港獨' and len(input_message)<6): 
                value_i = [
                    ['繪師: 浅ノ川-pixiv',      'https://i.imgur.com/zXNIMWm.jpg'],
                    ['繪師: Kinty-pixiv',       'https://i.imgur.com/fnpwjNA.jpg'],
                    ['繪師: 松うに-pixiv',      'https://i.imgur.com/ahxeS2g.jpg'],
                    ['繪師: マトリ-pixiv',      'https://i.imgur.com/TQcJlUj.jpg'],
                    ['繪師: 繭咲悠-pixiv',      'https://i.imgur.com/rhsNP4Y.jpg'],
                    ['繪師: 小枝-pixiv',        'https://i.imgur.com/xmQ7dEq.jpg'],
                    ['繪師: ちた-pixiv',        'https://i.imgur.com/KKfImwN.jpg']
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
    ### 心跳文學部 ###
    ### Doki Doki Literature Club! ###
    ### 心跳文學部 ###
            elif input_message in ['心跳文學部','DokiDoki','Doki Doki','dokidoki','doki doki Literature Club']: 
                value_i = [
                    ['繪師: TakuyaRawr-pixiv',   'https://i.imgur.com/rWqmHxA.jpg'],
                    ['繪師: klaeia-pixiv',       'https://i.imgur.com/UJglYyJ.jpg'],
                    ['繪師: 抠肉肚脐-pixiv',      'https://i.imgur.com/fK3p6OV.jpg'],
                    ['繪師: Satchel-pixiv',      'https://i.imgur.com/dJjVUnG.jpg'],
                    ['繪師: Satchely-pixiv',     'https://i.imgur.com/0J8OgFZ.jpg'],
                    ['繪師: luke-pixiv',         'https://i.imgur.com/k4ed73c.jpg']
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
        #just monika在公連莫妮卡那裏
            elif input_message in ['Natsuki','natsuki','夏樹']: 
                value_i = [
                    ['繪師: ...-pixiv',        'https://i.imgur.com/EhPgot9.jpg'],
                    ['繪師: ...-pixiv',        'https://i.imgur.com/sc21Wqx.jpg'],
                    ['繪師: hews-pixiv',       'https://i.imgur.com/pGYMKN8.jpg'],
                    ['繪師: humannose-pixiv',  'https://i.imgur.com/3FDfpNP.jpg'],
                    ['繪師: 麦飴 アンプ-pixiv', 'https://i.imgur.com/p1LbfSp.jpg'],
                    ['繪師: 麦飴 アンプ-pixiv', 'https://i.imgur.com/eC6XM1P.jpg'],
                    ['繪師: 麦飴 アンプ-pixiv', 'https://i.imgur.com/TMHdhdp.jpg'],
                    ['繪師: TheCold-pixiv',    'https://i.imgur.com/zRvEhvz.jpg']
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
            elif input_message in ['Sayori','sayori','紗世里']: 
                value_i = [
                    ['繪師: 麦飴 アンプ-pixiv',    'https://i.imgur.com/o3sJfRw.jpg'],
                    ['繪師: えりまき-pixiv',       'https://i.imgur.com/0bsE4c2.jpg'],
                    ['繪師: 麦飴 アンプ-pixiv',    'https://i.imgur.com/5jokre2.jpg'],
                    ['繪師: 麦飴 アンプ-pixiv',    'https://i.imgur.com/nQG7CGd.jpg'],
                    ['繪師: 麦飴 アンプ-pixiv',    'https://i.imgur.com/JBANcKk.jpg'],
                    ['繪師: 麦飴 アンプ-pixiv',    'https://i.imgur.com/cQqohkT.jpg']
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
            elif input_message in ['Yuri','yuri','優里']: 
                value_i = [
                    ['繪師: 麦飴 アンプ-pixiv',     'https://i.imgur.com/s1D2PHe.jpg'],
                    ['繪師: 麦飴 アンプ-pixiv',     'https://i.imgur.com/PseJ4gQ.jpg'],
                    ['繪師: 麦飴 アンプ-pixiv',     'https://i.imgur.com/MLVfysj.jpg'],
                    ['繪師: 十田-pixiv',           'https://i.imgur.com/zvKKnsN.jpg'],
                    ['繪師: hazu_t-pixiv',         'https://i.imgur.com/ME4mq0l.jpg'],
                    ['繪師: hazu_t-pixiv',         'https://i.imgur.com/rZGZHxi.jpg'],
                    ['繪師: 綾城大福-pixiv',        'https://i.imgur.com/vN1tbaC.jpg']
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
    ### 點兔 ###
    ### 請問您今天要來點兔子嗎？ ###
    ### ご注文はうさぎですか？ ###
            elif input_message in ['智乃','香風智乃','點兔','チノ']:
                value_i = [
                    ['繪師: Hitsu-pixiv',                     'https://i.imgur.com/NocwYLL.jpg'],
                    ['智乃香風 is not fuck your Waifu ok?',   'https://i.imgur.com/2ciqFyu.jpg'],
                    ['繪師: 真崎ケイ-pixiv',                   'https://i.imgur.com/XLEXScW.jpg'],
                    ['繪師: 真崎ケイ-pixiv',                   'https://i.imgur.com/Re8GFIS.jpg'],
                    ['繪師: かにビーム-pixiv',                 'https://i.imgur.com/DIMIze8.jpg'],
                    ['繪師: かにビーム-pixiv',                 'https://i.imgur.com/ZqmBXrD.jpg'],
                    ['繪師: かにビーム-pixiv',                 'https://i.imgur.com/Dxysvop.jpg'],
                    [ImageMessageURL('https://i.imgur.com/lINQsqA.jpg')],
                    [ImageMessageURL('https://i.imgur.com/ZjvdEr7.jpg')],   
                    [ImageMessageURL('https://i.imgur.com/x6y3KiT.jpg')],    
                    [Chino_H(
                        'https://i.imgur.com/wT28YYw.jpg',
                        'https://i.imgur.com/8BXeAO7.jpg',
                        'https://i.imgur.com/iZqYbd5.jpg',
                        'https://i.imgur.com/WXUitOs.jpg',
                        'https://i.imgur.com/mqKucrg.jpg',
                        'https://i.imgur.com/oa5rPGp.jpg',
                        'https://i.imgur.com/Fthdiox.jpg',
                        'https://i.imgur.com/QTyEwNd.jpg',
                        'https://i.imgur.com/kxrFnvP.jpg',
                        'https://i.imgur.com/plfXJWD.jpg',
                        'https://www.pixiv.net/artworks/73074675')],   
                    [Chino_H(
                        'https://i.imgur.com/46S4XEm.jpg',
                        'https://i.imgur.com/q91hXfv.jpg',
                        'https://i.imgur.com/lMtUojt.jpg',
                        'https://i.imgur.com/gQmFzsA.jpg',
                        'https://i.imgur.com/zvSzHkF.jpg',
                        'https://i.imgur.com/IbvF511.jpg',
                        'https://i.imgur.com/fhMZcGb.jpg',
                        'https://i.imgur.com/dIMdlFH.jpg',
                        'https://i.imgur.com/QxKwmfO.jpg',
                        'https://i.imgur.com/kWuE6Oh.jpg',
                        'https://www.pixiv.net/artworks/62564661')]
                ]
                if len (value_i[i% len(value_i)]) == 2:
                    line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
                elif len (value_i[i% len(value_i)]) == 1 :
                    line_bot_api.reply_message(event.reply_token,value_i[i% len(value_i)][0])
    ### 魔女之旅 ###
    ### 魔女の旅々 ###
    ### 魔女之旅 ###
            elif input_message in ['魔女之旅','魔女の旅々','伊蕾娜','灰之魔女','イレイナ']: 
                value_i = [
                    ['繪師: あずーる-pixiv',     'https://i.imgur.com/zj50nOb.png'],
                    ['繪師: あずーる-pixiv',     'https://i.imgur.com/zySbemA.png'],
                    ['繪師: あずーる-pixiv',     'https://i.imgur.com/WjvrOT4.png'],
                    ['繪師: あずーる-pixiv',     'https://i.imgur.com/OJ8oidK.png'],
                    ['繪師: あずーる-pixiv',     'https://i.imgur.com/CTN6KHK.png'],
                    ['繪師: あずーる-pixiv',     'https://i.imgur.com/Ptuv0Zg.png'],
                    ['繪師: あずーる-pixiv',     'https://i.imgur.com/K9qGpDJ.png'],
                    ['繪師: あずーる-pixiv',     'https://i.imgur.com/zAeGR3t.png'],
                    ['繪師: あずーる-pixiv',     'https://i.imgur.com/pLHyvB3.png'],
                    ['繪師: あずーる-pixiv',     'https://i.imgur.com/4Za8yu0.png'],
                    ['繪師: あずーる-pixiv',     'https://i.imgur.com/vQTXwOd.png'],
                    ['繪師: あずーる-pixiv',     'https://i.imgur.com/QHJZllu.png'],
                    ['繪師: あずーる-pixiv',     'https://i.imgur.com/hUb5ma4.png'],
                    ['繪師: あずーる-pixiv',     'https://i.imgur.com/UqnJjDp.png'],
                    ['繪師: あずーる-pixiv',     'https://i.imgur.com/T1tBpjN.png'],
                    ['繪師: あずーる-pixiv',     'https://i.imgur.com/K9l0bKR.png'],
                    ['繪師: あずーる-pixiv',     'https://i.imgur.com/6OZgCtC.png'],
                    ['繪師: あずーる-pixiv',     'https://i.imgur.com/Z5uYfoe.png'],
                    ['繪師: あずーる-pixiv',     'https://i.imgur.com/sEwHzYz.png'],
                    ['繪師: あずーる-pixiv',     'https://i.imgur.com/L4z2TbT.png'],
                    ['繪師: あずーる-pixiv',     'https://i.imgur.com/CLLOTSd.png'],
                    ['繪師: あずーる-pixiv',     'https://i.imgur.com/Fn5Z0O7.png'],
                    ['繪師: あずーる-pixiv',     'https://i.imgur.com/ugC8Mio.png'],
                    ['繪師: あずーる-pixiv',     'https://i.imgur.com/oyzn7pd.png'],
                    ['繪師: あずーる-pixiv',     'https://i.imgur.com/C7Bblx7.png'],
                    ['繪師: あずーる-pixiv',     'https://i.imgur.com/nduBfsd.png'],
                    ['繪師: あずーる-pixiv',     'https://i.imgur.com/9HJKFOg.png'],
                    ['繪師: あずーる-pixiv',     'https://i.imgur.com/0SmnQxB.png'],
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
    ### 原神 ###
    ### 抄襲偷個資 ###
    ### パイモン ###
            elif input_message in ['派蒙','原神','パイモン','應急食品','抄襲遊戲']: 
                value_i = [
                    ['繪師: Lunacle-pixiv',     'https://i.imgur.com/sJihIID.png'],
                    ['繪師: kyktsu-pixiv',      'https://i.imgur.com/5bvSvPx.png'],
                    ['繪師: あろえ-pixiv',       'https://i.imgur.com/jtep5MQ.png'],
                    ['繪師: Kabedon-pixiv',     'https://i.imgur.com/oK3qBRl.png'],
                    ['繪師: ユウ100-pixiv',      'https://i.imgur.com/Bm50cT7.png'],
                    ['繪師: 黎羽田共-pixiv',     'https://i.imgur.com/huFlDbP.png'],
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
    ### VTuber ###
    ### VTuber ###
    ### VTuber ###
            elif input_message in ['gura','Gura','GURA','鯊鯊','サメちゃん','グラ','古拉']: 
                value_i = [
                    ['繪師: nikitjke6996-pixiv',   'https://i.imgur.com/ITVPtDb.png'],
                    ['繪師: レモきち-pixiv',        'https://i.imgur.com/Dr11XvZ.png'],
                    ['繪師: あさの-pixiv',          'https://i.imgur.com/9yIuFcU.png'],
                    ['繪師: Ancy-pixiv',            'https://i.imgur.com/pd76nZS.png'],
                    ['繪師: 毛玉丸-pixiv',          'https://i.imgur.com/68F1l9O.png'],
                    ['繪師: Rayleigh Scale-pixiv',  'https://i.imgur.com/9yxOI77.png'],
                    ['繪師: Ancy-pixiv',            'https://i.imgur.com/iFAkraA.png'],
                    ['繪師: Zodirat-pixiv',         'https://i.imgur.com/EZBvqoC.png'],
                    ['繪師: BANGOSU-pixiv',         'https://i.imgur.com/SqQ5ZMi.png'],
                    ['繪師: BANGOSU-pixiv',         'https://i.imgur.com/LkPtHdk.png'],
                    ['繪師: PoNya-pixiv',           'https://i.imgur.com/uDtm3YP.png'],
                    ['繪師: @444renga-twitter',     'https://i.imgur.com/yRhigNY.png'],
                    ['繪師: Beryl-pixiv',           'https://i.imgur.com/dHXUueg.png'],
                    ['繪師: さなだケイスイ-pixiv',   'https://i.imgur.com/HTYaMr0.png'],
                    ['繪師: あううぃ-pixiv',         'https://i.imgur.com/ioHC4OJ.png'],
                    ['繪師: @fuyouchu-twitter',     'https://i.imgur.com/4oG2DB3.png'],
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
            elif input_message in ['Amelia','Ame','ame','AME','watson','Watson','華生']: 
                value_i = [
                    ['繪師: なび-pixiv',            'https://i.imgur.com/Tcb7P0D.png'],
                    ['繪師: Hyde-pixiv',            'https://i.imgur.com/BaONXVf.png'],
                    ['繪師: トカエミレオン-pixiv',   'https://i.imgur.com/hOJdlHY.png'],
                    ['繪師: なび-pixiv',            'https://i.imgur.com/Tcb7P0D.png'],
                    ['繪師: Hyde-pixiv',            'https://i.imgur.com/BaONXVf.png'],
                    ['繪師: トカエミレオン-pixiv',   'https://i.imgur.com/hOJdlHY.png'],
                    ['繪師: DannyKoo-pixiv',        'https://i.imgur.com/sBYTHhp.png'],
                    ['繪師: でじ-pixiv',            'https://i.imgur.com/sBYTHhp.png'],
                    ['繪師: BANGOSU-pixiv',         'https://i.imgur.com/UjnNSKh.png'],
                    ['繪師: 椎奈碧-pixiv',          'https://i.imgur.com/jy1Q9qp.png'],
                    ['繪師: PoLa-pixiv',            'https://i.imgur.com/kGmJGIy.png'],
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
            elif input_message in ['華鯊','華鯊公約']: 
                value_i = [
                    ['繪師: 二重白-pixiv',              'https://i.imgur.com/dsLXwui.png'],
                    ['繪師: Ancy-pixiv',                'https://i.imgur.com/koL3UZr.png'],
                    ['繪師: @nevblindarts-twitter',     'https://i.imgur.com/rptCS7T.png'],
                    ['繪師: @yakksan_-twitter',         'https://i.imgur.com/DOh55RR.png'],
                    ['繪師: @XsvLdktgkxnDiP0-twitter',  'https://i.imgur.com/yFOvEpA.png'],
                    ['繪師: @XsvLdktgkxnDiP0-twitter',  'https://i.imgur.com/ndUZudy.png'],
                    ['繪師: Xeph＇s Artworks-pixiv',    'https://i.imgur.com/qPulQf4.png'],
                    ['繪師: @Klaius-twitter',           'https://i.imgur.com/8ysrrgy.png'],
                    ['繪師: Beryl-pixiv',               'https://i.imgur.com/aVcXrOP.png'],
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
            elif input_message in ['Ina','ina',"Ina'nis"]: 
                value_i = [
                    ['繪師: 月と犬-pixiv',            'https://i.imgur.com/G9D5ovw.png'],
                    ['繪師: もれの-pixiv',            'https://i.imgur.com/LIlHJaM.png'],
                    ['繪師: PoNya-pixiv',            'https://i.imgur.com/YjSBOD8.png'],
                    ['繪師: sa-pixiv',               'https://i.imgur.com/I7gZ2RO.png'],
                    ['繪師: コナ-pixiv',             'https://i.imgur.com/UFEcqhH.png'],
                    ['繪師: anon-pixiv',             'https://i.imgur.com/dYvQzRW.png'],
                    ['繪師: @ninomaeinanis-twitter', 'https://i.imgur.com/7Z6l44v.png'],
                    ['繪師: @kelly_dog_cat-twitter', 'https://i.imgur.com/mYLxadc.png'],
                    ['繪師: @STOMACH168-twitter',    'https://i.imgur.com/pYw6nJ5.png'],
                    'https://i.imgur.com/5EGJjYE.png',
                ]
                if(len(value_i[i% len(value_i)])==2): 
                    line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
                else:
                    line_bot_api.reply_message(event.reply_token,ImageMessageURL(value_i[i% len(value_i)]))
            elif input_message in ['潤羽るしあ','るしあ','Rushia','rushia','潤羽露西婭','露西婭','初號機']: 
                value_i = [
                    ['繪師: やすゆき-pixiv',         'https://i.imgur.com/OZrornO.png'],
                    ['繪師: やすゆき-pixiv',         'https://i.imgur.com/jRjmbfr.png'],
                    ['繪師: Rosuuri-pixiv',         'https://i.imgur.com/G5gkBBc.png'],
                    ['繪師: むらさめしん-pixiv',     'https://i.imgur.com/PZhgKej.png'],
                    ['繪師: sune-pixiv',            'https://i.imgur.com/iCTDeMD.png'],
                    ['繪師: Rosuuri-pixiv',         'https://i.imgur.com/4J60hRu.png'],
                    ['繪師: とと-pixiv',            'https://i.imgur.com/TlZ1nw6.png'],
                    ['繪師: やすゆき-pixiv',        'https://i.imgur.com/5Mg82Uh.png'],
                    ['繪師: としぞう-pixiv',        'https://i.imgur.com/0fGKTA0.png'],
                    ['繪師: としぞう-pixiv',        'https://i.imgur.com/RrJKAih.png'],
                    ['繪師: としぞう-pixiv',        'https://i.imgur.com/QNOVO2Q.png'],
                    ['繪師: としぞう-pixiv',        'https://i.imgur.com/utCQbta.png'],
                    ['繪師: Guchico-pixiv',        'https://i.imgur.com/teOSiPw.png'],
                    ['繪師: @half_rice024-twitter','https://i.imgur.com/qcyXlX7.png'],
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
            elif input_message in ['百鬼あやめ','あやめ','百鬼綾目']: 
                value_i = [
                    ['繪師: としぞう-pixiv',          'https://i.imgur.com/ccdb23Y.png'],
                    ['繪師: 兎ipoi-pixiv',            'https://i.imgur.com/zTtRmXF.png'],
                    ['繪師: 楠ハルイ-pixiv',           'https://i.imgur.com/WLgsHlf.png'],
                    ['繪師: 三登 いつき-pixiv',        'https://i.imgur.com/d9kLd3j.png'],
                    ['繪師: らっち。-pixiv',          'https://i.imgur.com/W0UAYWV.png'],
                    ['繪師: 太もも-pixiv',            'https://i.imgur.com/PK9lRNq.png'],
                    ['繪師: ごれ-pixiv',              'https://i.imgur.com/JbWR1aU.png'],
                    ['繪師: にんにくましまし-pixiv',   'https://i.imgur.com/8BhWsuO.png'],
                    ['繪師: あううぃ-pixiv',          'https://i.imgur.com/WaVf29h.png'],
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
            elif input_message in ['湊あくあ','あくあ','aqua','Aqua','湊阿庫婭']: 
                value_i = [
                    ['繪師: がおう-pixiv',          'https://i.imgur.com/DMc2T8v.png'],
                    ['繪師: がおう-pixiv',          'https://i.imgur.com/m6UbxfP.png'],
                    ['繪師: がおう-pixiv',          'https://i.imgur.com/hhjrCgq.png'],
                    ['繪師: がおう-pixiv',          'https://i.imgur.com/tAVBci2.png'],
                    ['繪師: あかもく-pixiv',        'https://i.imgur.com/P1zE7zQ.png'],
                    ['繪師: Taht-pixiv',           'https://i.imgur.com/0Pah9fL.png'],
                    ['繪師: imi/ロカ-pixiv',        'https://i.imgur.com/eSyxHji.png'],
                    ['繪師: がおう-pixiv',          'https://i.imgur.com/1oQNmSW.png'],
                    ['繪師: がおう-pixiv',          'https://i.imgur.com/Y8uPFDB.png'],
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
            elif input_message in ['兎田ぺこら','ぺこら','兔田佩克拉','兔田佩可拉']: 
                value_i = [
                    ['繪師: nibosi-pixiv',            'https://i.imgur.com/9Dpb087.png'],
                    ['繪師: 干物A太-pixiv',           'https://i.imgur.com/kH78fOn.png'],
                    ['繪師: としぞう-pixiv',          'https://i.imgur.com/w3OtWk9.png'],
                    ['繪師: ねむん-pixiv',            'https://i.imgur.com/PwBFxf1.png'],
                    ['繪師: ゆーりか-pixiv',          'https://i.imgur.com/azoAZ4r.png'],
                    ['繪師: トモセシュンサク-pixiv',   'https://i.imgur.com/9L5IF5G.png'],
                    ['繪師: あううぃ-pixiv',          'https://i.imgur.com/biRyByn.png'],
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
            elif input_message in ['常闇トワ','トワ','TMT','常闇永遠']: 
                value_i = [
                    ['繪師: さなだケイスイ-pixiv',      'https://i.imgur.com/n1AGYPN.png'],
                    ['繪師: かんざきひろ-pixiv',        'https://i.imgur.com/k9WDkOL.png'],
                    ['繪師: Mr.Lime-pixiv',            'https://i.imgur.com/lS6UZW2.png'],
                    ['繪師: 兎ipoi-pixiv',             'https://i.imgur.com/GJ27W8G.png'],
                    ['繪師: Mr.Lime-pixiv',            'https://i.imgur.com/cLsjuw4.png'],
                    ['繪師: 兎ipoi-pixiv',             'https://i.imgur.com/vgciNKq.png'],
                    ['繪師: Mr.Lime-pixiv',            'https://i.imgur.com/J2VddAo.png'],
                    ['繪師: 北乃ゆきと-pixiv',          'https://i.imgur.com/5FcARmy.png'],
                    ['繪師: Mr.Lime-pixiv',            'https://i.imgur.com/3ZUTLVp.png'],
                    ['繪師: Mr.Lime-pixiv',            'https://i.imgur.com/guT1I72.png'],
                    ['繪師: Mr.Lime-pixiv',            'https://i.imgur.com/qDIlRwf.png'],
                    ['繪師: Mr.Lime-pixiv',            'https://i.imgur.com/wLkOibI.png'],
                    ['繪師: Mr.Lime-pixiv',            'https://i.imgur.com/pZgSvng.png'],
                    ['繪師: Mr.Lime-pixiv',            'https://i.imgur.com/1KA3Xm1.png'],
                    ['繪師: Mr.Lime-pixiv',            'https://i.imgur.com/AlcCbZg.png'],
                    ['繪師: Mr.Lime-pixiv',            'https://i.imgur.com/YIEHEUA.png'],
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
            elif input_message in ['雪花ラミィ','ラミィ','雪花菈米','菈米']: 
                value_i = [
                    ['繪師: リン☆ユウ-pixiv',            'https://i.imgur.com/CZt2KbL.png'],
                    ['繪師: リン☆ユウ-pixiv',            'https://i.imgur.com/PVx1Tnt.png'],
                    ['繪師: リン☆ユウ-pixiv',            'https://i.imgur.com/DD58P5C.png'],
                    ['繪師: リン☆ユウ-pixiv',            'https://i.imgur.com/j2bptr2.png'],
                    ['繪師: リン☆ユウ-pixiv',            'https://i.imgur.com/HcYjgU4.png'],
                    ['繪師: リン☆ユウ-pixiv',            'https://i.imgur.com/8aVD3Pr.png'],
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
            elif input_message in ['天使うと']: 
                value_i = [
                    ['繪師: PoLa-pixiv',            'https://i.imgur.com/mjEglnX.png'],
                    ['繪師: なび-pixiv',            'https://i.imgur.com/vuJ92XH.png'],
                    ['繪師: ｍｅｍｅｎｏ-pixiv',     'https://i.imgur.com/M1d1xYb.png'],
                ]
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)][0]),ImageMessageURL(value_i[i% len(value_i)][1])])
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        if self.access==-1 or self.access==1:
            if input_message[0] in 'Nn' and input_message[1] in '1234567890' and len(input_message) <= 7 :
                num =''.join([x for x in input_message if x.isdigit()])
                if eval(num)==0 and len(num)==1:
                    num = str(random.randint(185000,350000))
                elif((eval(num)) in [228922,173156,196970,323914,306333]) :
                    value_i = [
                        "等等...騎士君，別告訴我你是認真的",
                        "吶吶，這方面的還是不要的好吧...",
                        "就算是這樣的騎士君，優衣還是喜歡的呦",
                        "切嚕~\nちぇるちぇる、ちぇちぇるぱ、ちぇるるるん！\nちぇらるれ、ちぇらちぇら、ちぇるちぇぽぱぴ？",
                        "危",
                        "https://i.imgur.com/vRqJCMJ.jpg",
                        'https://i.imgur.com/BYrzmF5.jpg',
                    ]
                    if("imgur" in value_i[i% len(value_i)]) :
                        line_bot_api.reply_message(event.reply_token,ImageMessageURL(value_i[i% len(value_i)]))
                        return
                    else:
                        line_bot_api.reply_message(event.reply_token,TextSendMessage(text = value_i[i% len(value_i)]))
                        return
                if(i%20==0):
                    value_i = [
                        "騎士君不行呦~你已經有優衣了",
                        "騎士君~整天尻雞雞不行呦，這次先不要了吧",
                        "哼哼~原來騎士君喜歡這種的，這次先沒收了 (生氣氣"
                    ]
                    line_bot_api.reply_message(event.reply_token,TextSendMessage(text = value_i[i% len(value_i)]))
                    return
                else:
                    try:
                        value_i = [
                            "口黑口黑(ﾟ∀ﾟ)",
                            "老濕姬請點這",
                            "大☆爆☆射！！！",
                            "n網車車點我！",
                            "發車嘍！！"
                        ]
                        line_bot_api.reply_message(event.reply_token,getData_N(value_i[i% len(value_i)],num,event))
                    except:
                        value_i = [
                            "騎士君，人家找不到這本本",
                            "人家翻了好幾次都沒看到騎士君想要的本本耶，再從新輸入一次吧",
                            "隨機的功能不會驗證車車是否確實存在哦",
                            "這本車車介於有跟沒有之間，再檢查一次有沒有輸入錯誤呦",
                        ]
                        line_bot_api.reply_message(event.reply_token,TextSendMessage(text = '騎士君想要的車號：n'+num+'\n'+ value_i[i% len(value_i)], quick_reply = QuickClick_Res_Hentai (event)))

            elif input_message[0] in 'Ww' and input_message[1] in '1234567890' and len(input_message) <= 7 :
                num =''.join([x for x in input_message if x.isdigit()])
                if eval(num)==0 and len(num)==1:
                    num = str(random.randint(40000,120000))
                elif((eval(num)) in [31475,44854]):
                    value_i = [
                        "等等...騎士君，別告訴我你是認真的",
                        "吶吶，這方面的還是不要的好吧...",
                        "就算是這樣的騎士君，優依還是喜歡的呦",
                        "切嚕~\nちぇるちぇる、ちぇちぇるぱ、ちぇるるるん！\nちぇらるれ、ちぇらちぇら、ちぇるちぇぽぱぴ？",
                        "危",
                        "https://i.imgur.com/vRqJCMJ.jpg",
                        'https://i.imgur.com/BYrzmF5.jpg',
                    ]
                    if("imgur" in value_i[i% len(value_i)]) :
                        line_bot_api.reply_message(event.reply_token,ImageMessageURL(value_i[i% len(value_i)]))
                        return
                    else:
                        line_bot_api.reply_message(event.reply_token,TextSendMessage(text = value_i[i% len(value_i)]))
                        return
                if(i%20==0):
                    value_i = [
                        "騎士君不行呦~你已經有優衣了",
                        "騎士君~整天尻雞雞不行呦，這次先不要了吧",
                        "哼哼~原來騎士君喜歡這種的，這次先沒收了 (生氣氣"
                    ]
                    line_bot_api.reply_message(event.reply_token,TextSendMessage(text = value_i[i% len(value_i)]))
                    return
                else:
                    try:
                        value_i = [
                            "口黑口黑(ﾟ∀ﾟ)",
                            "老濕姬請點這",
                            "大☆爆☆射！！！",
                            "w網車車點我！",
                            "發車嘍！！"
                        ]
                        line_bot_api.reply_message(event.reply_token,getData_W(value_i[i% len(value_i)],num,event))
                    except:
                        value_i = [
                            "騎士君，人家找不到這本本",
                            "人家翻了好幾次都沒看到騎士君想要的本本耶，再從新輸入一次吧",
                            "隨機的功能不會驗證車車是否確實存在哦",
                            "這本車車介於有跟沒有之間，再檢查一次有沒有輸入錯誤呦",
                        ]
                        line_bot_api.reply_message(event.reply_token,TextSendMessage(text = '騎士君想要的車號：w'+num+'\n'+ value_i[i% len(value_i)], quick_reply = QuickClick_Res_Hentai (event)))

            elif input_message[:2] == '18' and input_message[2] in 'cC' and input_message[3] in '1234567890' and len(input_message)<=9: 
                num = input_message[3:]
                if eval(num)==0 and len(num)==1:
                    if(i%3==0):
                        num = str(random.randint(10000,235000))
                    else:
                        num = str(random.randint(150000,235000))
                elif(num in [9487,5487]):
                    value_i = [
                        "等等...騎士君，別告訴我你是認真的",
                        "吶吶，這方面的還是不要的好吧...",
                        "就算是這樣的騎士君，優依還是喜歡的呦",
                        "切嚕~\nちぇるちぇる、ちぇちぇるぱ、ちぇるるるん！\nちぇらるれ、ちぇらちぇら、ちぇるちぇぽぱぴ？",
                        "危",
                        "https://i.imgur.com/vRqJCMJ.jpg",
                        'https://i.imgur.com/BYrzmF5.jpg',
                    ]
                    if("imgur" in value_i[i% len(value_i)]) :
                        line_bot_api.reply_message(event.reply_token,ImageMessageURL(value_i[i% len(value_i)]))
                        return
                    else:
                        line_bot_api.reply_message(event.reply_token,TextSendMessage(text = value_i[i% len(value_i)]))
                        return
                if(i%20==0):
                    value_i = [
                        "騎士君不行呦~你已經有優衣了",
                        "騎士君~整天尻雞雞不行呦，這次先不要了吧",
                        "哼哼~原來騎士君喜歡這種的，這次先沒收了 (生氣氣"
                    ]
                    line_bot_api.reply_message(event.reply_token,TextSendMessage(text = value_i[i% len(value_i)]))
                    return
                else:
                    try:
                        value_i = [
                            "口黑口黑(ﾟ∀ﾟ)",
                            "老濕姬請點這",
                            "大☆爆☆射！！！",
                            "18c站車車點我！",
                            "發車嘍！！"
                        ]
                        line_bot_api.reply_message(event.reply_token,getData_18C(value_i[i% len(value_i)],num,event))
                    except:
                        value_i = [
                            "騎士君，人家找不到這本本",
                            "人家翻了好幾次都沒看到騎士君想要的本本耶，再從新輸入一次吧",
                            "隨機的功能不會驗證車車是否確實存在哦",
                            "這本車車介於有跟沒有之間，再檢查一次有沒有輸入錯誤呦",
                        ]
                        line_bot_api.reply_message(event.reply_token,TextSendMessage(text = '騎士君想要的車號：18c '+num+'\n'+ value_i[i% len(value_i)], quick_reply = QuickClick_Res_Hentai (event)))

            elif (input_message[:2] == 'ex' or input_message[:2] == 'e-') and input_message[2] in '1234567890': 
                line_bot_api.reply_message(event.reply_token,ImageMessageURL("https://i.imgur.com/DhE6XcZ.jpg"))
            
            elif(event.source.type != 'group' and input_message[0]!='#' and event.source.user_id not in Globals.Yui_denied_group):
                if('早' in input_message and len(input_message)<6):
                    print(self.localhour)
                    if(self.localhour>=6 and self.localhour<12):
                        value_i = [
                            "早啊騎士君",
                            "欸?!騎士君一大早就來找我了啊?!",
                            "おはよう！騎士君",
                            "おはようございます！",
                            "早啊，騎士君（今天依舊只注視著你喔）",
                            "早安啊，新的一天又開始了~",
                            "騎士君很有朝氣呢!!",
                            "騎士君早上好\n呵呵……騎士君睡迷糊的樣子真可愛呢，好像小寶寶一樣。",
                        ]
                        line_bot_api.reply_message(event.reply_token,TextSendMessage(text = value_i[i% len(value_i)]))
                    elif(self.localhour>=12 and self.localhour<18):
                        value_i = [
                            "呃...騎士君現在才說早安的嗎?",
                            "這有點晚了哦",
                            "騎士君~要說午安呦不是早安",
                            "有點晚了不過沒關係！"
                        ]
                        line_bot_api.reply_message(event.reply_token,TextSendMessage(text = value_i[i% len(value_i)]))
                    else:
                        value_i = [
                            "不對不對!現在已經晚上了哦",
                            "這真的有點晚了哦",
                            "咦？都日落了耶，要人家放一發日出魔法嗎？",
                            "現在是晚安了哦!",
                            "商店已經開始打烊了哦!",
                            "咦！已經晚上了\n騎士君現在才起床的嗎?!",
                            "人家等了你一整天到晚上，結果你跟我說早安",
                        ]
                        line_bot_api.reply_message(event.reply_token,TextSendMessage(text = value_i[i% len(value_i)]))
                elif('午' in input_message and len(input_message)<6):
                    if(self.localhour>=6 and self.localhour<12):
                        value_i = [
                            "騎士君...中午還沒到哦",
                            "離中午還有"+str(12-self.localhour)+"個小時哦",
                            "現在應該要說的是早安呦~",
                            "騎士君睡糊塗了嗎？還沒中午哦"
                        ]
                        line_bot_api.reply_message(event.reply_token,TextSendMessage(text = value_i[i% len(value_i)]))
                    elif(self.localhour>=12 and self.localhour<18):
                        value_i = [
                            "一起來吃午餐吧！騎士君~~",
                            "咦咦，你說你已經吃過學姊的便當了嗎?!",
                            "午安！騎士君",
                            "午餐，如果、如果騎士君不介意的話...能一起吃嗎？"
                        ]
                        line_bot_api.reply_message(event.reply_token,TextSendMessage(text = value_i[i% len(value_i)]))
                    else:
                        value_i = [
                            "不對不對!現在已經晚上了哦",
                            "現在應該要說晚安哦！",
                            "咦？都日落了耶，要人家放一發日出魔法嗎？",
                            "商店已經開始打烊了哦!"
                        ]
                        line_bot_api.reply_message(event.reply_token,TextSendMessage(text = value_i[i% len(value_i)]))
                elif('晚' in input_message and len(input_message)<6):
                    if(self.localhour>=6 and self.localhour<12):
                        value_i = [
                            "欸欸?!睡迷糊了嗎？",
                            "已經早上了，該說早安哦",
                            "已經一大早了哦~~\n騎士君還想要睡覺嗎？\n好吧...這次就讓你躺我的膝...沒有啦",
                            "是昨天晚上都在跟可可蘿玩嗎？已經早上了哦",
                            "已經早上了哦~騎士君",
                        ]
                        line_bot_api.reply_message(event.reply_token,TextSendMessage(text = value_i[i% len(value_i)]))
                    elif(self.localhour>=12 and self.localhour<18):
                        value_i = [
                            "呃...晚安還有點太早了",
                            "咦?!現在不是才下午而已嗎",
                            "晚上還沒到來哦 騎士君"
                        ]
                        line_bot_api.reply_message(event.reply_token,TextSendMessage(text = value_i[i% len(value_i)]))
                    else:
                        value_i = [
                            "晚安，騎士君 (嘻嘻嘻)",
                            "嗯，明天應該也是充滿希望的一天",
                            "今天我也可以到騎士君的公會小屋找佩可他們開睡衣趴嗎？",
                            "嘻嘻，蘭德索爾的夜景很美呢",
                            "有騎士君在，總覺得今天晚上的夜空會特別美呢！",
                            "外頭正下著流星雨，一起來許願吧 (希望能和騎士君....",
                        ]
                        line_bot_api.reply_message(event.reply_token,TextSendMessage(text = value_i[i% len(value_i)]))
                elif('好' in input_message and len(input_message)<3 and '不' not in input_message ):
                    value_i = [
                        "嗯，一起來吧",
                        "嘻嘻///",
                        "嗯，說好了哦",
                        "哈哈",
                        "恩恩，謝謝你騎士君"
                    ]
                    line_bot_api.reply_message(event.reply_token,TextSendMessage(text = value_i[i% len(value_i)]))
                elif('哈' in input_message and len(input_message)<3 and '笑' in input_message ):
                    value_i = [
                        "咦...\n人家說了什麼好笑的嗎？",
                        "嘻嘻///",
                        "呣~~有什麼好笑的",
                        "哈哈"
                    ]
                    line_bot_api.reply_message(event.reply_token,TextSendMessage(text = value_i[i% len(value_i)]))
                elif input_message in ["優衣我愛你","我愛你優衣","我愛你","我喜歡你","我愛優衣"]:
                    value_i = [
                        "嘻嘻 好開心~",
                        "嗯\n要永遠陪在優衣的身邊哦~",
                        "哇啊啊~\n騎士君這麼突然的嗎...不過，還是很開心///",
                        "嗯~~♡\n人家也是哦",
                        "咦欸 人家還沒準備好，怎麼辦怎麼辦，頭髮還有些亂，也沒有特別打扮過......騎士君，等我一下，絕對要等我哦///",
                        "嗯~這是騎士君對我的承諾，優衣一定會守護好這份羈絆"
                    ]
                    line_bot_api.reply_message(event.reply_token,TextSendMessage(text=value_i[i% len(value_i)]))
                else:
                    value_i = [
                        "怎麼了嗎?騎士君",
                        "哼哼~~！\n騎士君怎麼突然出現了///",
                        "不知道可可蘿這時候在做什麼呢？",
                        "哇哦！嚇了一跳",
                        "真開心，騎士君來找我了",
                        "(❁´◡`❁)",
                        "騎士君難道真的很閒嗎？",
                        "神奇真步魔法靈~~~\n學姊餓死還不行~~~\n優衣優衣騎士君~~~",
                        "今天到珍禽...真琴學姊打工的店一起吃小餅乾，把學姊要給騎士君的那份都吃光了",
                        "窗外今天天氣怎麼樣呢，人家這邊的天氣還是一樣好呢，就像是不會變似的。",
                        "騎士君今天還是一樣帥氣呢～～",
                        "不管外面有多少女孩子，騎士君的眼中也只有我吧，當然人家也是喔～",
                        "騎士君，你知道我真的真的很愛你\n不管你變成什麼樣子\n就算是變成屍體也一樣喔\n不過活著的騎士君還是比較好\n對吧騎～～士～～君～～",
                        "霞學妹嗎？為什麼她那時候不穿裙子？",
                        "霞就算是學妹也不能原諒呢",
                        "霞學妹真的髒死了",
                        "誰是日和？",
                        "傷害優衣的傢伙在哪？\n人家都處理掉了哦~~",
                        "明明是人家先來的...",
                        "粉紅切開都是純白的",
                        "人家只是為了清理不該存在的錯誤\n魔王什麼的...",
                        "守護好蘭德索爾的人民~\n我可以的",
                        "騎士君的溫暖\n騎士君的善良\n賦予了我向前的動力",
                        "不用擔心的，因為騎士君一直在我們身邊",
                        "就算失去了幾百次回憶，我相信騎士君都會陪伴著我向前",
                        "我的魔法有幫上忙嗎...",
                        "你能一直待在我的身邊嗎",
                        "騎士君騎士君~花朵都盛開著呢！",
                        "拜託你，騎士君，請你以後也給予我勇氣...\n為了能變得更強、更溫柔",
                        "欸?!\n人家只是一個變態紳士作者意識底下的優衣機器人吶",
                        "想和騎士君一直一直在一起。\n誒……？\n騎士君剛剛的話聽見了嗎？\n哇啊啊－－！請忘記剛剛的事……",
                        "只有心意可不行...",
                        "咦？為什麼要說對不起？？沒有人做過對不起人家的事啊，對啊沒有人...",
                        "嗯...\n我哪裡都不會去的喔\n我會一直和騎士君旁邊喔~~",
                        "騎士君是只要一下定決心要去幫助誰，就直到最後都不會退讓的人呢",
                    ]
                    line_bot_api.reply_message(event.reply_token,TextSendMessage(text = value_i[i% len(value_i)]))