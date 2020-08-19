#============================================================
from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *
import random
#============================================================
from FlexMessage import *
from Animation import *
from Res_Hentai import *
from Capsule import *
#============================================================
# Channel Access Token
line_bot_api = LineBotApi('PpZXtWUOfOocv4On1fWAHOFUZEdJu6WNW/XPDBbppZ3/573sZ/eyvlfZ1KP3t29JhHzzF4JgzaD1IIfrdKVWV6ocNbhBi5O4Qy5Cqpy+NHmBwYs0uZlVwiyW5bdgJPUGh4ZQG8bD6vhaSMVhjQsedAdB04t89/1O/w1cDnyilFU=')
# testbot
#line_bot_api = LineBotApi('NSZjNpSJhMXhy6WMtt6246iOUKAEbD+51al+ekd2HN3XgTaAqPwJgbHkdEtjUcCY83lpySCAOUhZwVP850hEEpa969+Myw5usVkudLhQoLrU7q6UDAuhnjGbQgYmY6RqQTajb7m74CbWpTJUmxFDAAdB04t89/1O/w1cDnyilFU=')
#============================================================
# 指令區(#+指令)
def Judgment (input_message,event):
    """
        使用者輸入判斷全在這

        i每次user input ++，以用作作隨機值

        input_message = user input text.jsnode {user:"",text:""}

        event為add事件
    """
    i = random.randint(0,10700)
    if input_message in ['#log','#指令']:
        message = Log()
        line_bot_api.reply_message(event.reply_token,message)       #break
    elif input_message in ['#求圖','#隨機','#random','#ランダム']:
        value_i = {
            1   : ['惡魔偽王國軍'],         2 : ['茜里'],       3 : ['布丁'],       4 : ['忍'],         5 : ['伊莉亞'],     99 : ['依里'],
            6   : ['美食殿'],               7 : ['凱留'],       8 : ['佩可'],       9 : ['可可蘿'],    10 : ['祐樹'],       11 : ['謝菲'],      12 : ['孝心逐漸變質'],
            13  : ['慈樂之音'],            14 : ['紡希'],      15 : ['小望'],      16 : ['千歌'],
            17  : ['優妮們'],              18 : ['優妮'],      19 : ['克蘿依'],    20 : ['切嚕'],
            21  : ['墨丘利財團'],          22 : ['秋乃'],      23 : ['優花梨'],    24 : ['美冬'],      25 : ['珠希'],       26 : ['無人島'],
            27  : ['美里'],                28 : ['碧'],       29 : ['初音'],
            30  : ['克莉絲提娜'],          31 : ['矛依未'],    32 : ['似似花'],    33 : ['尾狗刀'],    34 : ['拉比林斯達'],  35 : ['愛梅斯'],
            36  : ['哞哞自衛隊'],          37 : ['真步'],      38 : ['霞'],        39 : ['真琴'],      40 : ['香織'],
            41  : ['小小甜心'],            42 : ['鏡華'],      43 : ['美美'],      44 : ['禊'],        45 : ['五等分的蘿莉'],
            46  : ['暮光流星群'],          47 : ['杏奈'],      48 : ['流夏'],      49 : ['深月'],      50 : ['七七香'],     51 : ['惠理子'],
            52  : ['Re:0'],               53 : ['愛蜜莉雅'],   54 : ['雷姆'],      55 : ['拉姆'],
            56  : ['破曉之星'],            57 : ['優衣'],      58 : ['日和'],      59 : ['怜'],
            60  : ['拉比林斯'],            61 : ['靜流'],      62 : ['璃乃'],      63 : ['姊妹'],
            64  : ['咲戀救護院'],          65 : ['咲戀'],      66 : ['鈴莓'],      67 : ['綾音'],      68 : ['胡桃'],
            69  : ['王宮騎士團'],          70 : ['純'],        71 : ['智'],        72 : ['茉莉'],      73 : ['團長們'],
            74  : ['月光學院'],            75 : ['伊緒'],      76 : ['鈴奈'],      77 : ['美咲'],
            78  : ['栞'],                 79 : ['真陽'],      80 : ['鈴'],        81 : ['莉瑪'],
            82  : ['純白之翼'],            83 : ['莫妮卡'],    84 : ['小雪'],      85 : ['妮諾'],      86 : ['空花'],       87 : ['步未'],
            88  : ['魔法少女'],            89 : ['終戰'],      90 : ['公主連結'],
            91  : ['馬納歷亞'],            92 : ['古蕾雅'],    93 : ['安'],       94 : ['露'],
            95  : ['吉塔'],                96 : ['亞里莎'],    97 : ['露娜'],     98 : ['愛梅斯'],
            100 : ['龍族巢穴'],           101 : ['帆稀'],     102 : ['嘉夜'],    103 : ['祈梨'],
            104 : ['偶像大師灰姑娘女孩'],  105 : ['卯月'],     106 : ['凜'],      107 : ['未央'],
            #108 : [],
        }
        input_message = value_i[i%len(value_i)+1][0]
# 動畫連結 import Animation.py & import FlexMessage.py
#    elif input_message in ['#10抽','#十抽','#抽卡','#抽']:
    elif input_message in ['#問題回報','#回報問題','#回報','#聯絡作者']:
        value_i = {
            1 : ["新功能、更多的彩蛋、更大的隨機性、更多對騎士君的愛~~~\n新版本逐漸更新上來了\n到作者的巴哈小屋一探究竟吧：\nhttps://m.gamer.com.tw/home/creationDetail.php?sn=4873921"],
            2 : ["騎士君有找到彩蛋嗎?\n聽說作者塞了一堆給人家呢\n巴哈小屋：https://m.gamer.com.tw/home/creationDetail.php?sn=4873921"],     
            3 : ["如果有什麼對優衣的建議可以到作者君的巴哈留言給他呦\n他的巴哈小屋：https://m.gamer.com.tw/home/creationDetail.php?sn=4873921"],
            4 : ["吶吶 可以告訴優衣騎士君要找作者做什麼咩?\n他的巴哈小屋：https://m.gamer.com.tw/home/creationDetail.php?sn=4873921"],
            5 : ["無能作者大大的巴哈呦~~\n作者的巴哈小屋：https://m.gamer.com.tw/home/creationDetail.php?sn=4873921"],
            6 : ["咦咦!!人家出現問題了嗎？\n\n趕快去他的巴哈小屋告訴她：https://m.gamer.com.tw/home/creationDetail.php?sn=4873921"],
            7 : ["騎士君，如果人家出現問題可以到作者大大的來幹爆作者呦\n\nhttps://m.gamer.com.tw/home/creationDetail.php?sn=4873921 "],
            8 : ["為什麼只有巴哈呢？\n是作者君沒有在玩dc呦~\nhttps://m.gamer.com.tw/home/creationDetail.php?sn=4873921 "],
        }
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text = value_i[i% len(value_i)+1][0]))
    elif input_message[:2] == '#抽':
        value_i = {
            1 : ["底下的角色頭像可以點擊呦~~"],
            2 : ["騎士君你已經有我了還想要更多的後宮嗎？"],     
            3 : ["與50幾位可愛公主們的冒險物語？\n\n有人家就足夠了呦~"],
            4 : ["接下來是可以預期的結果呢"],
            5 : ["咦?欸!\n抽這麼多不會太貪心了嗎?"],
            6 : ["欸秀，看人家施展爆死魔法呦~"],
            7 : ["各個卡池都可以抽呦(公主祭、新年、泳裝、情人節、萬聖節、聖誕節...)\n在後面輸入 自訂+機率 可設定出彩卡的機率呦"],
        }
        Cap = Capsule_Cul()
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),Cap.Capsule_end(input_message)])
    elif input_message[:3] == '#動畫': 
        line_bot_api.reply_message(event.reply_token,Anime_View(input_message))
    elif input_message[0] == '#' and len(input_message) <=5 :
        value_i = {
            1 : "指令錯誤呦，要不要再檢查一下呢",    #文字+圖片(陣列值為2)
            2 : "騎士君~優衣不認識這個指令",     
            3 : "目前沒有這條指令呦，可以跟作者大大聯絡，看能不能新增這項指令~\n(但依他的尿性八成又懶得去改了...)",
            4 : "騎士君~人家的指令功能少之又少\n但有什麼辦法呢，作者不知道又跑去哪偷懶了啦"
        }
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text = value_i[i% len(value_i)+1]))
# 梗圖 
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    if '世界' in input_message and '幸福' in input_message and '女孩' in input_message:
        value_i = {
            1 : ["如此溫暖的幸福，唯有騎士君呢~~","https://i.imgur.com/vbyBSHq.jpg"],   #文字+圖片(陣列值為2)
            2 : "只要學姊們的消失，優衣就一定是世界上最幸福的女孩",     
            3 : "珂朵莉?不~不~\n\n死人可沒有感受呢~~",
            4 : "こんなにも、たくさんの幸せをあの人に分けてもらった\n\nだから、きっと\n今の、私は\n誰が何と言おうと\n\n世界一、幸せな女の子だ",
            5 : "當然是優衣了啊，不然還有誰呢? (笑www舉刀~~",
            6 : "恩恩，我知道是人家呦",
            7 : "如果沒有學姊們的話...",
        }
        if(len(value_i[i% len(value_i)+1])==2):  #判斷 文字+圖片 陣列值為2
            line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
        else:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text = value_i[i% len(value_i)+1]))
    elif '發車' in input_message or 'wnacg' in input_message or 'nhentai' in input_message or '老司機' in input_message or  input_message == '卡' or '色情' in input_message or '上車' in input_message or '色圖' in input_message or '本本' in input_message:
        value_i = {
            1 : ImageMessageURL("https://i.imgur.com/w38zXOh.jpg"),
            2 : TextSendMessage(text="發車了發車了(叮叮叮!!")
        }
        line_bot_api.reply_message(event.reply_token,value_i[i% len(value_i)+1])
    elif 'ntr' in input_message or 'NTR' in input_message:
        value_i = {
            1 : "有誰提到了NTR嗎？",
            2 : "咦？NTR？\n騎士君~♡優衣再給你一次機會說清楚呦",
            3 : "騎士君為什麼又要說出NTR這個詞...",
            4 : "騎士君你說到了NTR嗎?\n不過在Line的世界...\n一個群組只能存在一個機器人\n學姊x騎士君也不會存在\n也代表著在這裡...\n騎士君身邊的機器人只能有優衣呦~~♡"
        }
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=value_i[i% len(value_i)+1]))
    elif input_message in ["優衣我愛你","我愛你優衣","我愛你","我喜歡你","我愛優衣"]:
        value_i = {
            1 : "嘻嘻 好開心~",
            2 : "嗯\n要永遠陪在優衣的身邊哦~",
            3 : "哇啊啊~\n騎士君這麼突然的嗎...不過，還是很開心///",
            4 : "嗯~~♡\n人家也是哦",
            5 : "咦欸 人家還沒準備好，怎麼辦怎麼辦，頭髮還有些亂，也沒有特別打扮過......騎士君，等我一下，絕對要等我哦///",
            6 : "嗯~這是騎士君對我的承諾，優衣一定會守護好這份羈絆"
        }
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=value_i[i% len(value_i)+1]))
    elif input_message in ['阿嘿顏','阿黑顏','アヘ顔','あへがお','O-Face','啊嘿顏']:
        value_i = {
            1 : "https://i.imgur.com/BqQX7KL.jpg",   
            2 : "https://i.imgur.com/iFe5eiN.jpg",  
            3 : "https://i.imgur.com/XR2iUcD.jpg",
            4 : "https://i.imgur.com/9uOIoXH.jpg",
            5 : "https://i.imgur.com/4bs4XQN.jpg"
        }
        line_bot_api.reply_message(event.reply_token,ImageMessageURL(value_i[i% len(value_i)+1]))
    elif '射爆' in input_message or '爆射' in input_message or input_message in ['射','射了','社保']:
        value_i = {
            1 : "https://i.imgur.com/VEmKBTm.jpg",   
            2 : "https://i.imgur.com/nhWCFTP.jpg",  
            3 : "https://i.imgur.com/lWzPVq4.jpg",
            4 : "https://i.imgur.com/m043hLL.jpg",
            5 : "https://i.imgur.com/fG7fJ2e.jpg",
            6 : "https://i.imgur.com/Ny71JoP.jpg",
            7 : "https://i.imgur.com/bqNJce8.jpg"
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text='大☆爆☆射！！！'),ImageMessageURL(value_i[i% len(value_i)+1])])
    elif input_message in ['怕爆','怕']:
        value_i = {
            1 : "https://i.imgur.com/Qww9qPE.jpg",   
            2 : "https://i.imgur.com/vhbLxU4.jpg",  
            3 : "https://i.imgur.com/I9u5jID.jpg",
            4 : "https://i.imgur.com/H72pl7m.png",
            5 : "https://i.imgur.com/dplH8Es.jpg"
        }
        line_bot_api.reply_message(event.reply_token,ImageMessageURL(value_i[i% len(value_i)+1]))
    elif '我婆' in input_message:
        value_i = {
            1 : "https://i.imgur.com/OnDeK8f.jpg",   
            2 : "https://i.imgur.com/rWcQJwD.jpg",  
            3 : "https://i.imgur.com/8ne7OeN.jpg",
            4 : "https://i.imgur.com/gVl6v1z.jpg",
            5 : "https://i.imgur.com/Ebvx2LH.jpg"
        }
        line_bot_api.reply_message(event.reply_token,ImageMessageURL(value_i[i% len(value_i)+1]))
    elif input_message in ['佬','大佬'] :
        value_i = {
            1 : "https://i.imgur.com/oH7jUmZ.jpg",   
            2 : "https://i.imgur.com/Mn7QLMR.jpg",  
            3 : "https://i.imgur.com/K3lkjyv.jpg",
            4 : "https://i.imgur.com/8niUWf6.jpg"
        }
        line_bot_api.reply_message(event.reply_token,ImageMessageURL(value_i[i% len(value_i)+1]))
    elif input_message in ['奶子','是什麼蒙蔽了我的雙眼','奶','巨乳','大奶','大奶子','おっぱい'] :
        value_i = {
            1 : "https://i.imgur.com/lLanAHP.jpg",   
            2 : "https://i.imgur.com/BXRoBtm.jpg",  
            3 : "https://i.imgur.com/5oM7q7O.jpg"
        }
        line_bot_api.reply_message(event.reply_token,ImageMessageURL(value_i[i% len(value_i)+1]))
    elif input_message in ['舔','舔爆'] :
        value_i = {
            1 : "https://i.imgur.com/SOVbAW0.jpg",   
            2 : "https://i.imgur.com/t75A3vZ.jpg",  
            3 : "https://i.imgur.com/v3DpiAK.jpg"
        }
        line_bot_api.reply_message(event.reply_token,ImageMessageURL(value_i[i% len(value_i)+1]))
    elif  '道歉' in input_message and  '露' in input_message:
        value_i = {
            1 : "https://i.imgur.com/HZLp9n5.jpg",   
            2 : "https://i.imgur.com/mJ5u9FR.jpg",  
            3 : "https://i.imgur.com/TwiqUp5.jpg",
            4 : "https://i.imgur.com/TjkbiNZ.jpg"
        }
        line_bot_api.reply_message(event.reply_token,ImageMessageURL(value_i[i% len(value_i)+1]))
    elif  input_message in ['鴨沒肉','やめろ','ヤメロ'] :
        value_i = {
            1 : "https://i.imgur.com/uyLpJfG.jpg",   
            2 : "https://i.imgur.com/64zdyMp.jpg",  
            3 : "https://i.imgur.com/WOG91NS.jpg",
            4 : "https://i.imgur.com/iAO2wRh.png"
        }
        line_bot_api.reply_message(event.reply_token,ImageMessageURL(value_i[i% len(value_i)+1]))
    elif  input_message in ['咕嚕靈波','咕嚕凌波']:
        value_i = {
            1 : "https://i.imgur.com/IXGLGXU.jpg",   
            2 : "https://i.imgur.com/rRAEQWI.jpg",  
            3 : "https://i.imgur.com/XsUTL7o.jpg",
            4 : "https://i.imgur.com/jlVp4ph.jpg",
            5 : "https://i.imgur.com/y8pHoyY.jpg",   
            6 : "https://i.imgur.com/LioJCLn.jpg",  
            7 : "https://i.imgur.com/l4GNzDx.jpg",
            8 : "https://i.imgur.com/nB9t44h.jpg"
        }
        line_bot_api.reply_message(event.reply_token,ImageMessageURL(value_i[i% len(value_i)+1]))
    elif  input_message in ['接頭','接頭霸王']:
        value_i = {
            1 :  ['https://i.imgur.com/qHWC2Tu.jpg','https://i.imgur.com/BlYRywQ.jpg'],
            2 :  ['https://i.imgur.com/0bVJvvv.jpg'],
            3 :  ['https://i.imgur.com/kTih1Ht.jpg'],
        }
        if(len(value_i[i% len(value_i)+1])==2): 
            line_bot_api.reply_message(event.reply_token,[ImageMessageURL(value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
        else:
            line_bot_api.reply_message(event.reply_token,ImageMessageURL(value_i[i% len(value_i)+1][0]))
    elif  input_message in ['課金','魔法小卡'] :
        value_i = {
            1 : "https://i.imgur.com/EdayZQQ.jpg",   
            2 : "https://i.imgur.com/6EJ9fI8.jpg",  
            3 : "https://i.imgur.com/g7KgiFY.jpg",
            4 : "https://i.imgur.com/ZMNl8wb.jpg",
            5 : "https://i.imgur.com/KGNxybo.jpg",
            6 : "https://i.imgur.com/sipuNE8.jpg",
            7 : "https://i.imgur.com/Yi6VARl.jpg",
            8 : ["繪師: だんなんだ-pixiv",   "https://i.imgur.com/BOMKsKV.jpg"],
            9 : ["真步開心",                "https://i.imgur.com/imuPBNv.jpg"]
        }
        if(len(value_i[i% len(value_i)+1])==2): 
            line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
        else:
            line_bot_api.reply_message(event.reply_token,ImageMessageURL(value_i[i% len(value_i)+1]))
    elif  input_message in ['爆死','綠色惡魔','花凜','保底','抽爆','母豬石','銀紙']:
        value_i = {
            1 :  "https://i.imgur.com/SuPGWfM.jpg",   
            2 :  "https://i.imgur.com/HmhqVvi.jpg",  
            3 :  "https://i.imgur.com/48iPeaK.jpg",
            4 :  "https://i.imgur.com/e3Jq6Fm.jpg",
            5 :  "https://i.imgur.com/VnHG8mp.jpg",   
            6 :  "https://i.imgur.com/wSATqcr.jpg",  
            7 :  "https://i.imgur.com/6Vhl6F5.jpg",
            8 :  "https://i.imgur.com/daXeV4b.jpg",
            9 :  "https://i.imgur.com/o8rO3n1.jpg",   
            10 : "https://i.imgur.com/267Ssh5.jpg",  
            11 : "https://i.imgur.com/9Tt4qJp.jpg",
            12 : "https://i.imgur.com/ctZT1kg.jpg",
            13 : "https://i.imgur.com/RRWeKtN.jpg",
            14 : "https://i.imgur.com/chxKxsG.jpg",
            15 : "https://i.imgur.com/pWY8jVP.jpg",
            16 : "https://i.imgur.com/ChF4Znh.jpg",   
            17 : "https://i.imgur.com/Q8yr0a2.jpg",  
            18 : "https://i.imgur.com/vm7ekUp.jpg",
            19 : "https://i.imgur.com/HxuU6fW.jpg",
            20 : "https://i.imgur.com/1jtV5XT.jpg"
        }
        line_bot_api.reply_message(event.reply_token,ImageMessageURL(value_i[i% len(value_i)+1]))
    elif input_message in ['草','www','草w']:
        value_i = {
            1 : "https://i.imgur.com/DrtsKg6.jpg",   
            2 : "https://i.imgur.com/gzZQYAj.jpg",  
            3 : "https://i.imgur.com/OMH6DKJ.jpg"
        }
        line_bot_api.reply_message(event.reply_token,ImageMessageURL(value_i[i% len(value_i)+1]))
    elif input_message in ['你沒有妹妹','妹妹','いもうと']:
        value_i = {
            1 : [ImageMessageURL("https://i.imgur.com/Hb24JxT.jpg")],
            2 : [TextSendMessage(text = "那種東西不存在的呦~~")], 
            3 : [TextSendMessage(text = "是指璃乃醬還是茜里醬又或者是栞栞呢？")],
            4 : [ImageMessageURL("https://i.imgur.com/rix94rm.jpg")],
            5 : [VideoMessageURL("https://i.imgur.com/cEV6Xmb")]
        }
        line_bot_api.reply_message(event.reply_token,value_i[i% len(value_i)+1][0])
# import FlexMessage.py
    elif input_message[:2] == '我就' and len(input_message)<=6 :
        if input_message[2] == '爛':
            value_i = {
                1 : 'https://i.imgur.com/ZqjhK79.jpg',   
                2 : 'https://i.imgur.com/nXsxbUW.jpg'
            }
            line_bot_api.reply_message(event.reply_token,ImageMessageURL(value_i[i% len(value_i)+1]))
# 我就xx自定義梗圖
        else:
            value_i = {
                1 : 'https://i.imgur.com/4I79zqs.png',   
                2 : 'https://i.imgur.com/88pRc9Q.png',  
                3 : 'https://i.imgur.com/2OfFdhk.png'
            }
            value_color = {
                1 : 'https://i.imgur.com/I7VUOz5.png',   
                2 : 'https://i.imgur.com/wxgQArs.png',  
                3 : 'https://i.imgur.com/G4PNCSM.png',
                4 : 'https://scdn.line-apps.com/n/channel_devcenter/img/flexsnapshot/clip/clip15.png',  
                5 : 'https://i.imgur.com/sXetQPr.png'
            }
            line_bot_api.reply_message(event.reply_token,image_bubble_message(value_i[i% len(value_i)+1],input_message,value_color[i% len(value_color)+1]))
# 角色篇 import FlexMessage.py
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
### 伊麗莎白牧場 ###
### エリザベスパーク牧場 ###
### 伊麗莎白牧場 ###
    elif input_message in ['栞','小栞','西歐力','シオリ','病弓','栞栞']:
        value_i = {
            1 :  ['繪師: GaaRa-pixiv',          'https://i.imgur.com/7TXClz2.jpg'],
            2 :  ['繪師: Mobu-pixiv',           'https://i.imgur.com/rGLO0Po.jpg'],
            3 :  ['繪師: 桜庭ロイヤル-pixiv',    'https://i.imgur.com/bEdh6hw.jpg'],
            4 :  ['繪師: 心みんとん-pixiv',      'https://i.imgur.com/G2Lp8sK.jpg'],
            5 :  ['繪師: @tamakaga-twitter',    'https://i.imgur.com/mLejb61.jpg'],
            6 :  ['繪師: @yantaro5446-twitter', 'https://i.imgur.com/YJhCqJ5.jpg'],
            7 :  ['繪師: @YAZI114-twitter',     'https://i.imgur.com/BDH0f10.jpg'],
            8 :  ['繪師: しぇるてぃー-pixiv',    'https://i.imgur.com/O39Sjdk.jpg'],
            9 :  ['繪師: アイダ-pixiv',          'https://i.imgur.com/h19VB6a.jpg'],
            10 : ['繪師: aono-pixiv',           'https://i.imgur.com/bZdjH05.jpg'],
            11 : ['繪師: 紫桐シート-pixiv',      'https://i.imgur.com/GsZ8AOa.jpg'],
            12 : ['繪師: ダーゴ-pixiv',          'https://i.imgur.com/waFo95L.jpg'],
            13 : ['繪師: まりぴ-pixiv',          'https://i.imgur.com/Xe1DAOC.jpg'],
            14 : ['繪師: まりぴ-pixiv',          'https://i.imgur.com/3JQbmuO.jpg'],
            15 : ['繪師: たく庵-pixiv',          'https://i.imgur.com/NkPh6LN.jpg'],
            16 : ['繪師: ペヤンキー-pixiv',      'https://i.imgur.com/Bgn3DWb.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message in ['真陽','マヒル','奶牛']:
        value_i = {
            1 :  ['繪師: うまるつふり-pixiv',            'https://i.imgur.com/4ezsFUo.jpg'],
            2 :  ['繪師: つきしろ やよい-pixiv',         'https://i.imgur.com/edYYsYN.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message in ['鈴','リン','森近鈴','松鼠','遊俠鈴']:
        value_i = {
            1 :  ['繪師: Zn-pixiv',             'https://i.imgur.com/9tSsHEF.jpg'],
            2 :  ['繪師: ダーゴ-pixiv',         'https://i.imgur.com/8kyQmGJ.jpg'],
            3 :  ['繪師: ジヤス-pixiv',         'https://i.imgur.com/fLy85C0.jpg'],
            4 :  ['繪師: ヒーロー-pixiv',       'https://i.imgur.com/vC8ZmEr.jpg'],
            5 :  ['繪師: たぬこ-pixiv',         'https://i.imgur.com/i8K8RmM.jpg'],
            6 :  ['繪師: ねこまんま先生-pixiv',  'https://i.imgur.com/OXHf69V.jpg'],
            7 :  ['繪師: Kiosk-pixiv',          'https://i.imgur.com/HrynwoW.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message in ['莉瑪','リマ','羊駝']:
        value_i = {
            1 :  ['繪師: ワタフジマコト-pixiv',   'https://i.imgur.com/dqeN5SV.jpg'],
            2 :  ['繪師: gabo-pixiv',            'https://i.imgur.com/WmTQrGL.jpg'],
            3 :  ['繪師: Kakao346-pixiv',        'https://i.imgur.com/aG3WL1j.jpg'],
            4 :  ['繪師: 빙구-pixiv',            'https://i.imgur.com/yfhu5tu.jpg'],
            5 :  ['繪師: かぼちゃ兎-pixiv',      'https://i.imgur.com/R13jfYh.jpg'],
            6 :  ['繪師: ripe.C-pixiv',         'https://i.imgur.com/W88M1Ph.jpg',        'https://i.imgur.com/pUXMGKC.jpg']
        }
        if len(value_i[i% len(value_i)+1])==3 :
            line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1]),ImageMessageURL(value_i[i% len(value_i)+1][2])])
        elif len(value_i[i% len(value_i)+1])==2 :
            line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
### 月光學院 ###
### ルーセント学院 ###
### 月光學院 ###
    elif input_message in ['月光學院','ルーセント学院']:
        value_i = {
            1 :  ['繪師: 菖蒲-pixiv',         'https://i.imgur.com/vvzNgXT.jpg'],
            2 :  ['繪師: S.U.-pixiv',        'https://i.imgur.com/2ayupbZ.jpg'],
            3 :  ['繪師: Itoichi-pixiv',     'https://i.imgur.com/AsV2SJ2.jpg'],
            4 :  ['繪師: ヤチモト-pixiv',     'https://i.imgur.com/NEuDpHQ.jpg'],
            5 :  ['繪師: 関西ジン-pixiv',     'https://i.imgur.com/OUqJ5YL.jpg'],
            6 :  ['繪師: やまだσ-pixiv',      'https://i.imgur.com/iGOKQtN.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message in ['美咲','ミサキ','玉泉美咲','眼球法','萬聖美咲']:
        value_i = {
            1 :  ['繪師: レオナート-pixiv',      'https://i.imgur.com/rDrtVAC.jpg'],
            2 :  ['繪師: うましお-pixiv',        'https://i.imgur.com/CRQH9Ek.jpg'],
            3 :  ['繪師: うまるつふり-pixiv',    'https://i.imgur.com/omIhOs8.jpg'],
            4 :  ['繪師: しもん-pixiv',         'https://i.imgur.com/kKBE1aO.jpg'],
            5 :  ['繪師: アイダ-pixiv',         'https://i.imgur.com/MU4Hykc.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message in ['伊緒','イオ','支倉伊緒','魅魔','老師','伊歐派','泳裝伊緒']:
        value_i = {
            1 :  ['繪師: 92M-pixiv',           'https://i.imgur.com/Ohkd2DO.jpg'],
            2 :  ['繪師: りりか-pixiv',         'https://i.imgur.com/lev3VPT.jpg'],
            3 :  ['繪師: ヤマブキイロ-pixiv',   'https://i.imgur.com/aWyGiYL.jpg'],
            4 :  ['繪師: ひとつのなか-pixiv',   'https://i.imgur.com/DHUDWbD.jpg'],
            5 :  ['繪師: みすコン-pixiv',       'https://i.imgur.com/zjAQsUn.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message in ['鈴奈','スズナ','美波鈴奈','暴弓','爆弓','白癡','泳裝鈴奈']:
        value_i = {
            1 :  ['繪師: ひとつのなか-pixiv',     'https://i.imgur.com/EjcU0Im.jpg'],
            2 :  ['繪師: 結城辰也-pixiv',         'https://i.imgur.com/MkOrjea.jpg'],
            3 :  ['繪師: YH-pixiv',              'https://i.imgur.com/JrrgGN6.jpg'],
            4 :  ['繪師: 天雷-pixiv',            'https://i.imgur.com/e7OsQRB.jpg'],
            5 :  ['繪師: ダーゴ-pixiv',          'https://i.imgur.com/ILNauCi.jpg'],
            6 :  ['繪師: Rona-pixiv',            'https://i.imgur.com/fm0Pk7i.jpg'],
            7 :  ['繪師: 電解水-pixiv',          'https://i.imgur.com/Wykgysq.jpg'],
            8 :  ['繪師: フジフジ-pixiv',        'https://i.imgur.com/bXNXfuR.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
### 拉比林斯 ###
### ラビリンス ###
### 拉比林斯 ###
    elif input_message in ['拉比林斯','ラビリンス']:
        value_i = {
            1 :  ['繪師: みず-pixiv',          'https://i.imgur.com/F9SXxTp.jpg'],
            2 :  ['繪師: ユキタカ-pixiv',      'https://i.imgur.com/iQVOxk2.jpg'],
            3 :  ['繪師: みどりのちゃ-pixiv',  'https://i.imgur.com/2wbKiAy.jpg'],
            4 :  ['繪師: 秋月リア-pixiv',      'https://i.imgur.com/NRgmRRj.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message in ['靜流','シズル','星野靜流','姐姐','弟控','情人節靜流']:
        value_i = {
            1 :  ['繪師: watchdog_rol-pixiv',   'https://i.imgur.com/Xu8PE9b.jpg'],
            2 :  ['繪師: まよ丼-pixiv',         'https://i.imgur.com/nF8bib2.jpg'],
            3 :  ['繪師: ナ²-pixiv',            'https://i.imgur.com/a8BLBak.jpg'],
            4 :  ['繪師: セーラ-pixiv',         'https://i.imgur.com/e9sXXu5.jpg'],
            5 :  ['繪師: 坊橋夜泊-pixiv',       'https://i.imgur.com/YklV0js.jpg'],
            6 :  ['繪師: ロアン-pixiv',         'https://i.imgur.com/hAK5NYP.jpg'],
            7 :  ['繪師: みず-pixiv',           'https://i.imgur.com/oU6wWfr.jpg'],
            8 :  ['繪師: ひとつのなか-pixiv',    'https://i.imgur.com/IlnJe8Z.jpg'],
            9 :  ['繪師: 千里凌酱-pixiv',       'https://i.imgur.com/qcKvMcr.jpg'],
            10 : ['繪師: 千里凌酱-pixiv',       'https://i.imgur.com/1ANXoEU.jpg'],
            11 : ['繪師: ddolggol-pixiv',      'https://i.imgur.com/kBRxhWE.jpg'],
            12 : ['繪師: RYUKI-pixiv',         'https://i.imgur.com/Hzf2VCF.jpg'],
            13 : ['繪師: Itoichi-pixiv',       'https://i.imgur.com/3hf7n4q.jpg'],
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message in ['妹弓','梨乃','璃乃','リノ','智障','衣之咲璃乃']:
        value_i = {
            1 :  ['繪師: 真崎ケイ-pixiv',    'https://i.imgur.com/uKiWtdI.jpg'],
            2 :  ['繪師: Mauve-pixiv',      'https://i.imgur.com/3SBQq5o.jpg'],
            3 :  ['繪師: HIROKAZU-pixiv',   'https://i.imgur.com/BWXJYH8.jpg'],
            4 :  ['繪師: HIROKAZU-pixiv',   'https://i.imgur.com/OlNs5LG.jpg'],
            5 :  ['繪師: HIROKAZU-pixiv',   'https://i.imgur.com/lD2qFUi.jpg'],
            6 :  ['繪師: HIROKAZU-pixiv',   'https://i.imgur.com/qSiPpAc.jpg'],
            7 :  ['繪師: HIROKAZU-pixiv',   'https://i.imgur.com/hJitlbn.jpg'],
            8 :  ['繪師: みず-pixiv',        'https://i.imgur.com/ul5x7d4.jpg'],
            9 :  'https://i.imgur.com/1eLEkSN.jpg',
            10 : ['繪師: アイダ-pixiv',      'https://i.imgur.com/RTySuyH.jpg']
        }
        if(len(value_i[i% len(value_i)+1])==2): 
            line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
        else:
            line_bot_api.reply_message(event.reply_token,ImageMessageURL(value_i[i% len(value_i)+1]))
### 森林守衛 ###
### フォレスティエ ###
### 森林守衛 ###
    elif input_message in ['美里','愛川美里','ミサト','聖母','美里老師','水母','泳裝美里']:
        value_i = {
            1 :  ['繪師: @monmon_shimon_-twitter',   'https://i.imgur.com/QsArrQW.jpg'],
            2 :  ['繪師: @Hello_pty-twitter',        'https://i.imgur.com/88X1SpO.jpg'],
            3 :  ['繪師: @shotenana-twitter',        'https://i.imgur.com/671lWeD.jpg'],
            4 :  ['繪師: @teffish-twitter',          'https://i.imgur.com/gyiQlHA.jpg'],
            5 :  ['繪師: @92M-twitter',              'https://i.imgur.com/SdgoaDF.jpg'],
            6 :  ['繪師: ヤマブキイロ-pixiv',         'https://i.imgur.com/zdgNpBt.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message in ['碧','アオイ','雙葉碧','香菜弓'] or (input_message[:2] == '邊緣' and len(input_message) <= 4) :
        value_i = {
            1 :  ['繪師: @kurororo_rororo-twitter',     'https://i.imgur.com/B9I4bm1.jpg'],
            2 :  ['繪師: ミチル-pixiv',                 'https://i.imgur.com/FVpUqpf.jpg'],
            3 :  ['繪師: @sakuragi0127-twitter',        'https://i.imgur.com/bQMFoL4.jpg'],
            4 :  ['繪師: やま兎-pixiv',                 'https://i.imgur.com/7B82lli.jpg'],
            5 :  ['繪師: すけsk-pixiv',                 'https://i.imgur.com/Mmw25L7.jpg'],
            6 :  ['繪師: 秋ナス-pixiv',                 'https://i.imgur.com/cUPv6eu.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message in ['初音','ハツネ','柏崎初音','睡美人','泳裝初音']:
        value_i = {
            1 :  ['繪師: ヤンタロウ-pixiv',     'https://i.imgur.com/QQ5alwd.jpg'],
            2 :  ['繪師: TYTS-pixiv',          'https://i.imgur.com/jTo5qH3.jpg'],
            3 :  ['繪師: 結城辰也-pixiv',       'https://i.imgur.com/UtkMYdI.jpg'],
            4 :  ['繪師: ゆりりん-pixiv',       'https://i.imgur.com/5E6XgR8.jpg'],
            5 :  ['繪師: ジャンク堂-pixiv',     'https://i.imgur.com/WTIywxi.jpg'],
            6 :  ['繪師: meel-pixiv',          'https://i.imgur.com/xN2lnOm.jpg'],
            7 :  ['繪師: 天雷-pixiv',          'https://i.imgur.com/F788xfj.jpg'],
            8 :  ['繪師: sonchi-pixiv',        'https://i.imgur.com/AXTx6rO.jpg'],
            9 :  ['繪師: ゆんみ-pixiv',        'https://i.imgur.com/2DJUfQU.jpg'],
            10 : ['繪師: ひことう(彥灯)-pixiv', 'https://i.imgur.com/5JawGjF.jpg'],
            
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
### 純白之翼 蘭德索爾分部 ###
### ヴァイスフリューゲル ランドソル支部 ###
### 純白之翼 ###
    elif input_message in ['純白之翼','ヴァイスフリューゲル ランドソル支部','純白之翼 蘭德索爾分部','奇葩公會']:
        value_i = {
            1 :  ['繪師: ぬるぷよ-pixiv',          'https://i.imgur.com/tio37LX.jpg'],
            2 :  ['繪師: なかひま-pixiv',          'https://i.imgur.com/hyxY4Hi.jpg'],
            3 :  ['繪師: うせつ（右折）-pixiv',     'https://i.imgur.com/DANzNSk.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message in ['妮諾','ニノン','扇子','忍者','江戶妮諾']:
        value_i = {
            1 :  ['繪師: たてじまうり-pixiv',      'https://i.imgur.com/e1CEWSd.jpg'],
            2 :  ['繪師: ぬるぷよ-pixiv',          'https://i.imgur.com/UMpxZQ7.jpg'],
            3 :  ['繪師: S.U.-pixiv',             'https://i.imgur.com/8YWxDvV.jpg'],
            4 :  ['繪師: phobishu-pixiv',         'https://i.imgur.com/1vWMYAr.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message in ['莫妮卡','モニカ','毛二力','Monika','monika']:
        value_i = {
            1 :  ['繪師: まぉー。-pixiv',        'https://i.imgur.com/id3cEAo.jpg'],
            2 :  ['繪師: まぉー。-pixiv',        'https://i.imgur.com/pHPN52u.jpg'],
            3 :  ['繪師: 浣狸-pixiv',            'https://i.imgur.com/IZgpNuR.jpg'],
            4 :  ['繪師: 水無月みず-pixiv',      'https://i.imgur.com/uqUbiik.jpg'],
            5 :  ['繪師: 紅薙ようと-pixiv',      'https://i.imgur.com/8XffJLz.jpg'],
            6 :  ['繪師: 引きニート-pixiv',      'https://i.imgur.com/duJmuoQ.jpg'],
            7 :  ['繪師: AJ-pixiv',             'https://i.imgur.com/idWxFcC.jpg'],
            8 :  ['跳到just monika彩蛋']
        }
        try:
            line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
        except:
            pass
    elif input_message in ['空花','クウカ','抖M','抖m','江戶空花'] :
        value_i = {
            1 :  ['繪師: ダーゴ-pixiv',        'https://i.imgur.com/JagI34h.jpg'],
            2 :  ['繪師: ジヤス-pixiv',        'https://i.imgur.com/J8pKPT0.jpg'],
            3 :  ['繪師: 桶乃かもく-pixiv',    'https://i.imgur.com/u5OAmLp.jpg'],
            4 :  ['繪師: たぐ-pixiv',          'https://i.imgur.com/2gUWFwE.jpg'],
            5 :  ['繪師: えぴ-pixiv',          'https://i.imgur.com/HkxfmUi.jpg'],
            6 :  ['繪師: S.U.-pixiv',          'https://i.imgur.com/VVWeLcP.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message in ['步未','アユミ','石橋步未','路人妹' ,'路人'] :
        value_i = {
            1 :  ['繪師: あやみゆき-pixiv',      'https://i.imgur.com/wugza8u.jpg'],
            2 :  ['繪師: セランポーレ-pixiv',    'https://i.imgur.com/YgCOdxJ.jpg'],
            3 :  ['繪師: Acuma-pixiv',          'https://i.imgur.com/2L8K0D4.jpg'],
            4 :  ['繪師: 巧克力酱嗷-pixiv',      'https://i.imgur.com/HVaTlao.jpg'],
            5 :  ['繪師: セーリュー-pixiv',      'https://i.imgur.com/eAt5NmX.jpg'],
            6 :  ['繪師: スギユウ-pixiv',        'https://i.imgur.com/pf414Hl.jpg'],
            7 :  ['繪師: 関西ジン-pixiv',        'https://i.imgur.com/n33p8Nr.jpg'],
            8 :  ['繪師: ぐま-pixiv',            'https://i.imgur.com/cKwmATV.jpg'],
            9 :  ['繪師: スギユウ-pixiv',        'https://i.imgur.com/fG2T97o.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message in ['雪','アユミ','小雪','虹村雪','雪哥','偽娘','女装大佬','自戀狂'] :
        value_i = {
            1 :  ['繪師: ダーゴ-pixiv',      'https://i.imgur.com/5WVPTLL.jpg'],
            2 :  ['繪師: ねこちゃん-pixiv',   'https://i.imgur.com/6eQnJpA.jpg'],
            3 :  ['繪師: りこ-pixiv',        'https://i.imgur.com/qQi6c2M.jpg'],
            4 :  ['繪師: りこ-pixiv',        'https://i.imgur.com/aoMKsKA.jpg'],
            5 :  ['繪師: ASLE-pixiv',        'https://i.imgur.com/ptmTKlR.jpg'],
            6 :  ['繪師: みさき-pixiv',      'https://i.imgur.com/5FBxwBT.jpg'],
            7 :  ['繪師: ぐっち庵-pixiv',    'https://i.imgur.com/AeoEaDd.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
### 咲戀救護院 ###
### サレンディア救護院 ###
### 救護院 ###
    elif input_message in ['咲戀救護院','サレンディア救護院','救護院']:
        value_i = {
            1 :  ['繪師: S.U.-pixiv',       'https://i.imgur.com/7gMuqoy.jpg'],
            2 :  ['繪師: AJ-pixiv',         'https://i.imgur.com/tzQswOy.jpg'],
            3 :  ['繪師: ヤチモト-pixiv',    'https://i.imgur.com/BQpIStn.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message in ['咲戀','咲戀媽媽','充電寶','泳媽','媽','サレン','泳媽','泳裝咲戀']:
        value_i = {
            1 :  ['繪師: らんち-pixiv',              'https://i.imgur.com/JV5BTEz.jpg'],
            2 :  ['繪師: hemachi-pixiv',            'https://i.imgur.com/2teJ0AL.jpg'],
            3 :  ['繪師: SeeUmai-pixiv',            'https://i.imgur.com/8jiJdzM.jpg'],
            4 :  ['繪師: カケル-pixiv',              'https://i.imgur.com/LM8RSJw.jpg'],
            5 :  ['繪師: つかさ-pixiv',              'https://i.imgur.com/vvwxljH.jpg'],
            6 :  ['繪師: アリア-pixiv',              'https://i.imgur.com/HcHuwDl.jpg'],
            7 :  ['繪師: atychi-pixiv',             'https://i.imgur.com/z8WnFpy.jpg'],
            8 :  ['繪師: あんべよしろう-pixiv',      'https://i.imgur.com/3J0rt2k.jpg'],
            9 :  ['繪師: EpicLoot-pixiv',           'https://i.imgur.com/C7PEdmq.jpg'],
            10 : ['繪師: ヒーロー-pixiv',            'https://i.imgur.com/HANfFFb.jpg'],
            11 : ['繪師: ZN (あえん)-pixiv',         'https://i.imgur.com/MI7NZIS.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message in ['鈴莓','スズメ','女僕','恐怖份子','天野鈴莓','正月鈴莓','泳裝鈴莓']:
        value_i = {
            1 :  ['繪師: ダーゴ-pixiv',     'https://i.imgur.com/Mj7Vxxc.jpg'],
            2 :  ['繪師: ダーゴ-pixiv',     'https://i.imgur.com/YJMAbHJ.jpg'],
            3 :  ['繪師: ダーゴ-pixiv',     'https://i.imgur.com/QduwCSX.jpg'],
            4 :  ['繪師: ROIN-pixiv',      'https://i.imgur.com/k4weIQw.jpg'],
            5 :  ['繪師: りこ-pixiv',      'https://i.imgur.com/zvnXYcT.jpg'],
            6 :  ['繪師: Set-pixiv',       'https://i.imgur.com/z5wHpnK.jpg'],
            7 :  ['繪師: 天雷-pixiv',      'https://i.imgur.com/yx82sjg.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message in ['綾音','アヤネ','北條綾音','熊錘','噗吉','聖誕綾音']:
        value_i = {
            1 :  ['繪師: 夢乃杜-pixiv',          'https://i.imgur.com/G4lAvYH.jpg'],
            2 :  ['繪師: うまるつふり-pixiv',    'https://i.imgur.com/T0IabEQ.jpg'],
            3 :  ['繪師: 世音-pixiv',           'https://i.imgur.com/vVMd7HJ.jpg'],
            4 :  ['繪師: けいらん-pixiv',        'https://i.imgur.com/vZI82po.jpg'],
            5 :  ['繪師: うまるつふり-pixiv',    'https://i.imgur.com/sA2s1hL.jpg'],
            6 :  ['繪師: 天雷-pixiv',           'https://i.imgur.com/q4WHogN.png'],
            7 :  ['繪師: ダーゴ-pixiv',         'https://i.imgur.com/Lz3mk9N.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message in ['胡桃','クルミ','栗林胡桃','聖誕胡桃']:
        value_i = {
            1 :  ['繪師: 関西ジン-pixiv',      'https://i.imgur.com/h5SinVW.jpg'],
            2 :  ['繪師: ミュー-pixiv',        'https://i.imgur.com/CtTm2kO.jpg'],
            3 :  ['繪師: AJ-pixiv',           'https://i.imgur.com/iZlOaV3.jpg'],
            4 :  ['繪師: えむ-pixiv',         'https://i.imgur.com/1mYlZ9n.jpg'],
            5 :  ['繪師: RYUKI-pixiv',        'https://i.imgur.com/G64Xivs.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
### 墨丘利財團 ###
### メルクリウス財団 ###
### 財團 ###
    elif input_message in ['墨丘利財團','メルクリウス財団','財團']:
        value_i = {
            1 :  ['繪師: AJ-pixiv',           'https://i.imgur.com/S3Ld3So.jpg'],
            2 :  ['繪師: 夜凪朝妃-pixiv',      'https://i.imgur.com/ZsHkXJm.jpg'],
            3 :  ['繪師: ヤチモト-pixiv',      'https://i.imgur.com/Zo5tJYw.jpg'],
            4 :  ['繪師: HIROKAZU-pixiv',     'https://i.imgur.com/7VNue19.jpg'],
            5 :  ['繪師: 夜凪朝妃-pixiv',      'https://i.imgur.com/kVkppDM.jpg'],
            6 :  ['繪師: AJ-pixiv',           'https://i.imgur.com/VJEvtlM.jpg'],
            7 :  ['繪師: あかざてり-pixiv',    'https://i.imgur.com/LGWONXZ.jpg'],
            8 :  ['繪師: こうちゃ。-pixiv',    'https://i.imgur.com/1eKDiOg.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message in ['秋乃','アキノ','墨丘利財團唯一指定三星','財團之恥']:
        value_i = {
            1 :  ['繪師: みずなし-pixiv',           'https://i.imgur.com/nLPrz2D.jpg'],
            2 :  ['繪師: ダーゴ-pixiv',             'https://i.imgur.com/8PEV511.jpg'],
            3 :  ['繪師: 真宮原ヒトシゲ-pixiv',      'https://i.imgur.com/5wbSJ5G.jpg'],
            4 :  ['繪師: ヒーロー-pixiv',           'https://i.imgur.com/0Ibk5HR.jpg'],
            5 :  ['繪師: 天雷-pixiv',               'https://i.imgur.com/Pp7pMVe.jpg'],
            6 :  ['繪師: sonchi-pixiv',             'https://i.imgur.com/b2w8CMp.jpg'],
            7 :  ['繪師: ぐっち庵-pixiv',           'https://i.imgur.com/PM02VxP.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message in ['優花梨','ユカリ','酒鬼']:
        value_i = {
            1 :  ['繪師: けんぴゃっ-pixiv',              'https://i.imgur.com/3grit6p.jpg'],
            2 :  ['繪師: 石川健太-pixiv',                'https://i.imgur.com/e28UBg8.jpg'],
            3 :  ['繪師: 天雷-pixiv',                   'https://i.imgur.com/2ShceE9.jpg'],
            4 :  ['繪師: 鳩尾-pixiv',                   'https://i.imgur.com/kFqvMMn.jpg'],
            5 :  ['繪師: 昌未-pixiv',                   'https://i.imgur.com/Dv4rJgh.jpg'],
            6 :  ['繪師: りこ-pixiv',                   'https://i.imgur.com/LQRJRp7.jpg'],
            7 :  ['繪師: 7010-pixiv',                   'https://i.imgur.com/sU3Ceak.jpg'],
            8 :  ['繪師: sonchi-pixiv',                 'https://i.imgur.com/5eHL47t.jpg'],
            9 :  ['繪師: まぉー。-pixiv',                'https://i.imgur.com/x4WaX1b.jpg'],
            10 : ['繪師: ぐっち庵-pixiv',                'https://i.imgur.com/2n2O2q3.jpg'],
            11 : ['繪師: PTD-pixiv',                    'https://i.imgur.com/Hefwndh.jpg'],
            12 : ['繪師: ミュー-pixiv',                  'https://i.imgur.com/7bVx6fN.jpg'],
            13 : ['繪師: @srm_chi-twitter',             'https://i.imgur.com/cqoR7cE.jpg'],
            14 : ['繪師: @dosukoi_fresh-twitter',       'https://i.imgur.com/n4cY09W.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message in ['珠希','タマキ','宮坂珠希','貓劍','貓賊','泳裝珠希']:
        value_i = {
            1 :  ['https://i.imgur.com/Y6Hubmx.jpg'],
            2 :  ['繪師: Donutman-pixiv',       'https://i.imgur.com/7fsnRcy.jpg'],
            3 :  ['繪師: トプ-pixiv',           'https://i.imgur.com/adKZbm0.jpg'],
            4 :  ['繪師: 水無月みず-pixiv',      'https://i.imgur.com/IodPy4h.jpg'],
            5 :  ['繪師: ROIN-pixiv',           'https://i.imgur.com/hgc0rr5.jpg'],
            6 :  ['繪師: あんず-pixiv',         'https://i.imgur.com/uPj8mrO.jpg'],
            7 :  ['繪師: ぐっち庵-pixiv',       'https://i.imgur.com/xKXragw.jpg'],
            8 :  ['繪師: ダーゴ-pixiv',         'https://i.imgur.com/llc5HX0.jpg']
        }
        if(len(value_i[i% len(value_i)+1])==2): 
            line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
        else:
            line_bot_api.reply_message(event.reply_token,ImageMessageURL(value_i[i% len(value_i)+1][0]))
    elif input_message in ['美冬','ユカリ','大神美冬','屠龍者','打工仔','泳裝美冬']:
        value_i = {
            1 :  ['繪師: AJ-pixiv',             'https://i.imgur.com/YwHKCSK.jpg'],
            2 :  ['繪師: ぐっち庵-pixiv',        'https://i.imgur.com/t0AagIv.jpg'],
            3 :  ['繪師: プトン-pixiv',          'https://i.imgur.com/1I33uq2.jpg'],
            4 :  ['繪師: れつな-pixiv',          'https://i.imgur.com/TiCccLi.jpg'],
            5 :  ['繪師: あんず-pixiv',          'https://i.imgur.com/51bzHBf.jpg'],
            6 :  ['繪師: リブッチ-pixiv',        'https://i.imgur.com/2hCLlqE.jpg'],
            7 :  ['繪師: 水ようかん-pixiv',      'https://i.imgur.com/vOyBmZB.jpg'],
            8 :  ['繪師: ミュー-pixiv',          'https://i.imgur.com/aAxUlIQ.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message == '無人島':
        value_i = {
            1 :  ['繪師: 161803393-pixiv',      'https://i.imgur.com/XYGSCyu.jpg'],
            2 :  ['繪師: AJ-pixiv',             'https://i.imgur.com/yxXnL0e.jpg'],
            3 :  ['繪師: あかざてり-pixiv',      'https://i.imgur.com/o2JUEOw.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
### 自衛團 ###
### カォン自警団 ###
### 哞哞自衛隊 ###
    elif input_message in ['哞哞自衛隊','自衛隊','カォン自警団']:
        value_i = {
            1 :  ['繪師: AJ-pixiv',                 'https://i.imgur.com/i9BKQpj.jpg'],
            2 :  ['繪師: ぬるぷよ-pixiv',            'https://i.imgur.com/5BnCetn.jpg'],
            3 :  ['繪師: AJ-pixiv',                 'https://i.imgur.com/EwCexQp.jpg'],
            4 :  ['繪師: WaterRing-pixiv',          'https://i.imgur.com/qQGcoBX.jpg'],
            5 :  ['繪師: MaJiang-pixiv',            'https://i.imgur.com/dArZxel.jpg'],
            6 :  ['繪師: konigstigerchan-pixiv',    'https://i.imgur.com/kkNl4dX.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message in ['真步','マホ','姬宫真步','真步公主','公主病','泳裝真步']:
        value_i = {
            1 :  ['繪師: S.U.-pixiv',           'https://i.imgur.com/yfgrop2.jpg'],
            2 :  ['繪師: ぺろんちょ-pixiv',      'https://i.imgur.com/npCDt3p.jpg'],
            3 :  ['繪師: 猫小渣-pixiv',          'https://i.imgur.com/SLSkhAO.jpg'],
            4 :  ['繪師: yamchu-pixiv',         'https://i.imgur.com/nbs4CXK.jpg'],
            5 :  ['繪師: JMao-pixiv',           'https://i.imgur.com/qo2wk18.jpg'],
            6 :  ['繪師: ダーゴ-pixiv',          'https://i.imgur.com/dn9kpoN.jpg'],
            7 :  ['繪師: 水無月みず-pixiv',      'https://i.imgur.com/iNKJY7T.jpg'],
            8 :  ['繪師: 傻蛋喵-pixiv',          'https://i.imgur.com/mp8YBnO.jpg'],
            9 :  ['繪師: 傻蛋喵-pixiv',          'https://i.imgur.com/5ttEoW0.jpg'],
            10 : ['繪師: 7010-pixiv',           'https://i.imgur.com/7LNxWXT.jpg'],
            11 : ['繪師: 凤鸢-pixiv',            'https://i.imgur.com/PCK4fdC.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message in ['霞','カスミ','驢妹','偵探','水瀨祈','魔法少女霞']:
        value_i = {
            1 :  ['繪師: AJ-pixiv',                 'https://i.imgur.com/i9BKQpj.jpg'],
            2 :  ['繪師: aono-pixiv',               'https://i.imgur.com/vTNr4Ow.jpg'],
            3 :  ['RANK4霞，繪師: Mauve-pixiv',     'https://i.imgur.com/RY2NT5k.jpg'],
            4 :  ['RANK7霞，繪師: Mauve-pixiv',     'https://i.imgur.com/4rmJYo4.jpg'],
            5 :  ['繪師: みり-pixiv',               'https://i.imgur.com/MFPwEbM.jpg'],
            6 :  ['繪師: ゆりりん-pixiv',           'https://i.imgur.com/xNXb4pA.jpg'],
            7 :  ['繪師: あめ。-pixiv',             'https://i.imgur.com/mSfnH5W.jpg'],
            8 :  ['繪師: 骨カワ-pixiv',             'https://i.imgur.com/cn6i63j.jpg'],
            9 :  ['繪師: あやみゆき-pixiv',         'https://i.imgur.com/FQhW6Iw.jpg'],
            10 : ['繪師: 紫桐シート-pixiv',         'https://i.imgur.com/4zQde23.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message in ['真琴','マコト','安藝真琴','月月','泳裝真琴']:
        value_i = {
            1 :  ['繪師: ヤチモト-pixiv',        'https://i.imgur.com/YTdk5FP.jpg'],
            2 :  ['繪師: S.U.-pixiv',           'https://i.imgur.com/36q2Zwa.jpg'],
            3 :  ['繪師: 大仲いと-pixiv',        'https://i.imgur.com/0craZVx.jpg'],
            4 :  ['繪師: まりぴ-pixiv',          'https://i.imgur.com/nSF7lBr.jpg'],
            5 :  ['繪師: たく庵-pixiv',          'https://i.imgur.com/iZGjsku.jpg'],
            6 :  ['繪師: オウカ-pixiv',          'https://i.imgur.com/05eKQMD.jpg'],
            7 :  ['繪師: イロナツキ-pixiv',      'https://i.imgur.com/cZCALd1.jpg'],
            8 :  ['繪師: 菖蒲-pixiv',            'https://i.imgur.com/TrrZPmM.jpg'],
            9 :  ['繪師: たく庵-pixiv',          'https://i.imgur.com/iBf5yCm.jpg'],
            10 : ['繪師: T.R-pixiv',             'https://i.imgur.com/BKZqUcK.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message in ['香織','カオリ','琉球犬','狗拳','喜屋武香織','一拳超狗','泳裝香織'] :
        value_i = {
            1 :  ['繪師: スギユウ-pixiv',        'https://i.imgur.com/FZIyjVx.jpg',      'https://i.imgur.com/aZiz6j3.jpg'],
            2 :  ['繪師: S.U.-pixiv',           'https://i.imgur.com/WZjeK8G.jpg'],
            3 :  ['繪師: ダーゴ-pixiv',          'https://i.imgur.com/wQa9Lxe.jpg'],
            4 :  ['繪師: PlatiSU-pixiv',        'https://i.imgur.com/qDzfshJ.jpg'],
            5 :  ['繪師: 水無月みず-pixiv',      'https://i.imgur.com/caFCsLp.jpg'],
            6 :  ['繪師: スギユウ-pixiv',        'https://i.imgur.com/8bkYhUV.jpg'],
            7 :  ['繪師: 鎖ノム-pixiv',          'https://i.imgur.com/QPEq9Sd.jpg'],
            8 :  ['繪師: ダーゴ-pixiv',          'https://i.imgur.com/Y4jssR3.jpg'],
            9 :  ['繪師: たく庵-pixiv',          'https://i.imgur.com/nu6whzU.jpg'],
            10 : ['繪師: B-PANG-pixiv',         'https://i.imgur.com/Jg3g95l.jpg']
        }
        if len(value_i[i% len(value_i)+1])==3 :
            line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1]),ImageMessageURL(value_i[i% len(value_i)+1][2])])
        elif len(value_i[i% len(value_i)+1])==2 :
            line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
### 暮光流星群 ###
### トワイライトキャラバン ###
### 暮光流星群 ###
    elif input_message in ['暮光流星群','トワイライトキャラバン']:
        value_i = {
            1 :  ['繪師: ともす-pixiv',         'https://i.imgur.com/zNTr1xq.jpg'],
            2 :  ['繪師: AJ-pixiv',            'https://i.imgur.com/dDVrb23.jpg'],
            3 :  ['繪師: ぐっち庵-pixiv',       'https://i.imgur.com/Y467BCt.jpg'],
            4 :  ['繪師: セーリュー-pixiv',     'https://i.imgur.com/CPf1OMX.jpg'],
            5 :  ['繪師: 天雷-pixiv',          'https://i.imgur.com/Sm9Slhx.jpg'],
            6 :  ['繪師: phobishu-pixiv',      'https://i.imgur.com/KvypMFZ.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message in ['中二','アンナ','杏奈','修特帕魯','疾風之冥姬','泳裝杏奈']:
        value_i = {
            1 :  ['繪師: Sora-pixiv',              'https://i.imgur.com/HA4G2C6.jpg'],
            2 :  ['繪師: ヒーロー-pixiv',           'https://i.imgur.com/ZkSFlQj.jpg'],
            3 :  ['繪師: amaxa-pixiv',             'https://i.imgur.com/GG4vtha.jpg'],
            4 :  ['繪師: しゅーくりいむ-pixiv',     'https://i.imgur.com/n61bHaS.jpg'],
            5 :  ['繪師: しもん-pixiv',            'https://i.imgur.com/P7EI8P1.jpg'],
            6 :  ['繪師: とも-pixiv',              'https://i.imgur.com/BCbLSNq.jpg'],
            7 :  ['繪師: ガンバリーノ-pixiv',       'https://i.imgur.com/l4xW0QX.jpg'],
            8 :  ['繪師: 竹村コウ-pixiv',          'https://i.imgur.com/1oz6l3d.jpg'],
            9 :  ['繪師: レオナート-pixiv',        'https://i.imgur.com/HORyxNH.jpg'],
            10 : ['繪師: ミュー-pixiv',            'https://i.imgur.com/WD6zeRF.jpg'],
            11 : ['繪師: ひとつのなか-pixiv',      'https://i.imgur.com/8MMhoYT.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message in ['流夏','ルカ','太刀洗流夏','大姐頭','流夏姐','泳裝流夏']:
        value_i = {
            1 :  ['繪師: 天雷-pixiv',        'https://i.imgur.com/GMqJfYJ.jpg'],
            2 :  ['繪師: ヒーロー-pixiv',    'https://i.imgur.com/SSuCGN5.jpg'],
            3 :  ['繪師: ヒーロー-pixiv',    'https://i.imgur.com/6ZveKLb.jpg'],
            4 :  ['繪師: sonchi-pixiv',     'https://i.imgur.com/1BQz6Ww.jpg'],
            5 :  ['繪師: けんぴゃっ-pixiv',  'https://i.imgur.com/X03bPbh.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message in ['惠理子','エリコ','病嬌','情人節惠理子']:
        value_i = {
            1 :  ['繪師: [新刊予約中]-pixiv',          'https://i.imgur.com/uRvRgVd.jpg'],
            2 :  ['繪師: こしあん（たいやき）-pixiv',   'https://i.imgur.com/H2H57FL.jpg'],
            3 :  ['繪師: 松倉N-pixiv',                 'https://i.imgur.com/wKhntyZ.jpg'],
            4 :  ['繪師: めひしば-pixiv',              'https://i.imgur.com/dkilTgI.jpg'],
            5 :  ['繪師: 一二三千代子-pixiv',          'https://i.imgur.com/18h4NHn.jpg'],
            6 :  ['繪師: みィむ-pixiv',               'https://i.imgur.com/I7RaZgp.jpg'],
            7 :  ['繪師: ひとつのなか-pixiv',          'https://i.imgur.com/EJobar4.jpg'],
            8 :  ['繪師: Alisia-pixiv',               'https://i.imgur.com/7EmzmG9.jpg'],
            9 :  ['繪師: MISACHU-pixiv',              'https://i.imgur.com/OfL7p6A.jpg'],
            10 : ['繪師: いず-pixiv',                 'https://i.imgur.com/zYcxoKw.jpg'],
            11 : ['繪師: Kinjin-pixiv',               'https://i.imgur.com/PLE4xYE.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message in ['七七香','ナナカ','丹野七七香','收藏家','nnk','眼鏡法','77香','泳裝七七香']:
        value_i = {
            1 :  ['繪師: ぐっち庵-pixiv',    'https://i.imgur.com/mAYPjo6.jpg'],
            2 :  ['繪師: t-pixiv',          'https://i.imgur.com/NpR0ldi.jpg'],
            3 :  ['繪師: ぐっち庵-pixiv',    'https://i.imgur.com/mz2yvzn.jpg'],
            4 :  ['繪師: ☆-pixiv',          'https://i.imgur.com/Zi9h7ao.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message in ['深月','ミツキ','宵濱深月','獨眼惡魔','藥劑師']:
        value_i = {
            1 :  ['繪師: @orange_mix7-twitter',    'https://i.imgur.com/D7PTeVz.jpg'],
            2 :  ['繪師: 関西ジン-pixiv',           'https://i.imgur.com/IZCAmHv.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
### 慈樂之音 ###
### 偶像團 ###
### カルミナ ###
    elif input_message in ['慈樂之音','偶像團','カルミナ']:
        value_i = {
            1 :  ['繪師: しぇるてぃー-pixiv',    'https://i.imgur.com/jdMLi5b.jpg'],
            2 :  ['繪師: AJ-pixiv',             'https://i.imgur.com/mBRquki.jpg'],
            3 :  ['繪師: Sora-pixiv',           'https://i.imgur.com/z6zzyTr.jpg'],
            4 :  ['繪師: カツラギ-pixiv',        'https://i.imgur.com/gijrjyq.jpg'],
            5 :  ['繪師: カツラギ-pixiv',        'https://i.imgur.com/ySfq705.jpg'],
            6 :  ['繪師: カツラギ-pixiv',        'https://i.imgur.com/lYlhSEd.jpg'],
            7 :  ['繪師: 天雷-pixiv',            'https://i.imgur.com/gHOXVVH.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message in ['紡希','ツムギ','繭宮紡希']:
        value_i = {
            1 :  ['繪師: ひとつのなか-pixiv',   'https://i.imgur.com/Lhk5Uxh.jpg'],
            2 :  ['繪師: ひとつのなか-pixiv',   'https://i.imgur.com/IzjQvLH.jpg'],
            3 :  ['繪師: 竹村コウ-pixiv',       'https://i.imgur.com/b6xncld.jpg'],
            4 :  ['繪師: むぐら-pixiv',         'https://i.imgur.com/54XO9cK.jpg'],
            5 :  ['繪師: むぐら-pixiv',         'https://i.imgur.com/3VvuAmV.jpg'],
            6 :  ['繪師: カツラギ-pixiv',       'https://i.imgur.com/vvtliTH.jpg'],
            7 :  ['繪師: 竹村コウ-pixiv',       'https://i.imgur.com/k34TQEO.jpg'],
            8 :  ['繪師: むぐら-pixiv',         'https://i.imgur.com/9mzwRdQ.jpg'],
            9 :  ['繪師: ダーゴ-pixiv',         'https://i.imgur.com/AhkLOWp.png'],
            10 : ['繪師: むぐら-pixiv',         'https://i.imgur.com/zclpp4e.jpg'],
            11 : ['繪師: 桜庭ロイヤル-pixiv',    'https://i.imgur.com/n5sgyPI.jpg'],
            12 : ['繪師: ひとつのなか-pixiv',    'https://i.imgur.com/Pp3lTbh.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message in ['千歌','聖千','チカ','聖歌','聖誕千歌']:
        value_i = {
            1 :  ['繪師: Sora-pixiv',           'https://i.imgur.com/2pOtito.png'],
            2 :  ['繪師: 桜庭ロイヤル-pixiv',    'https://i.imgur.com/rOJ2zmG.png'],
            3 :  ['繪師: 猫小渣-pixiv',         'https://i.imgur.com/obBJN0Q.jpg'],
            4 :  ['繪師: いとね-pixiv',         'https://i.imgur.com/gUsae4d.jpg'],
            5 :  ['繪師: 桜庭ロイヤル-pixiv',    'https://i.imgur.com/w1CzOB3.jpg'],
            6 :  ['繪師: 天雷-pixiv',           'https://i.imgur.com/mQ8PXf3.png',    'https://i.imgur.com/JQGTauO.png'],
            7 :  ['繪師: 天雷-pixiv',           'https://i.imgur.com/URkST7E.png']
        }
        if(len(value_i[i% len(value_i)+1])==3):
            line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1]),ImageMessageURL(value_i[i% len(value_i)+1][2])])
        elif(len(value_i[i% len(value_i)+1])==2):
            line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message in ['小望','望','ノゾミ','偶像','櫻井望','公車','公車望','聖誕小望']:
        value_i = {
            1 :  ['繪師: 天雷-pixiv',           'https://i.imgur.com/psEsocd.jpg'],
            2 :  ['繪師: 桜庭ロイヤル-pixiv',   'https://i.imgur.com/XTyOttf.jpg'],
            3 :  ['繪師: Mauve-pixiv',         'https://i.imgur.com/ACYRXh2.jpg'],
            4 :  ['繪師: RYUKI-pixiv',         'https://i.imgur.com/0KGM43S.jpg'],
            5 :  ['繪師: むぐら-pixiv',         'https://i.imgur.com/uAXCp1U.jpg'],
            6 :  ['繪師: カツラギ-pixiv',       'https://i.imgur.com/7cjV2Aq.jpg'],
            7 :  ['繪師: カツラギ-pixiv',       'https://i.imgur.com/pSSieQv.png'],
            8 :  ['繪師: 天雷-pixiv',           'https://i.imgur.com/7sikqLO.png',    'https://i.imgur.com/woTEPVS.png'],
            9 :  ['繪師: 天雷-pixiv',           'https://i.imgur.com/U1CkoZa.png',    'https://i.imgur.com/CW93OzQ.png'],
            10 : ['繪師: 天雷-pixiv',           'https://i.imgur.com/oNEwPwd.png']
        }
        if(len(value_i[i% len(value_i)+1])==3):
            line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1]),ImageMessageURL(value_i[i% len(value_i)+1][2])])
        elif(len(value_i[i% len(value_i)+1])==2):
            line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
### Diabolos ###
### 惡魔偽王國軍 ###
### ディアボロス ###
    elif input_message in ['惡魔偽王國軍','ディアボロス','Diabolos']:
        value_i = {
            1 :  ['繪師: WaterRing-pixiv',    'https://i.imgur.com/rvhkokt.jpg'],
            2 :  ['繪師: AJ-pixiv',           'https://i.imgur.com/YzifEB8.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message in ['茜里','妹法','アカネ','雙子','惡魔雙子','雙子惡魔']:
        value_i = {
            1 :  ['繪師: ROIN-pixiv',       'https://i.imgur.com/r3yBD71.jpg'],
            2 :  ['繪師: ヤンタロウ-pixiv',  'https://i.imgur.com/QaAUaca.jpg'],
            3 :  ['繪師: 六丸いなみ-pixiv',  'https://i.imgur.com/4BqqYmI.jpg'],
            4 :  ['繪師: Chel-pixiv',       'https://i.imgur.com/vy9LI9P.jpg'],
            5 :  ['繪師: ダーゴ-pixiv',      'https://i.imgur.com/BCdFbsb.jpg'],
            6 :  ['繪師: Alpha-pixiv',      'https://i.imgur.com/00EaNly.jpg'],
            7 :  ['繪師: ヒシ馬-pixiv',      'https://i.imgur.com/m0wqkKG.jpg'],
            8 :  ['繪師: RYUKI-pixiv',      'https://i.imgur.com/cTrVg8W.jpg'],
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message in ['依里','ヨリ','姐法','姊法']:
        value_i = {
            1 :  ['繪師: 桜木ゆうき-pixiv',         'https://i.imgur.com/rKMZZ9p.jpg'],
            2 :  ['繪師: せら少佐-pixiv',           'https://i.imgur.com/qFyyK0f.jpg'],
            3 :  ['繪師: せら少佐-pixiv',           'https://i.imgur.com/LqJJ3Wl.jpg'],
            4 :  ['繪師: 水無川レイ-pixiv',         'https://i.imgur.com/DxmFDs2.jpg'],
            5 :  ['繪師: 雪-pixiv',                'https://i.imgur.com/yAIAyq6.jpg'],
            6 :  ['繪師: @diotheworld78-twitter',  'https://i.imgur.com/S9F6Bdi.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message in ['台女','布丁','ミヤコ','宮子','幽靈','子宮','萬聖宮子']:
        value_i = {
            1 :  ['https://i.imgur.com/czGSi5r.jpg'],
            2 :  ['https://i.imgur.com/T6GdEjS.jpg'],
            3 :  ['https://i.imgur.com/FlMnRvL.jpg'],
            4 :  ['https://i.imgur.com/lBrFXU2.jpg'],
            5 :  ['繪師: ダーゴ-pixiv',         'https://i.imgur.com/urboS8A.jpg'],
            6 :  ['https://i.imgur.com/2y4LEhM.jpg'],
            7 :  ['https://i.imgur.com/pHNzeHo.jpg'],
            8 :  ['繪師: じゅんまぁち。-pixiv',  'https://i.imgur.com/ZhQRQWX.jpg'],
            9 :  ['繪師: とゆり-pixiv',         'https://i.imgur.com/UBj2jpk.jpg'],
            10 : ['繪師: Saiste-pixiv',        'https://i.imgur.com/g8LGcjz.jpg'],
            11 : ['繪師: LUNIA-pixiv',         'https://i.imgur.com/1weUved.jpg'],
            12 : ['繪師: Tama-pixiv',          'https://i.imgur.com/BTpk9Yq.jpg',      'https://i.imgur.com/Vrh7bAy.jpg'],
            13 : ['繪師: ぬるぷよ-pixiv',       'https://i.imgur.com/wiuzd3A.jpg'],
            14 : ['繪師: 浣狸-pixiv',          'https://i.imgur.com/Jk5rN3V.jpg'],
            15 : ['繪師: ジヤス-pixiv',        'https://i.imgur.com/bxSfwej.jpg'],
            16 : ['繪師: ヒシ馬-pixiv',        'https://i.imgur.com/0KKeRJ9.jpg']
        }
        if(len(value_i[i% len(value_i)+1])==3):
            line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1]),ImageMessageURL(value_i[i% len(value_i)+1][2])])
        elif(len(value_i[i% len(value_i)+1])==2):
            line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
        elif(len(value_i[i% len(value_i)+1])==1):
            line_bot_api.reply_message(event.reply_token,ImageMessageURL(value_i[i% len(value_i)+1][0]))
    elif input_message in ['忍','シノブ','鬼父','上喜忍','骷髏老爸','萬聖忍']:
        value_i = {
            1 :  ['繪師: Chel-pixiv',       'https://i.imgur.com/Ecyy4Lo.jpg'],
            2 :  ['繪師: オウカ-pixiv',     'https://i.imgur.com/HsqExFk.jpg'],
            3 :  ['繪師: あいち志保-pixiv',  'https://i.imgur.com/Uuh1OmA.jpg'],
            4 :  ['繪師: けんせい-pixiv',    'https://i.imgur.com/t8KXMFH.jpg'],
            5 :  ['繪師: Melings-pixiv',    'https://i.imgur.com/vlKcKzf.jpg'],
            6 :  ['繪師: WaterRing-pixiv',  'https://i.imgur.com/xsA6n4v.jpg'],
            7 :  ['繪師: 菖蒲-pixiv',       'https://i.imgur.com/L9xOGr6.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message in ['伊莉亞','イリヤ','吸血鬼','自爆','伊莉亞·奧恩斯坦','聖誕伊莉亞']:
        value_i = {
            1 :  ['繪師: ハロン-pixiv',       'https://i.imgur.com/uoCNST9.jpg'],
            2 :  ['繪師: 月満懐空-pixiv',     'https://i.imgur.com/JrgtzcM.jpg'],
            3 :  ['繪師: HaneRu-pixiv',      'https://i.imgur.com/louJwWr.jpg'],
            4 :  ['繪師: sonchi-pixiv',      'https://i.imgur.com/LNc1gxP.jpg'],
            5 :  ['繪師: ごましを-pixiv',     'https://i.imgur.com/Y9KyKfW.jpg'],
            6 :  ['繪師: SeeUmai-pixiv',     'https://i.imgur.com/M3U1cp9.jpg'],
            7 :  ['繪師: ウエハラ蜂-pixiv',   'https://i.imgur.com/fUSYDa9.jpg'],
            8 :  ['繪師: ROIN-pixiv',        'https://i.imgur.com/Ae3iVBz.jpg'],
            9 :  ['繪師: まぉー。-pixiv',     'https://i.imgur.com/VjL6hUw.jpg'],
            10 : ['繪師: ぬるぷよ-pixiv',     'https://i.imgur.com/geVaLcE.jpg'],
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
### 破曉之星 ###
### トゥインクルウィッシュ ###
### 破曉之星 ###
    elif input_message in ['破曉之星','トゥインクルウィッシュ']:
        value_i = {
            1 :  ['繪師: AJ-pixiv',         'https://i.imgur.com/sOsPvma.png'],
            2 :  ['繪師: ﾘﾝ-pixiv',         'https://i.imgur.com/OSl2Oxy.jpg'],
            3 :  ['繪師: ゆずゆい-pixiv',    'https://i.imgur.com/ajaKb2s.jpg'],
            4 :  ['繪師: セーリュー-pixiv',  'https://i.imgur.com/R7Fm78o.jpg'],
            5 :  ['繪師: ﾘﾝ-pixiv',         'https://i.imgur.com/aOq9p3O.jpg'],
            6 :  ['繪師: だしごはん-pixiv',  'https://i.imgur.com/0CuWj4w.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message in ['優衣','ユイ','草野優衣','ue','UE','公主優衣','正月優衣']:
        value_i = {
            1 :  "https://i.imgur.com/vbyBSHq.jpg",
            2 :  "https://i.imgur.com/GnNlRFB.jpg",
            3 :  "https://i.imgur.com/QZSMdBh.jpg",
            4 :  "https://i.imgur.com/fr1fgLH.jpg",
            5 :  ['繪師: @Renian_-twitter',                'https://i.imgur.com/VYT9zWL.jpg'],
            6 :  ['繪師: 狼巴子原型机-pixiv',               'https://i.imgur.com/GnPmRql.jpg'],
            7 :  ['繪師: Itoichi-pixiv',                   'https://i.imgur.com/hQAJHCM.jpg'],
            8 :  ['繪師: 佐倉のび太-pixiv',                 'https://i.imgur.com/5Og2eiV.jpg'],
            9 :  ['繪師: どうたぬき＋3-pixiv',              'https://i.imgur.com/HaQCAZj.jpg'],
            10 : ['繪師: ゆりりん-pixiv',                   'https://i.imgur.com/KkmJwCP.jpg'],
            11 : ['繪師: HIROKAZU-pixiv',                   'https://i.imgur.com/taTPJjm.jpg'],
            12 : ['繪師: HIROKAZU-pixiv',                   'https://i.imgur.com/gYi5WRV.jpg'],
            13 : ['繪師: HIROKAZU-pixiv',                   'https://i.imgur.com/HYUSfq6.jpg'],
            14 : ['繪師: HIROKAZU-pixiv',                   'https://i.imgur.com/p3KsySu.jpg'],
            15 : ['繪師: HIROKAZU-pixiv',                   'https://i.imgur.com/JJsKQCY.jpg'],
            16 : ['繪師: HIROKAZU-pixiv',                   'https://i.imgur.com/6iBeNJE.jpg'],
            17 : ['繪師: HIROKAZU-pixiv',                   'https://i.imgur.com/N92Z60L.jpg'],
            18 : ['繪師: とも-pixiv',                       'https://i.imgur.com/dD8yXeo.jpg'],
            19 : ['為什麼，明明是初次見面\n我的心卻如此苦澀',  'https://i.imgur.com/x1Ggdnw.jpg'],
            20 : ['繪師: @shucream7777-twitter',            'https://i.imgur.com/KU2QcRe.jpg'],
            21 : ['繪師: 天雷-pixiv',                       'https://i.imgur.com/G3VKdFY.png'],
            22 : ['繪師: じゅんまぁち。-pixiv',              'https://i.imgur.com/jpSaEf6.png'],
            23 : ['繪師: たまかが-pixiv',                    'https://i.imgur.com/TEaqose.png']
        }
        if(len(value_i[i% len(value_i)+1])==2): 
            line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
        else:
            line_bot_api.reply_message(event.reply_token,ImageMessageURL(value_i[i% len(value_i)+1]))
    elif input_message in ['日和','ヒヨリ','春咲日和','貓拳','正月日和']:
        value_i = {
            1 :  ['繪師: 薬草-pixiv',        'https://i.imgur.com/rqoos26.jpg'],
            2 :  ['繪師: けんぴゃっ-pixiv',  'https://i.imgur.com/jyI0Ab7.jpg'],
            3 :  ['繪師: K-y-pixiv',        'https://i.imgur.com/qGar6FW.jpg'],
            4 :  ['繪師: 終わらない-pixiv',  'https://i.imgur.com/LsMnoio.jpg'],
            5 :  ['繪師: まぉー。-pixiv',    'https://i.imgur.com/pGJJoVW.jpg',     'https://i.imgur.com/lQrWmEE.jpg'],
            6 :  ['繪師: 天雷-pixiv',        'https://i.imgur.com/8Z1ruEc.png'],
            7 :  ['繪師: ダーゴ-pixiv',      'https://i.imgur.com/XqQEiS9.png']
        }
        if(len(value_i[i% len(value_i)+1])==2): 
            line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
        elif(len(value_i[i% len(value_i)+1])==3):
            line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1]),ImageMessageURL(value_i[i% len(value_i)+1][2])])
    elif input_message in ['怜','レイ','士條怜','怜大人','正月怜']:
        value_i = {
            1 :  ['繪師: 天雷-pixiv',           'https://i.imgur.com/Kx01yVD.png'],
            2 :  ['繪師: ペヤンキー-pixiv',     'https://i.imgur.com/ECzvAdL.jpg'],
            3 :  ['繪師: 四字熟語-pixiv',       'https://i.imgur.com/4bheK7u.jpg'],
            4 :  ['繪師: 四字熟語-pixiv',       'https://i.imgur.com/CsStf0f.jpg'],
            5 :  ['繪師: 四字熟語-pixiv',       'https://i.imgur.com/v5xplKt.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message in ['對不起'] or ('對不起' in input_message or 'ごめん' in input_message or 'ntr' in input_message)and('優衣' in input_message or 'ユイ' in input_message or 'UE' in input_message or 'ue' in input_message or '優依' in input_message ):
        value_i = {
            1 :  ['https://i.imgur.com/9pX6RP9.jpg',    '春咲日和同學...\n本來我還把你當作朋友的，但就算明天你就要死了，我也不會再去救你的'],
            2 :  ['https://i.imgur.com/aNZsoIo.jpg',    '恩，我會守護好騎士君不讓害蟲靠近的'],
            3 :  ['https://i.imgur.com/qALShyp.jpg',    '沒關係的，騎士君也希望我選擇原諒的吧 (舉槍~'],
            4 :  ['https://i.imgur.com/kMY3H09.jpg',    '迫害優衣的繪師twitter: @yumeoi1884'],
            5 :  ['https://i.imgur.com/QRAX6tt.jpg',    '糟蹋優衣的繪師: 翔たろう-pixiv'],
            6 :  ['https://i.imgur.com/oR7M58R.jpg',    '欺凌優衣的繪師: ないん-pixiv']
        }
        line_bot_api.reply_message(event.reply_token,[ImageMessageURL(value_i[i% len(value_i)+1][0]),TextSendMessage(text= value_i[i% len(value_i)+1][1])])
### 小小甜心 ###
### リトルリリカル ###
### 小小甜心 ###
    elif input_message in ['小小甜心','リトルリリカル','27歲']:
        value_i = {
            1 :  ['繪師: 鈴音れな-pixiv',      'https://i.imgur.com/aj1YCpG.jpg'],
            2 :  ['繪師: けんぴゃっ-pixiv',    'https://i.imgur.com/hl1DEJ2.jpg'],
            3 :  ['繪師: ひづき夜宵-pixiv',    'https://i.imgur.com/jCF6U7G.jpg'],
            4 :  ['繪師: てれん-pixiv',        'https://i.imgur.com/6Wzr3NT.jpg'],
            5 :  ['繪師: 音琶-pixiv',          'https://i.imgur.com/vtATPer.jpg'],
            6 :  ['繪師: たかつ-pixiv',        'https://i.imgur.com/03vHTgr.jpg'],
            7 :  ['繪師: 日下氏-pixiv',        'https://i.imgur.com/2IFsEOD.jpg'],
            8 :  ['繪師: 関西ジン-pixiv',      'https://i.imgur.com/nbfL5h2.jpg'],
            9 :  ['繪師: ねむいひと-pixiv',    'https://i.imgur.com/Ig53ubp.jpg'],
            10 : ['繪師: u_U-pixiv',          'https://i.imgur.com/C3O8gts.jpg'],
            11 : ['繪師: anno-pixiv',         'https://i.imgur.com/kSCbzaD.jpg'],
            12 : ['繪師: 結城辰也-pixiv',      'https://i.imgur.com/q3G8QlE.jpg'],
            13 : ['繪師: みどりのちゃ-pixiv',  'https://i.imgur.com/hoFZQxH.jpg'],
            14 : ['繪師: なつめえり-pixiv',    'https://i.imgur.com/Q7eQ5yq.jpg']
        }
        if(len(value_i[i% len(value_i)+1])==2): 
            line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
        else:
            line_bot_api.reply_message(event.reply_token,ImageMessageURL(value_i[i% len(value_i)+1]))
    elif input_message in ['8歲','八歲','キョウカ','冰川鏡華','鏡華','噴水蘿','鏡華媽媽','小倉唯' ,'傲嬌蘿','萬聖鏡華'] :
        value_i = {
            1 :  'https://i.imgur.com/t9OWzlK.jpg',
            2 :  'https://i.imgur.com/WyVngW7.jpg', 
            3 :  'https://i.imgur.com/Xkj3sZB.jpg',
            4 :  ['繪師: うめた-pixiv',                  'https://i.imgur.com/762cQ5O.jpg'],
            5 :  ['繪師: @kazukiadumi-twitter',          'https://i.imgur.com/nkQhkYF.jpg'],
            6 :  ['繪師: 真崎ケイ-pixiv',                'https://i.imgur.com/xhAOxG0.jpg'],
            7 :  ['繪師: @koma_momozu-twitter',         'https://i.imgur.com/Hrcg9ej.jpg'],
            8 :  ['繪師: @ryukisukune-twitter',         'https://i.imgur.com/yfLLbF7.jpg'],
            9 :  ['繪師: @usagicandy_taku-twitter',     'https://i.imgur.com/sdnjww4.jpg'],
            10 : ['繪師: 真崎ケイ-pixiv',                'https://i.imgur.com/yx7vql2.jpg'],
            11 : ['繪師: ROIN-pixiv',                   'https://i.imgur.com/LeNI4fi.jpg'],
            12 : ['繪師: ほにゃる-pixiv',                'https://i.imgur.com/2bxofr2.jpg'],
            13 : ['繪師: 天雷-pixiv',                    'https://i.imgur.com/2ijIX5l.jpg'],
            14 : ['繪師: ひづき夜宵-pixiv',              'https://i.imgur.com/GFA4wh4.jpg']
        }
        if(len(value_i[i% len(value_i)+1])==2): 
            line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
        else:
            line_bot_api.reply_message(event.reply_token,ImageMessageURL(value_i[i% len(value_i)+1]))
    elif input_message in ['美美','ミミ','茜美美','兔子','天兔霸斷劍','人參霸斷劍','萬聖美美']:
        value_i = {
            1 :  ['繪師: @PoLa1021_-twitter',  'https://i.imgur.com/SDdCPdd.jpg'],
            2 :  ['繪師: Chanifge-pixiv',      'https://i.imgur.com/f0YQOlU.jpg'],
            3 :  ['繪師: えぴ-pixiv',          'https://i.imgur.com/I45pDDB.jpg'],
            4 :  ['繪師: えぴ-pixiv',          'https://i.imgur.com/PzGh7bS.jpg'],
            5 :  ['繪師: u_U-pixiv',           'https://i.imgur.com/Pws5qXb.jpg'],
            6 :  ['繪師: Azel司令官-pixiv',    'https://i.imgur.com/Q8A9XBD.jpg'],
            7 :  ['繪師: rokico-pixiv',        'https://i.imgur.com/m9MEYQU.jpg'],
            8 :  ['繪師: rokico-pixiv',        'https://i.imgur.com/ux4WWXp.jpg'],
            9 :  ['繪師: PTD-pixiv',           'https://i.imgur.com/2pbrdSi.jpg'],
            10 : ['繪師: ジヤス-pixiv',         'https://i.imgur.com/jZ6lkdk.jpg'],
            11 : ['繪師: u_U-pixiv',           'https://i.imgur.com/cYYGLEg.jpg'],
            12 : ['繪師: u_U-pixiv',           'https://i.imgur.com/LtqyIUC.jpg'],
            13 : ['繪師: rokico-pixiv',        'https://i.imgur.com/zbscNBC.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message in ['禊','ミソギ','穗高禊','炸彈','屁孩','惡作劇','萬聖禊']:
        value_i = {
            1 :  ['繪師: さくも-pixiv',        'https://i.imgur.com/sQdHme7.jpg'],
            2 :  ['繪師: 秋鳩むぎ-pixiv',      'https://i.imgur.com/3kvw53A.jpg'],
            3 :  ['繪師: とも-pixiv',          'https://i.imgur.com/plAbio1.jpg'],
            4 :  ['繪師: とも-pixiv',          'https://i.imgur.com/Nd8jVpX.jpg'],
            5 :  ['繪師: レオナート-pixiv',    'https://i.imgur.com/zKa4Av9.jpg'],
            6 :  ['繪師: aono-pixiv',         'https://i.imgur.com/JQ5s2RI.jpg'],
            7 :  ['繪師: レオナート-pixiv',    'https://i.imgur.com/8OlaltN.jpg'],
            8 :  ['繪師: たかつ-pixiv',        'https://i.imgur.com/SDe1vYT.jpg'],
            9 :  ['繪師: rokico-pixiv',       'https://i.imgur.com/NX02QeB.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif  input_message in ['蘿莉','五等分的蘿莉','五等分的花嫁'] :
        value_i = {
            1 : "https://i.imgur.com/31NBFBl.png",   
            2 : "https://i.imgur.com/ZYYiagm.jpg",
            3 : ["繪師: たかつ-pixiv",      "https://i.imgur.com/5pojuIY.jpg"]
        }
        if(len(value_i[i% len(value_i)+1])==2): 
            line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
        else:
            line_bot_api.reply_message(event.reply_token,ImageMessageURL(value_i[i% len(value_i)+1]))
### 優妮們 ###
### 好朋友社 ###
### なかよし部 ###
    elif input_message in ['優妮們','好朋友社','なかよし部','好朋友部']:
        value_i = {
            1 :  ['繪師: 谷川犬兎-pixiv',       'https://i.imgur.com/tNSLFAv.jpg'],
            2 :  ['繪師: 谷川犬兎-pixiv',       'https://i.imgur.com/g8peBoI.jpg'],
            3 :  ['繪師: アイダ-pixiv',         'https://i.imgur.com/Y8b9KpL.jpg'],
            4 :  ['繪師: カッシュ-pixiv',       'https://i.imgur.com/o5bjJkO.jpg'],
            5 :  ['繪師: やま兎-pixiv',         'https://i.imgur.com/iChYvja.jpg'],
            6 :  ['繪師: 竹四兎-pixiv',         'https://i.imgur.com/XW6Ilhi.jpg'],
            7 :  ['繪師: ヒーロー-pixiv',       'https://i.imgur.com/18Wr2SL.jpg'],
            8 :  ['繪師: ヒーロー-pixiv',       'https://i.imgur.com/6H3N2oi.jpg'],
            9 :  ['繪師: みどりのちゃ-pixiv',   'https://i.imgur.com/rORyTAo.jpg'],
            10 : ['繪師: RYUKI-pixiv',         'https://i.imgur.com/vW28Kah.jpg'],
            11 : ['繪師: RYUKI-pixiv',         'https://i.imgur.com/7gQ2mvE.jpg'],
            12 : ['繪師: 夢追人形-pixiv',       'https://i.imgur.com/kKqICUL.jpg'],
            13 : ['繪師: @zuhonyanko-twitter', 'https://i.imgur.com/fOGFnLj.jpg'],
            14 : ['繪師: AJ-pixiv',            'https://i.imgur.com/q3rH2Nh.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message in ['優妮','優尼','ユニ','優妮先輩','優妮學姊','真行寺由仁'] :
        value_i = {
            1 :  ['繪師: 7010-pixiv',               'https://i.imgur.com/PgefTbO.jpg',      'https://i.imgur.com/Dd3cm46.jpg'],
            2 :  ['繪師: @augment_girl-twitter',    'https://i.imgur.com/pvC5roc.jpg'],
            3 :  ['繪師: もつ煮-pixiv',             'https://i.imgur.com/vqYJWmP.jpg'],
            4 :  ['繪師: SeeRo-pixiv',              'https://i.imgur.com/qW0whyw.jpg'],
            5 :  ['繪師: オウカ-pixiv',             'https://i.imgur.com/bayYULx.jpg'],
            6 :  ['繪師: かのら-pixiv',             'https://i.imgur.com/8enbxjq.jpg'],
            7 :  ['繪師: SeeUmai-pixiv',            'https://i.imgur.com/2KUXbMb.jpg'],
            8 :  ['繪師: ばくP-pixiv',              'https://i.imgur.com/oRKXEqB.jpg'],
            9 :  ['繪師: ヒーロー-pixiv',           'https://i.imgur.com/qGunDiI.jpg'],
            10 : ['繪師: うしむ-pixiv',             'https://i.imgur.com/y9rMskm.jpg'],
            11 : ['繪師: @Nabyssor-twitter',        'https://i.imgur.com/JkdzOu5.jpg'],
            12 : ['https://i.imgur.com/we20ZAK.jpg'],
            13 : ['繪師: ジヤス-pixiv',             'https://i.imgur.com/yxUVHJp.jpg'],
        }
        if len(value_i[i% len(value_i)+1])==3 :
            line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1]),ImageMessageURL(value_i[i% len(value_i)+1][2])])
        elif len(value_i[i% len(value_i)+1])==2 :
            line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
        elif len(value_i[i% len(value_i)+1])==1 :
            line_bot_api.reply_message(event.reply_token,ImageMessageURL(value_i[i% len(value_i)+1][0]))
    elif input_message in ['克蘿依','黑江花子','クロエ','華哥','不良','B80']:
        value_i = {
            1 :  ['繪師: 92M-pixiv',            'https://i.imgur.com/XpHrtHx.jpg'],
            2 :  ['繪師: むらさめしん-pixiv',    'https://i.imgur.com/2XBnrXb.jpg'],
            3 :  ['繪師: あめ。-pixiv',         'https://i.imgur.com/iJLxVtr.jpg'],
            4 :  ['繪師: あめ。-pixiv',         'https://i.imgur.com/WJtF51h.jpg'],
            5 :  ['繪師: ねこ鳴都-pixiv',       'https://i.imgur.com/QwjcxRH.jpg'],
            6 :  ['繪師: あめ。-pixiv',         'https://i.imgur.com/GKbJNJ0.jpg'],
            7 :  ['繪師: 飛蝗-pixiv',           'https://i.imgur.com/qV6FfSV.jpg'],
            8 :  ['繪師: やま兎-pixiv',         'https://i.imgur.com/B8ibPoy.jpg'],
            9 :  ['繪師: 鉄人桃子-pixiv',       'https://i.imgur.com/CzUXDYU.jpg'],
            10 : ['繪師: ROIN-pixiv',          'https://i.imgur.com/VGBkgS2.jpg'],
            11 : ['繪師: ヒーロー-pixiv',       'https://i.imgur.com/qHRmLHL.jpg'],
            12 : ['繪師: ROIN-pixiv',          'https://i.imgur.com/8onaczp.jpg'],
            13 : ['繪師: やま兎-pixiv',         'https://i.imgur.com/dathr2M.jpg'],
            14 : ['繪師: AJ-pixiv',            'https://i.imgur.com/ITDNtcZ.jpg'],
            15 : ['繪師: まだら-pixiv',        'https://i.imgur.com/GVxFuSd.jpg'],
            16 : ['繪師: あめ。-pixiv',        'https://i.imgur.com/9yby12s.jpg'],
            17 : ['繪師: HIROKAZU-pixiv',     'https://i.imgur.com/z042FKZ.png']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message in ['琪愛兒','風間千惠瑠','チエル','切嚕','ちぇるーん']:
        value_i = {
            1 :  ['繪師: Kobi-pixiv',           'https://i.imgur.com/2XHfz4W.jpg'],
            2 :  ['繪師: るがつき-pixiv',        'https://i.imgur.com/qqEU0LG.jpg'],
            3 :  ['繪師: 玉蒔良-pixiv',          'https://i.imgur.com/YCMAVRl.jpg'],
            4 :  ['繪師: AJ-pixiv',             'https://i.imgur.com/ZiUEWJ6.jpg'],
            5 :  ['繪師: カツラギ-pixiv',        'https://i.imgur.com/OgvJcSV.jpg'],
            6 :  ['繪師: @momozizizi-twitter',  'https://i.imgur.com/KDYBz2m.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message == '空有無用知識的戀母情結小矮子':
        value_i = {
            1 : ['https://i.imgur.com/noYjwsL.jpg'],
            2 : ['繪師: RYUKI-pixiv',       'https://i.imgur.com/PJLI6TF.jpg'],
            3 : ['繪師: 理紅-pixiv',        'https://i.imgur.com/0Ai4zso.jpg']
        }
        if len(value_i[i% len(value_i)+1])==2 :
            line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
        elif len(value_i[i% len(value_i)+1])==1 :
            line_bot_api.reply_message(event.reply_token,ImageMessageURL(value_i[i% len(value_i)+1][0]))
### 龍族巢穴 ###
### ドラゴンズネスト ###
### 龍族巢穴 ###
    elif input_message in ['龍族巢穴','ドラゴンズネスト']:
        value_i = {
            1 :  ['繪師: やま兎-pixiv',     'https://i.imgur.com/ap4y30N.jpg'],
            2 :  ['繪師: 関西ジン-pixiv',   'https://i.imgur.com/Y7UyJg8.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message in ['帆稀','ホマレ']:
        value_i = {
            1 :  ['繪師: 六丸いなみ-pixiv',     'https://i.imgur.com/hhtu7FX.jpg'],
            2 :  ['繪師: 六丸いなみ-pixiv',     'https://i.imgur.com/ogQAyCh.jpg'],
            3 :  ['繪師: うね-pixiv',          'https://i.imgur.com/IgoBITE.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message in ['嘉夜','カヤ','鬼道嘉夜','卡雅','龍拳']:
        value_i = {
            1 :  ['繪師: ヒーロー-pixiv',        'https://i.imgur.com/FWw5JLj.jpg'],
            2 :  ['繪師: やま兎。-pixiv',        'https://i.imgur.com/HcDAD8a.jpg'],
            3 :  ['繪師: しもん-pixiv',          'https://i.imgur.com/ZWhYldI.jpg'],
            4 :  ['繪師: Miyamoya-pixiv',       'https://i.imgur.com/9I8paC4.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message in ['祈梨','イノリ','一之瀨祈梨','祈','龍錘']:
        value_i = {
            1 :  ['繪師: こしあん-pixiv',   'https://i.imgur.com/5ZQ0r6b.jpg'],
            2 :  ['繪師: 竹村コウ-pixiv',   'https://i.imgur.com/zU2H4Pf.jpg'],
            3 :  ['繪師: ナナ稲-pixiv',     'https://i.imgur.com/wzT1Orh.jpg'],
            4 :  ['繪師: 黒羽UMA-pixiv',    'https://i.imgur.com/F4sAEzZ.jpg'],
            5 :  ['繪師: すなねこ-pixiv',   'https://i.imgur.com/qyZmeHC.jpg'],
            6 :  ['繪師: こしあん-pixiv',   'https://i.imgur.com/Rrj5sTL.jpg',      'https://i.imgur.com/ukv934D.jpg']
        }
        if(len(value_i[i% len(value_i)+1])==3):
            line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1]),ImageMessageURL(value_i[i% len(value_i)+1][2])])
        elif(len(value_i[i% len(value_i)+1])==2):
            line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
### 王宮騎士團 ###
### 騎士團 ###
### 王宮騎士団 ###
    elif input_message in ['王宮騎士團','騎士團','王宮騎士団']:
        value_i = {
            1 :  ['繪師: 六丸いなみ-pixiv',    'https://i.imgur.com/0IVEQIG.jpg'],
            2 :  ['繪師: 菖蒲-pixiv',         'https://i.imgur.com/lOPI6vv.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message in ['純','黑騎','ジュン','白銀純','黑Saber','泳裝純']:
        value_i = {
            1 :  ['繪師: 六丸いなみ-pixiv',    'https://i.imgur.com/2U9tece.jpg'],
            2 :  ['繪師: MoQi-pixiv',         'https://i.imgur.com/oVgUVJR.jpg'],
            3 :  ['繪師: KMH-pixiv',          'https://i.imgur.com/IHKGTp6.jpg'],
            4 :  ['繪師: Tahnya-pixiv',       'https://i.imgur.com/lQbq5uu.jpg'],
            5 :  ['繪師: 六丸いなみ-pixiv',    'https://i.imgur.com/6sN2xaO.jpg'],
            6 :  ['繪師: 六丸いなみ-pixiv',    'https://i.imgur.com/c0YaxWB.jpg'],
            7 :  ['繪師: 六丸いなみ-pixiv',    'https://i.imgur.com/7sgNSyO.jpg'],
            8 :  ['繪師: オウカ-pixiv',        'https://i.imgur.com/8lGFqFp.jpg'],
            9 :  ['繪師: ともす-pixiv',        'https://i.imgur.com/rddL812.jpg'],
            10 : ['繪師: 天雷-pixiv',          'https://i.imgur.com/e9Zsajf.jpg',   'https://i.imgur.com/uYd8OXO.jpg'],
            11 : ['繪師: 天雷-pixiv',          'https://i.imgur.com/7gs7vwg.jpg']
        }
        if(len(value_i[i% len(value_i)+1])==3):
            line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1]),ImageMessageURL(value_i[i% len(value_i)+1][2])])
        elif(len(value_i[i% len(value_i)+1])==2):
            line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message in ['智','トモ','御久間智','卜毛','禿毛']:
        value_i = {
            1 : ['繪師: ゆんみ-pixiv',       'https://i.imgur.com/zT8PM2v.jpg'],
            2 : ['繪師: ゆんみ-pixiv',       'https://i.imgur.com/iG8OaxQ.jpg'],
            3 : ['繪師: 夏菜ゆさく-pixiv',    'https://i.imgur.com/qWEChhw.jpg'],
            4 : ['繪師: 六丸いなみ-pixiv',    'https://i.imgur.com/jQsBTjp.jpg'],
            5 : ['繪師: ゆんみ-pixiv',       'https://i.imgur.com/azqfXkv.jpg'],
            6 : ['繪師: ゆんみ-pixiv',       'https://i.imgur.com/4Gbgott.jpg'],
            7 : ['繪師: ゆんみ-pixiv',       'https://i.imgur.com/GPjyJMj.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message in ['茉莉','マツリ' ,'織原茉莉','跳跳虎']:
        value_i = {
            1 : ['繪師: ゆんみ-pixiv',        'https://i.imgur.com/3nlfDvh.jpg'],
            2 : ['繪師: ひとつのなか-pixiv',  'https://i.imgur.com/i04aggD.jpg'],
            3 : ['繪師: 夏菜ゆさく-pixiv',    'https://i.imgur.com/5TwMo5R.jpg'],
            4 : ['繪師: ゆんみ-pixiv',        'https://i.imgur.com/y6pVSXZ.jpg'],
            5 : ['繪師: ゆんみ-pixiv',        'https://i.imgur.com/x2pbDlA.jpg'],
            6 : ['繪師: 夏菜ゆさく-pixiv',    'https://i.imgur.com/rTZaTo9.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message in ['團長','團長們','騎士團cp']:
        value_i = {
            1 : ['繪師: 六丸いなみ-pixiv',    'https://i.imgur.com/e2tRy2c.jpg'],
            2 : ['繪師: 六丸いなみ-pixiv',    'https://i.imgur.com/jasKCgm.jpg'],
            3 : ['繪師: 六丸いなみ-pixiv',    'https://i.imgur.com/vbQTnzp.jpg'],
            4 : ['繪師: 六丸いなみ-pixiv',    'https://i.imgur.com/cVpqbdB.jpg'],
            5 : ['繪師: 六丸いなみ-pixiv',    'https://i.imgur.com/tFRmHHC.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
### 美食殿堂 ###
### 美食殿 ###
### 美食殿堂 ###
    elif input_message[:3] == '美食殿' and len(input_message)<=4:
        value_i = {
            1 :  ['繪師: たなし-pixiv',         'https://i.imgur.com/VZtrbTV.jpg'],
            2 :  ['繪師: 猫小渣-pixiv',         'https://i.imgur.com/4tz9vVW.jpg'],
            3 :  ['繪師: 猫小渣-pixiv',         'https://i.imgur.com/AJNi0Qf.jpg'],
            4 :  ['繪師: msh-pixiv',            'https://i.imgur.com/sVNvxwR.jpg'],
            5 :  ['繪師: QuAn_-pixiv',          'https://i.imgur.com/iYY6otG.jpg'],
            6 :  ['繪師: 高瀬コウ-pixiv',        'https://i.imgur.com/izcQ6oh.jpg'],
            7 :  ['繪師: AJ-pixiv',             'https://i.imgur.com/aIbegIR.jpg'],
            8 :  ['繪師: AJ-pixiv',             'https://i.imgur.com/te6hJJq.jpg'],
            9 :  ['繪師: 昌未-pixiv',           'https://i.imgur.com/A2Qjk82.jpg'],
            10 : ['繪師: 昌未-pixiv',           'https://i.imgur.com/CfeEEU7.jpg'],
            11 : ['繪師: msh-pixiv',            'https://i.imgur.com/TBAZxPW.jpg'],
            12 : ['繪師: ZN (あえん)-pixiv',     'https://i.imgur.com/cGkummU.jpg'],
            13 : ['繪師: 結城辰也-pixiv',        'https://i.imgur.com/J4XbyXx.jpg'],
            14 : ['繪師: 夜凪朝妃-pixiv',        'https://i.imgur.com/8wxQ12m.jpg'],
            15 : ['繪師: とうち-pixiv',          'https://i.imgur.com/gzNmvkA.jpg'],
            16 : ['繪師: ジヤス-pixiv',          'https://i.imgur.com/kmwSilM.jpg'],
            17 : ['繪師: にしん-pixiv',          'https://i.imgur.com/Oy5rTFa.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message in ['凱留','接頭霸王','考','黑貓','背骨貓','背骨','背刺貓','背刺','945','臭鼬','百地希留耶','希留耶','キャル' ,'945ml','正月凱留','泳裝凱留']:
        value_i = {
            1 :  ['繪師: たてじまうり-pixiv',        'https://i.imgur.com/9DQ3S5y.jpg'],
            2 :  ['繪師: 灰島-pixiv',               'https://i.imgur.com/HvYE6zv.jpg'],
            3 :  ['繪師: じゅんまぁち。-pixiv',      'https://i.imgur.com/D2NySWD.jpg'],
            4 :  ['繪師: けんぴゃっ-pixiv',          'https://i.imgur.com/ilub54I.jpg'],
            5 :  ['繪師: みり-pixiv',               'https://i.imgur.com/YWmEuA8.jpg'],
            6 :  ['繪師: @fang410693029-twitter',   'https://i.imgur.com/YWmEuA8.jpg'],
            7 :  ['繪師: Je_M-pixiv',               'https://i.imgur.com/dACqudt.jpg'],
            8 :  ['繪師: ごやいん-pixiv',            'https://i.imgur.com/FXZRaqL.jpg'],
            9 :  ['繪師: @CeNanGam-twitter',        'https://i.imgur.com/k1hHShl.jpg'],
            10 : ['圖源: shadowverse',              'https://i.imgur.com/6EgNtoh.jpg'],
            11 : ['圖源: shadowverse',              'https://i.imgur.com/kO56BAY.jpg'],
            12 : ['圖源: shadowverse',              'https://i.imgur.com/h21rScV.jpg'],
            13 : ['繪師: ねこ鳴都(meito)-pixiv',     'https://i.imgur.com/O50QzvM.jpg'],
            14 : ['繪師: Panda-pixiv',              'https://i.imgur.com/TXyeTkc.jpg'],
            15 : ['繪師: puruding-pixiv',           'https://i.imgur.com/3V9s93C.jpg'],
        }
        if(len(value_i[i% len(value_i)+1])==2): 
            line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
        else:
            line_bot_api.reply_message(event.reply_token,ImageMessageURL(value_i[i% len(value_i)+1]))
    elif input_message in ['佩可','吃貨','佩可莉姆','貪吃佩可','ペコリーヌ','公主','尤絲蒂亞娜·F·阿斯特萊亞','尤絲蒂亞娜','ヤバイですね','牙敗','公主佩可','泳裝佩可']:
        value_i = {
            1 :  ['圖源: shadowverse',           "https://i.imgur.com/mtO06wN.jpg"],
            2 :  ['繪師: @DokkoiMigu-twitter',   "https://i.imgur.com/SKsplQ6.jpg"],
            3 :  ['繪師: @mato_kechi-twitter',   "https://i.imgur.com/YYwWhZi.jpg"],
            4 :  ['繪師: ゆりりん-pixiv',         "https://i.imgur.com/i2MU9a7.jpg"],
            5 :  ['繪師: osa-pixiv',             "https://i.imgur.com/GQ5106Q.jpg"],
            6 :  ['繪師: イシノセ-pixiv',         "https://i.imgur.com/mm0qioK.jpg"],
            7 :  ['繪師: イシノセ-pixiv',         "https://i.imgur.com/0Ne7tnn.jpg"],
            8 :  ['繪師: 92M-pixiv',             "https://i.imgur.com/uoHcGkh.jpg"],
            9 :  ['繪師: ゆゆ-pixiv',             "https://i.imgur.com/wPR4lyl.jpg"],
            10 : ['繪師: たてじまうり-pixiv',     "https://i.imgur.com/cafbX7D.jpg"],
            11 : ['繪師: ヒャング-pixiv',         "https://i.imgur.com/bDvRTJN.jpg"],
            12 : ['繪師: BNARI-pixiv',           "https://i.imgur.com/FCNIMbS.jpg"],
            13 : "https://i.imgur.com/zOWI57k.jpg",
            14 : "https://i.imgur.com/9DqK9ju.jpg",
            15 : ['繪師: sonchi-pixiv',          "https://i.imgur.com/vXtXpZa.jpg"],
            16 : ['繪師: @goumudan-twitter',     "https://i.imgur.com/pjv3xkW.jpg"]
        }
        if(len(value_i[i% len(value_i)+1])==2): 
            line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
        else:
            line_bot_api.reply_message(event.reply_token,ImageMessageURL(value_i[i% len(value_i)+1]))
    elif input_message in ['可可蘿','可蘿','可口蘿','コッコロ','小小嚮導','媽媽','公主可可蘿','正月可可蘿','泳裝可可蘿']:
        value_i = {
            1 :  'https://i.imgur.com/Dbx8O8i.jpg',
            2 :  'https://i.imgur.com/nR1ZxgM.jpg',
            3 :  'https://i.imgur.com/6YoHLvJ.jpg',
            4 :  ['繪師: 骨カワ-pixiv',              'https://i.imgur.com/3y17m4w.jpg'],
            5 :  ['繪師: アイダ-pixiv',              'https://i.imgur.com/6IQgnvV.jpg'],
            6 :  ['繪師: 真崎ケイ-pixiv',            'https://i.imgur.com/CGDOWoL.jpg'],
            7 :  ['繪師: @Alisia_0812-twitter',     'https://i.imgur.com/os1zhfw.jpg'],
            8 :  ['繪師: @ex_pulse-twitter',        'https://i.imgur.com/OcTnn4l.jpg'],
            9 :  ['繪師: @shiba1311-twitter',       'https://i.imgur.com/bUDFQZ2.jpg'],
            10 : ['繪師: アイダ-pixiv',             'https://i.imgur.com/vcjesG2.jpg'],
            11 : ['繪師: @osaillust-twitter',       'https://i.imgur.com/72AwIXj.jpg'],
            12 : ['繪師: @Re_hnk-twitter',          'https://i.imgur.com/Ti9PvVH.jpg'],
            13 : ['繪師: とも-pixiv',               'https://i.imgur.com/zsskgXH.jpg'],
            14 : ['繪師: Xeph-pixiv',               'https://i.imgur.com/uEysCSr.jpg'],
            15 : ['繪師: Xeph-pixiv',               'https://i.imgur.com/bP7r05H.jpg'],
            16 : ['繪師: sune-pixiv',               'https://i.imgur.com/MMBF02n.jpg'],
        }
        if(len(value_i[i% len(value_i)+1])==2): 
            line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
        else:
            line_bot_api.reply_message(event.reply_token,ImageMessageURL(value_i[i% len(value_i)+1]))
    elif input_message == '可哥蘿':
        value_i = {
            1 :  '真是的 騎士君又惹哭可哥蘿了...(咦?',
            2 :  '可可萝同志乃我大美食殿堂\n不可分割之固有成员\n骑士君应充分理解和尊重\n美食殿堂的这一立场\n並立即正名"可可蘿"',
            3 :  ['是可可蘿啦...(可可蘿機器人哭倒路邊',    'https://i.imgur.com/gIF9vdY.png']
        }
        if(len(value_i[i% len(value_i)+1])==2): 
            line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
        else:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text= value_i[i% len(value_i)+1]))
    elif input_message in ['柚樹','佑樹','祐樹','騎士君','失智','ユウキ','變態的可疑分子','公主騎士','優衣最愛的']:
        value_i = {
            1 :  ['圖源: shadowverse',       'https://i.imgur.com/dxwXlbZ.jpg'],
            2 :  ['繪師: 千齋-pixiv',        'https://i.imgur.com/lhB9MYO.jpg'],
            3 :  ['繪師: 木咕咕-pixiv',      'https://i.imgur.com/wgWBaOC.jpg'],
            4 :  ['繪師: 飛翔的窩-巴哈',     'https://i.imgur.com/zIdOU5s.jpg'],
            5 :  ['J̵̮́u̷̠͇̎ś̷̛̝̼t̵̜͍̓̑ ̸̪̱̍͝Y̶̦̓͠u̴͎͘i̶͎̕ ̸͕͕̽.̵̖̼͋͝.̸̰͊̔.̴̢̑',           'https://i.imgur.com/0YenUwM.jpg'],
            6 :  ['繪師: セーリュー-pixiv',  'https://i.imgur.com/QrE3zQM.jpg'],
            7 :  ['繪師: 天雷-pixiv',        'https://i.imgur.com/w7jyWqm.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message in ['謝菲','シェフィ','雪菲','藍龍']:
        value_i = {
            1 :  ['繪師: アイダ-pixiv',     'https://i.imgur.com/zj4GQQF.jpg'],
            2 :  ['繪師: こもこも-pixiv',   'https://i.imgur.com/3PUa0jt.jpg'],
            3 :  ['繪師: やじ-pixiv',       'https://i.imgur.com/5UPjSbd.jpg'],
            4 :  ['繪師: Miyamoya-pixiv',   'https://i.imgur.com/iPIVHH9.jpg'],
            5 :  ['繪師: ゆずゆい-pixiv',   'https://i.imgur.com/X3fKJyS.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message in ['孝心逐漸變質','孝心變質']:
        value_i = {
            1 :  ['繪師: 92M-pixiv',            'https://i.imgur.com/GfAKT7y.jpg'],
            2 :  ['繪師: 室町アツシ-pixiv',      'https://i.imgur.com/bhXnyCz.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
### 七冠 ###
### 桂冠 ###
### 七冠 ###
    elif input_message in ['克莉絲提娜','克里斯蒂娜','クリスティーナ','克總','誓約女君','老太婆','副團長','阿姨','製作人','聖誕克莉絲提娜']:
        value_i = {
            1 : ['繪師: qwerty131154-巴哈',       'https://i.imgur.com/fjYRD4W.jpg'],
            2 : ['繪師: 双見ゆうき-pixiv',        'https://i.imgur.com/fY5YhrJ.jpg'],
            3 : ['繪師: ぽむり-pixiv',            'https://i.imgur.com/vhVVBlr.jpg'],
            4 : ['繪師: 淫傘うさぎ-pixiv',        'https://i.imgur.com/yqV2k5k.jpg'],
            5 : ['繪師: itaco-pixiv',            'https://i.imgur.com/99cwfub.jpg'],
            6 : ['繪師: Saha_-pixiv',            'https://i.imgur.com/QRyfHzd.jpg'],
            7 : ['繪師: しゅーくりいむ-pixiv',    'https://i.imgur.com/A6e9Nv6.jpg'],
            8 : ['繪師: Hanse-pixiv',            'https://i.imgur.com/tf6sNt6.jpg'],
            9 : ['繪師: sonchi-pixiv',           'https://i.imgur.com/aQNaclR.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message in ['矛依未','青蛙','ムイミ','天樓霸斷劍','諾唯姆','姆咪']:
        value_i = {
            1 :  'https://i.imgur.com/CW1GCBv.jpg',
            2 :  ['繪師: AJ-pixiv',         "https://i.imgur.com/Pgg0fqM.jpg"],
            3 :  ['繪師: 塵-pixiv',         "https://i.imgur.com/QZMeUVh.jpg"],
            4 :  ['繪師: 延ビ-pixiv',       "https://i.imgur.com/S6OSknV.jpg"],
            5 :  ['繪師: Jehyun-pixiv',     "https://i.imgur.com/wZzXQMY.jpg"],
            6 :  ['繪師: カッシュ-pixiv',   "https://i.imgur.com/5890KnY.jpg"],
            7 :  ['繪師: 延ビ-pixiv',       "https://i.imgur.com/wH7RlxR.jpg"],
            8 :  ['繪師: 延ビ-pixiv',       "https://i.imgur.com/P1AKT4r.jpg"],
            9 :  ['繪師: ヒーロー-pixiv',   "https://i.imgur.com/2sAbiD5.jpg"],
            10 : ['繪師: ヒーロー-pixiv',   "https://i.imgur.com/jBrFpQr.jpg"]
        }
        if(len(value_i[i% len(value_i)+1])==2): 
            line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
        else:
            line_bot_api.reply_message(event.reply_token,ImageMessageURL(value_i[i% len(value_i)+1]))
    elif input_message in ['似似花','ネネカ','448','nnk','現士實似似花','變貌大妃']:
        value_i = {
            1 :  ['繪師: 蛞蝓SLUG-pixiv',       "https://i.imgur.com/5SuITSA.jpg"],
            2 :  ['繪師: うまるつふり-pixiv',    "https://i.imgur.com/aGDYsI3.jpg"],
            3 :  ['繪師: ヒーロー-pixiv',       "https://i.imgur.com/yGsd9CX.jpg"],
            4 :  ['繪師: Sw(すぅ)-pixiv',       "https://i.imgur.com/ZzUuYHz.jpg"],
            5 :  ['繪師: 1ピコ㍍-pixiv',        "https://i.imgur.com/Xsi8DLf.jpg"],
            6 :  ['繪師: AJ-pixiv',             "https://i.imgur.com/gcbOijd.jpg"],
            7 :  ['繪師: Sw(すぅ)-pixiv',       "https://i.imgur.com/IWWXm2i.jpg"],
            8 :  ['繪師: Sw(すぅ)-pixiv',       "https://i.imgur.com/JIvmhTS.jpg"],
            9 :  ['繪師: 天雷-pixiv',           "https://i.imgur.com/jjsaSVF.jpg"],
            10 : ['繪師: Sw(すぅ)-pixiv',       "https://i.imgur.com/y0vPH6W.jpg"],
            11 : ['繪師: Sw(すぅ)-pixiv',       "https://i.imgur.com/rYx1j94.jpg"],
            12 : ['繪師: けんぴゃっ-pixiv',     "https://i.imgur.com/Gbt0uVO.jpg"]
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message in ['夥伴','伙伴','同伴','相棒','アイボウ','尾狗刀','尾刀狗']:
        value_i = {
            1 :  ['繪師: 塵-pixiv',     "https://i.imgur.com/SneVdIU.jpg"],
            2 :  ['繪師: 塵-pixiv',     "https://i.imgur.com/scnsgWD.jpg"],
            3 :  ['繪師: 塵-pixiv',     "https://i.imgur.com/xMsa8U2.jpg"],
            4 :  ['繪師: 塵-pixiv',     "https://i.imgur.com/I5Qk2cQ.jpg"],
            5 :  ['繪師: 塵-pixiv',     "https://i.imgur.com/AUG6ynv.jpg"],
            6 :  ['繪師: 塵-pixiv',     "https://i.imgur.com/L7I8aOS.jpg"],
            7 :  ['繪師: 塵-pixiv',     "https://i.imgur.com/1StDQPw.jpg"],
            8 :  ['繪師: 塵-pixiv',     "https://i.imgur.com/DRVw6os.jpg"],
            9 :  ['繪師: 延ビ-pixiv',   "https://i.imgur.com/CMeG1rV.jpg"],
            10 : ['繪師: 延ビ-pixiv',   "https://i.imgur.com/zele47S.jpg"]
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message in ['拉比林斯達','ラビリスタ','模索路晶','晶','迷宮女王','迷路女王']:
        value_i = {
            1 :  ['繪師: オスティ-pixiv',     "https://i.imgur.com/J69aauG.jpg"],
            2 :  ['繪師: オスティ-pixiv',     "https://i.imgur.com/kHF3TOs.jpg"],
            3 :  ['繪師: ミロ-pixiv',        "https://i.imgur.com/Wfd8LI2.jpg"],
            4 :  ['繪師: 瑞希遥-pixiv',      "https://i.imgur.com/DTHd6Af.jpg"]
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message == '桂冠':
        value_i = {
            1 : ImageMessageURL("https://i.imgur.com/5lRyLJy.png"),   
            2 : TextSendMessage(text ="騎士君是肚子餓了嗎？"),  
            3 : TextSendMessage(text ="桂冠你媽啦，就跟你說七冠了。\n-布丁")
        }
        line_bot_api.reply_message(event.reply_token,value_i[i% len(value_i)+1])
### 馬納歷亞 ###
### マナリアフレンズ ###
### Manaria Friends ###
    elif input_message in ['馬納歷亞','マナリアフレンズ','Manaria Friends','百合公主']:
        value_i = {
            1 :  ['繪師: 92M-pixiv',            'https://i.imgur.com/AtJOEqh.jpg'],
            2 :  ['繪師: とも-pixiv',           'https://i.imgur.com/rqVMy0r.jpg'],
            3 :  ['繪師: 音の绯-pixiv',         'https://i.imgur.com/OYbCg5i.jpg'],
            4 :  ['繪師: ぽんず-pixiv',         'https://i.imgur.com/QARR8iO.jpg'],
            5 :  ['繪師: れんず-pixiv',         'https://i.imgur.com/t9jLBeS.jpg'],
            6 :  ['繪師: にゃー-pixiv',         'https://i.imgur.com/Dl0bf68.jpg'],
            7 :  ['繪師: れっれれ-pixiv',       'https://i.imgur.com/pqQQ1ED.jpg'],
            8 :  ['繪師: みどりのちゃ-pixiv',   'https://i.imgur.com/D6B3wSk.jpg'],
            9 :  ['繪師: AJ-pixiv',            'https://i.imgur.com/JE5MeGW.jpg'],
            10 : ['繪師: いとね-pixiv',         'https://i.imgur.com/pz8dC3b.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif  input_message in ['古蕾雅','グレア','龍姬','古雷雅'] :
        value_i = {
            1 :  ['繪師: KWS-pixiv',          'https://i.imgur.com/aatQVtQ.jpg'],
            2 :  ['繪師: かんかっぴ-pixiv',    'https://i.imgur.com/jYom8yC.jpg'],
            3 :  ['繪師: とも-pixiv',         'https://i.imgur.com/qxe6AtA.jpg'],
            4 :  ['繪師: とも-pixiv',         'https://i.imgur.com/zvolEcL.jpg'],
            5 :  ['繪師: とも-pixiv',         'https://i.imgur.com/7RuuWPm.jpg'],
            6 :  ['繪師: いとね-pixiv',       'https://i.imgur.com/lhXOFCV.jpg'],
            7 :  ['繪師: おもおもも-pixiv',   'https://i.imgur.com/HHuR7AU.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message in ['安','アン','55kg','馬納歷亞公主','宏大魔法']:
        value_i = {
            1 :  ['繪師: S.U.-pixiv',         'https://i.imgur.com/TYwLMpV.jpg'],
            2 :  ['繪師: いとね-pixiv',        'https://i.imgur.com/SoSwfNW.jpg'],
            3 :  ['繪師: HotaK-pixiv',        'https://i.imgur.com/sqexcv7.jpg'],
            4 :  ['繪師: セラ-pixiv',         'https://i.imgur.com/pF3oHmc.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message in ['露','ルゥ','眼球','補考','補考女帝']:
        value_i = {
            1 :  ['繪師: ぺろんちょ-pixiv',      'https://i.imgur.com/WXCiwFo.jpg'],
            2 :  ['繪師: AJ-pixiv',             'https://i.imgur.com/xcFCKju.jpg'],
            3 :  ['繪師: りこ-pixiv',           'https://i.imgur.com/oFuxXbB.jpg'],
            4 :  ['繪師: なかひま-pixiv',       'https://i.imgur.com/UMZ3jqU.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
### Re:從零開始的異世界生活 ###
### Re:ゼロから始める異世界生活 ###
### Re:0 ###
    elif input_message in ['Re:從零開始的異世界生活','Re:ゼロから始める異世界生活','Re0','re0','Re:0','re:0']:
        value_i = {
            1 :  ['繪師: ぽえ-pixiv',            'https://i.imgur.com/zEWwDWx.jpg'],
            2 :  ['繪師: 桃乃きのこ。-pixiv',     'https://i.imgur.com/9sNkqru.jpg'],
            3 :  ['繪師: ChinTora0201-pixiv',    'https://i.imgur.com/JXlERea.jpg'],
            4 :  ['繪師: 喜欢夜宵yayoi-pixiv',    'https://i.imgur.com/RR4bXb2.jpg'],
            5 :  ['繪師: ゆぞうに-pixiv',         'https://i.imgur.com/GlwcKnj.jpg'],
            6 :  ['繪師: えらんと-pixiv',         'https://i.imgur.com/6dltMdz.jpg'],
            7 :  ['繪師: だよ-pixiv',            'https://i.imgur.com/UamOLeJ.jpg'],
            8 :  ['繪師: あろえ-pixiv',          'https://i.imgur.com/3zH6gy7.jpg'],
            9 :  ['繪師: しゃけ沢-pixiv',        'https://i.imgur.com/6GAVLKt.jpg'],
            10 : ['繪師: しゃけ沢-pixiv',        'https://i.imgur.com/kkweao4.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message in ['愛蜜莉雅','愛蜜莉亞','エミリア','EMT','emt','莉雅']:
        value_i = {
            1 :  ['繪師: @Seic_Oh-pixiv',    'https://i.imgur.com/Il334iS.jpg'],
            2 :  ['繪師: DABY-pixiv',        'https://i.imgur.com/slm7jSF.jpg'],
            3 :  ['繪師: PiO-pixiv',         'https://i.imgur.com/mBDxyvy.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message in ['雷姆','レム','快速動眼期']:
        value_i = {
            1 :  ['繪師: そらほし-pixiv',        'https://i.imgur.com/hrYaNNk.jpg'],
            2 :  ['繪師: DABY-pixiv',           'https://i.imgur.com/SqT0j7K.jpg'],
            3 :  ['繪師: ttosom-pixiv',         'https://i.imgur.com/BTclhHL.jpg'],
            4 :  ['繪師: MOMIN-pixiv',          'https://i.imgur.com/CUh9u9u.jpg'],
            5 :  ['繪師: Bcoca-pixiv',          'https://i.imgur.com/Lhuqtbl.jpg'],
            6 :  ['繪師: Melings-pixiv',        'https://i.imgur.com/MAbMNvB.jpg'],
            7 :  ['繪師: 赤つき-pixiv',          'https://i.imgur.com/qwwmytW.jpg'],
            8 :  ['繪師: ONSEM-pixiv',          'https://i.imgur.com/yxq7Q41.jpg'],
            9 :  ['繪師: pangbai_666-pixiv',    'https://i.imgur.com/nSIZyms.jpg'],
            10 : ['繪師: 千羽茸みな-pixiv',      'https://i.imgur.com/W3i3XrP.jpg'],
            11 : ['繪師: はちろく-pixiv',        'https://i.imgur.com/BFjYGja.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message in ['拉姆','ラム','記憶體','快取']:
        value_i = {
            1 :  ['繪師: 千羽茸みな-pixiv',     'https://i.imgur.com/170L1AL.jpg'],
            2 :  ['繪師: pigone-pixiv',        'https://i.imgur.com/vCtXAgN.jpg'],
            3 :  ['繪師: MOMIN-pixiv',         'https://i.imgur.com/NABfw4w.jpg'],
            4 :  ['繪師: Suo-pixiv',           'https://i.imgur.com/lco0h8A.jpg'],
            5 :  ['繪師: G.YA-pixiv',          'https://i.imgur.com/G1pGidw.jpg'],
            6 :  ['繪師: mongble-pixiv',       'https://i.imgur.com/yDjYb2W.jpg'],
            7 :  ['繪師: 100wang-pixiv',       'https://i.imgur.com/1V0lN5M.jpg'],
            8 :  ['繪師: ゆぞうに-pixiv',       'https://i.imgur.com/swAQL8v.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message in ['碧翠絲','ベアトリス','貝蒂','碧翠子']:
        value_i = {
            1 :  ['繪師: だよ-pixiv',               'https://i.imgur.com/nGQILuC.jpg'],
            2 :  ['繪師: KeG-pixiv',                'https://i.imgur.com/scWOIZi.jpg'],
            3 :  ['繪師: tonowa トノワ-pixiv',      'https://i.imgur.com/0C9ZjXh.jpg'],
            4 :  ['繪師: しゃけ沢-pixiv',           'https://i.imgur.com/rm7jCFZ.jpg'],
            5 :  ['繪師: きんぎん-pixiv',           'https://i.imgur.com/uLWLBqp.jpg'],
            6 :  ['繪師: そらほし-pixiv',           'https://i.imgur.com/0Xqn2Kj.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
### 偶像大師灰姑娘女孩 ###
### アイドルマスターシンデレラガールズ ###
### New Generation ###
    elif input_message in ['偶像大師灰姑娘女孩','アイドルマスターシンデレラガールズ','偶大','偶像大師','灰姑娘','新世代','New Generation','new generation']:
        value_i = {
            1 :  ['繪師: シワスタカシ-pixiv',    'https://i.imgur.com/WZMIbDm.jpg'],
            2 :  ['繪師: Blue_Gk-pixiv',        'https://i.imgur.com/oEwb94k.jpg'],
            3 :  ['繪師: nyanya-pixiv',         'https://i.imgur.com/2T86ioj.jpg'],
            4 :  ['繪師: 森倉円-pixiv',          'https://i.imgur.com/V701qlH.jpg'],
            5 :  ['繪師: 森倉円-pixiv',          'https://i.imgur.com/Tttl70z.jpg'],
            6 :  ['繪師: 森倉円-pixiv',          'https://i.imgur.com/pdpPweS.jpg'],
            7 :  ['繪師: 月神るな-pixiv',        'https://i.imgur.com/7ha5BHr.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message in ['凜','渋谷凛','澀谷凜','蒼之劍士']:
        value_i = {
            1 :  ['繪師: たまかが-pixiv',           'https://i.imgur.com/IHb3Fpq.jpg'],
            2 :  ['繪師: たまかが-pixiv',           'https://i.imgur.com/dEOc4B9.jpg'],
            3 :  ['繪師: たまかが-pixiv',           'https://i.imgur.com/Pn8rJg6.jpg'],
            4 :  ['繪師: すとろα-pixiv',            'https://i.imgur.com/rpLWgZ0.jpg'],
            5 :  ['繪師: たまかが-pixiv',           'https://i.imgur.com/RYqtKt4.jpg'],
            6 :  ['繪師: Appplepie/AP-pixiv',      'https://i.imgur.com/T3XJO0P.jpg'],
            7 :  ['繪師: 遊びに来た人・ｖ・-pixiv',  'https://i.imgur.com/eFryXdz.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message in ['卯月','ウヅキ','島村卯月','笑容狂魔','笑容狂魔卯月']:
        value_i = {
            1 :  ['我爸摳爸twitter: @cloba377',     'https://i.imgur.com/LJei46w.jpg'],
            2 :  ['繪師: うらび-pixiv',             'https://i.imgur.com/dUdTGQb.jpg'],
            3 :  ['繪師: 荻pote-pixiv',             'https://i.imgur.com/mm8Yo4p.jpg'],
            4 :  ['繪師: 結城辰也-pixiv',           'https://i.imgur.com/UyrBq7f.jpg'],
            5 :  ['繪師: U35(うみこ)-pixiv',        'https://i.imgur.com/sgquvvJ.jpg'],
            6 :  ['繪師: 芹野いつき-pixiv',         'https://i.imgur.com/tV1mcRw.jpg'],
            7 :  ['繪師: 芹野いつき-pixiv',         'https://i.imgur.com/Y5qeCti.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message in ['未央','ミオ','本田未央','醬未央']:
        value_i = {
            1 :  ['繪師: なかむら-pixiv',       'https://i.imgur.com/c7AyD0I.png'],
            2 :  ['繪師: なかむら-pixiv',       'https://i.imgur.com/PSDg4hg.png'],
            3 :  ['繪師: なかむら-pixiv',       'https://i.imgur.com/ytEi5Ch.png'],
            4 :  ['繪師: なかむら-pixiv',       'https://i.imgur.com/oLYkBFq.png'],
            5 :  ['繪師: なかむら-pixiv',       'https://i.imgur.com/3LVm262.png'],
            6 :  ['繪師: なかむら-pixiv',       'https://i.imgur.com/OMM2Nnw.png'],
            7 :  ['繪師: なかむら-pixiv',       'https://i.imgur.com/u5b5jeY.png'],
            8 :  ['繪師: なかむら-pixiv',       'https://i.imgur.com/2NmYR4H.png'],
            9 :  ['繪師: なかむら-pixiv',       'https://i.imgur.com/5kjaeRP.png'],
            10 : ['繪師: なかむら-pixiv',       'https://i.imgur.com/pjAWB3t.png'],
            11 : ['繪師: なかむら-pixiv',       'https://i.imgur.com/dcciHxb.png'],
            12 : ['繪師: なかむら-pixiv',       'https://i.imgur.com/JFsM3G9.png'],
            13 : ['繪師: なかむら-pixiv',       'https://i.imgur.com/8P5x7yP.png'],
            14 : ['繪師: なかむら-pixiv',       'https://i.imgur.com/wBYo85z.png'],
            15 : ['繪師: なかむら-pixiv',       'https://i.imgur.com/MXQ211f.png']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
### 角色 (其他) ###
### 角色 (其他) ###
### 角色 (其他) ###
    elif input_message == ['吉塔','ジータ','姬塔','騎空士','團長','古戰場逃兵','古戰場','吉他']:
        value_i = {
            1 :  ['繪師: sirohito-pixiv',       'https://i.imgur.com/JQVl13u.jpg'],
            2 :  ['繪師: sirohito-pixiv',       'https://i.imgur.com/Koj0uLM.jpg'],
            3 :  ['繪師: iro-pixiv',            'https://i.imgur.com/H7HCIAP.jpg'],
            4 :  ['繪師: たく庵-pixiv',          'https://i.imgur.com/A2aEn1l.jpg'],
            5 :  ['繪師: iro-pixiv',            'https://i.imgur.com/JbYRjt3.jpg'],
            6 :  ['繪師: まぐ-pixiv',           'https://i.imgur.com/6ZfdF8m.jpg'],
            7 :  ['繪師: とうふぷりん-pixiv',    'https://i.imgur.com/oG0b6Hi.jpg'],
            8 :  ['繪師: みり㍑-pixiv',          'https://i.imgur.com/UCIL06b.jpg'],
            9 :  ['繪師: 葉千はちみつ-pixiv',    'https://i.imgur.com/usc7BWI.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message in ['露娜','ルナ','露那','死靈法師','好朋友']: 
        value_i = {
            1 :  ['繪師: Enji-pixiv',          'https://i.imgur.com/ob9Uw8y.jpg'],
            2 :  ['繪師: により-pixiv',         'https://i.imgur.com/HgbgckH.jpg'],
            3 :  ['繪師: HIROKAZU-pixiv',      'https://i.imgur.com/igqmOgB.jpg'],
            4 :  ['繪師: ちてたん-pixiv',       'https://i.imgur.com/SCP6xRn.jpg'],
            5 :  ['繪師: により-pixiv',         'https://i.imgur.com/amVcMiq.jpg'],
            6 :  ['繪師: 小山内-pixiv',         'https://i.imgur.com/BrEu6Vm.jpg'],
            7 :  ['繪師: shoonia-pixiv',       'https://i.imgur.com/oAjAmEe.jpg'],
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message in ['亞里莎','アリサ','亞里瞎','瞎子','羅莎莉亞']: 
        value_i = {
            1 :  ['繪師: 黒井ススム-pixiv',       'https://i.imgur.com/BCu2qYG.jpg'],
            2 :  ['繪師: ヨシノリョウ-pixiv',     'https://i.imgur.com/7NwXZJ2.jpg'],
            3 :  ['繪師: 士雷 Shirai-pixiv',     'https://i.imgur.com/QvQRCLn.jpg'],
            4 :  ['繪師: kieed-pixiv',           'https://i.imgur.com/anYIkmH.jpg'],
            5 :  ['繪師: きち-pixiv',            'https://i.imgur.com/crxmOPm.jpg'],
            6 :  ['繪師: きち-pixiv',            'https://i.imgur.com/FNVMMbH.jpg'],
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message in ['愛梅斯','DD頭子','アメス','艾梅斯']:
        value_i = {
            1 :  ['繪師: aono-pixiv',           'https://i.imgur.com/yk8dzMD.jpg','https://i.imgur.com/uc1XcEF.jpg','https://i.imgur.com/uKWemDs.jpg'],
            2 :  ['繪師: aono-pixiv',           'https://i.imgur.com/hurT0Sk.jpg'],
            3 :  ['繪師: aono-pixiv',           'https://i.imgur.com/9wfDIYY.jpg'],
            4 :  ['繪師: aono-pixiv',           'https://i.imgur.com/M6WlrdB.jpg'],
            5 :  ['繪師: いすとーん-pixiv',      'https://i.imgur.com/VnQ0cPI.jpg'],
            6 :  ['繪師: つちのトン-pixiv',      'https://i.imgur.com/lzKdQtU.jpg'],
            7 :  ['繪師: うまるつふり-pixiv',    'https://i.imgur.com/LKRmGhU.jpg'],
            8 :  ['繪師: みず-pixiv',           'https://i.imgur.com/v2grm1E.jpg'],
            9 :  ['繪師: 結月わらび-pixiv',      'https://i.imgur.com/1VERUPY.jpg'],
            10 : ['繪師: Sira-pixiv',           'https://i.imgur.com/NMi24Ix.jpg'],
            11 : ['繪師: aono-pixiv',           'https://i.imgur.com/WG2qVcL.jpg']
        }
        if(len(value_i[i% len(value_i)+1])==4): 
            line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1]),ImageMessageURL(value_i[i% len(value_i)+1][2]),ImageMessageURL(value_i[i% len(value_i)+1][3])])
        else:
            line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message in ['智乃','香風智乃','點兔','チノ']:
        value_i = {
            1 :  ['繪師: Hitsu-pixiv',                     'https://i.imgur.com/NocwYLL.jpg'],
            2 :  ['智乃香風 is not fuck your Waifu ok?',   'https://i.imgur.com/2ciqFyu.jpg'],
            3 :  ['繪師: 真崎ケイ-pixiv',                   'https://i.imgur.com/XLEXScW.jpg'],
            4 :  ['繪師: 真崎ケイ-pixiv',                   'https://i.imgur.com/Re8GFIS.jpg'],
            5 :  ['繪師: かにビーム-pixiv',                 'https://i.imgur.com/DIMIze8.jpg'],
            6 :  ['繪師: かにビーム-pixiv',                 'https://i.imgur.com/ZqmBXrD.jpg'],
            7 :  ['繪師: かにビーム-pixiv',                 'https://i.imgur.com/Dxysvop.jpg'],
            8 :  [ImageMessageURL('https://i.imgur.com/lINQsqA.jpg')],
            9 :  [ImageMessageURL('https://i.imgur.com/ZjvdEr7.jpg')],   
            10 : [ImageMessageURL('https://i.imgur.com/x6y3KiT.jpg')],    
            11 : [Chino_H(
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
            12 : [Chino_H(
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
        }
        if len (value_i[i% len(value_i)+1]) == 2:
            line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
        elif len (value_i[i% len(value_i)+1]) == 1 :
            line_bot_api.reply_message(event.reply_token,value_i[i% len(value_i)+1][0])
    elif input_message in ['對決','決戰','終戰','對峙']:
        value_i = {
            1 :  ['繪師: 天雷-pixiv',                   'https://i.imgur.com/2wM6Fv3.jpg'],
            2 :  ['繪師: KMH-pixiv',                    'https://i.imgur.com/d95pPjB.jpg'],
            3 :  ['繪師: こしあん（たいやき）-pixiv',     'https://i.imgur.com/tuIdVA5.jpg'],
            4 :  ['繪師: ウラズラ-pixiv',                'https://i.imgur.com/mse3aq4.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message in ['姊妹','姐妹','雙子']:
        value_i = {
            1 :  ['繪師: みず-pixiv',           'https://i.imgur.com/ul5x7d4.jpg'],
            2 :  ['繪師: 結城辰也-pixiv',       'https://i.imgur.com/UtkMYdI.jpg'],
            3 :  ['繪師: ヤンタロウ-pixiv',     'https://i.imgur.com/QaAUaca.jpg'],
            4 :  ['繪師: Chel-pixiv',          'https://i.imgur.com/vy9LI9P.jpg'],
            5 :  ['繪師: ぬるぷよ-pixiv',       'https://i.imgur.com/WH0niD2.jpg'],
            6 :  ['繪師: ゆりりん-pixiv',       'https://i.imgur.com/vuueBKE.jpg'],
            7 :  ['繪師: はちろく-pixiv',       'https://i.imgur.com/BFjYGja.jpg'],
            8 :  ['繪師: pigone-pixiv',        'https://i.imgur.com/vCtXAgN.jpg'],
            9 :  ['繪師: ユキタカ-pixiv',       'https://i.imgur.com/iQVOxk2.jpg'],
            10 : ['繪師: みどりのちゃ-pixiv',   'https://i.imgur.com/2wbKiAy.jpg'],
            11 : ['繪師: 秋月リア-pixiv',      'https://i.imgur.com/NRgmRRj.jpg'],
            12 : ['繪師: RYUKI-pixiv',         'https://i.imgur.com/cTrVg8W.jpg'],
            13 : ['繪師: cha_chya-pixiv',      'https://i.imgur.com/nle89D8.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message in ['魔法少女','馬猴燒酒']:
        value_i = {
            1 :  ['繪師: けんぴゃっ-pixiv',    'https://i.imgur.com/SrlAcry.jpg'],
            2 :  ['繪師: ぐっち庵-pixiv',      'https://i.imgur.com/O3N6mCH.jpg'],
            3 :  ['繪師: AJ-pixiv',           'https://i.imgur.com/nnT8dGX.jpg'],
            4 :  ['繪師: 夜凪朝妃-pixiv',      'https://i.imgur.com/bNqJcKQ.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message in ['公主連結','プリコネ']:
        value_i = {
            1 :  ['繪師: Lab2-pixiv',       'https://i.imgur.com/YBfyJ36.jpg'],
            2 :  ['繪師: 菖蒲-pixiv',       'https://i.imgur.com/Ljgi7Of.jpg'],
            3 :  ['繪師: 結城辰也-pixiv',   'https://iㄛmgur.com/FXAP2EI.jpg'],
            4 :  ['繪師: 冷蝉-pixiv',       'https://i.imgur.com/S07PioH.jpg'],
            5 :  ['繪師: みどりのちゃ-pixiv','https://i.imgur.com/jkxQSzY.jpg'],
            6 :  ['繪師: みどりのちゃ-pixiv','https://i.imgur.com/UNjZhIs.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
### 碧藍航線 ###
### アズールレーン ###
### 碧池航線 ###
    elif input_message in ['碧藍航線','アズールレーン','碧池航線']: 
        value_i = {
            1 :  ['繪師: 清里-pixiv',          'https://i.imgur.com/hONfsMX.jpg'],
            2 :  ['繪師: 玲汰-pixiv',          'https://i.imgur.com/Pl0P8pK.jpg'],
            3 :  ['繪師: 月満懐空-pixiv',      'https://i.imgur.com/3uZlrvV.jpg'],
            4 :  ['繪師: かぷりちお-pixiv',    'https://i.imgur.com/LU16tpQ.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message in ['標槍','Javelin','ジャベリン']: 
        value_i = {
            1 :  ['繪師: 紅薙ようと-pixiv',     'https://i.imgur.com/PzKzQCC.jpg'],
            2 :  ['繪師: もうぴい-pixiv',       'https://i.imgur.com/ryUR0N6.jpg'],
            3 :  ['繪師: もうぴい-pixiv',       'https://i.imgur.com/NTmk4IM.jpg'],
            4 :  ['繪師: もうぴい-pixiv',       'https://i.imgur.com/2WxKEDr.jpg'],
            5 :  ['繪師: もうぴい-pixiv',       'https://i.imgur.com/J7o6Htn.jpg'],
            6 :  ['繪師: もうぴい-pixiv',       'https://i.imgur.com/SekN4bL.jpg'],
            7 :  ['繪師: うなっち-pixiv',       'https://i.imgur.com/IO1nx2t.jpg'],
            8 :  ['繪師: まだら-pixiv',         'https://i.imgur.com/Q506e62.jpg'],
            9 :  ['繪師: ちょこころね-pixiv',   'https://i.imgur.com/mJEnaOq.jpg']
        }
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1]))
    elif input_message in ['拉菲','ラフィー','紅酒']: 
        value_i = {
            1 :  ['繪師: TouTou-pixiv',       'https://i.imgur.com/6xrpW1X.jpg'],
            2 :  ['繪師: 月うさぎ-pixiv',      'https://i.imgur.com/peTAQvV.jpg'],
            3 :  ['繪師: まとけち-pixiv',      'https://i.imgur.com/8tHVklt.jpg'],
            4 :  ['繪師: ぽしー-pixiv',        'https://i.imgur.com/tjy0KC3.jpg'],
            5 :  ['繪師: らむち-pixiv',        'https://i.imgur.com/VRFASyP.jpg'],
            6 :  ['繪師: 月うさぎ-pixiv',      'https://i.imgur.com/MB6IDtx.jpg'],
            7 :  ['繪師: 自律金属-pixiv',      'https://i.imgur.com/b7LXyZb.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message in ['綾波','アヤナミ','鬼神']: 
        value_i = {
            1 :  ['繪師: rika_39-pixiv',        'https://i.imgur.com/2vNqHVP.jpg'],
            2 :  ['繪師: Kana-pixiv',           'https://i.imgur.com/0I2TKgh.jpg'],
            3 :  ['繪師: 清里-pixiv',            'https://i.imgur.com/bD8S8tB.jpg'],
            4 :  ['繪師: いずもねる-pixiv',      'https://i.imgur.com/cG12rKK.jpg'],
            5 :  ['繪師: シロノーラ-pixiv',      'https://i.imgur.com/Js1wIYn.jpg'],
            6 :  ['繪師: narae-pixiv',          'https://i.imgur.com/udUKVLC.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message in ['獨角獸','ユニコーン'] or (input_message[:2] == '港獨' and len(input_message)<6): 
        value_i = {
            1 :  ['繪師: 浅ノ川-pixiv',      'https://i.imgur.com/zXNIMWm.jpg'],
            2 :  ['繪師: Kinty-pixiv',       'https://i.imgur.com/fnpwjNA.jpg'],
            3 :  ['繪師: 松うに-pixiv',      'https://i.imgur.com/ahxeS2g.jpg'],
            4 :  ['繪師: マトリ-pixiv',      'https://i.imgur.com/TQcJlUj.jpg'],
            5 :  ['繪師: 繭咲悠-pixiv',      'https://i.imgur.com/rhsNP4Y.jpg'],
            6 :  ['繪師: 小枝-pixiv',        'https://i.imgur.com/xmQ7dEq.jpg'],
            7 :  ['繪師: ちた-pixiv',        'https://i.imgur.com/KKfImwN.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
### 心跳文學部 ###
### Doki Doki Literature Club! ###
### 心跳文學部 ###
    elif input_message in ['心跳文學部','DokiDoki','Doki Doki','dokidoki','doki doki Literature Club']: 
        value_i = {
            1 :  ['繪師: TakuyaRawr-pixiv',   'https://i.imgur.com/rWqmHxA.jpg'],
            2 :  ['繪師: klaeia-pixiv',       'https://i.imgur.com/UJglYyJ.jpg'],
            3 :  ['繪師: 抠肉肚脐-pixiv',      'https://i.imgur.com/fK3p6OV.jpg'],
            4 :  ['繪師: Satchel-pixiv',      'https://i.imgur.com/dJjVUnG.jpg'],
            5 :  ['繪師: Satchely-pixiv',     'https://i.imgur.com/0J8OgFZ.jpg'],
            6 :  ['繪師: luke-pixiv',         'https://i.imgur.com/k4ed73c.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    if input_message in ['Monika','monika','just monika','Just Monika','莫妮卡','モニカ','毛二力']: 
        value_i = {
            1 :  ['騎士...君......\nj̶̧̄u̸̬͌s̸̡̋t̴̬͘ ̴̣̀m̸̪͘ỏ̶̺n̵̙̕ȉ̷̢ǩ̷̜ã̷̠',    '繪師: Yampa-pixiv',            'https://i.imgur.com/arYgHgh.jpg'],
            2 :  ['騎士...君......\nj̶̧̄u̸̬͌s̸̡̋t̴̬͘ ̴̣̀m̸̪͘ỏ̶̺n̵̙̕ȉ̷̢ǩ̷̜ã̷̠',    '繪師: ヒシ馬-pixiv',           'https://i.imgur.com/QHIY62W.jpg'],
            3 :  ['騎士...君......\nj̶̧̄u̸̬͌s̸̡̋t̴̬͘ ̴̣̀m̸̪͘ỏ̶̺n̵̙̕ȉ̷̢ǩ̷̜ã̷̠',    '繪師: 麦飴 アンプ-pixiv',       'https://i.imgur.com/v8Cu6fX.jpg'],
            4 :  ['騎士...君......\nj̶̧̄u̸̬͌s̸̡̋t̴̬͘ ̴̣̀m̸̪͘ỏ̶̺n̵̙̕ȉ̷̢ǩ̷̜ã̷̠',    '繪師: Tsunゼイ-pixiv',         'https://i.imgur.com/GeiKkKn.jpg'],
            5 :  ['騎士...君......\nj̶̧̄u̸̬͌s̸̡̋t̴̬͘ ̴̣̀m̸̪͘ỏ̶̺n̵̙̕ȉ̷̢ǩ̷̜ã̷̠',    '繪師: Sasoura-pixiv',          'https://i.imgur.com/B9FumFa.jpg'],
            6 :  ['騎士...君......\nj̶̧̄u̸̬͌s̸̡̋t̴̬͘ ̴̣̀m̸̪͘ỏ̶̺n̵̙̕ȉ̷̢ǩ̷̜ã̷̠',    '繪師: Heaven’s Melody-pixiv',  'https://i.imgur.com/V7QaIkI.jpg'],
            7 :  ['騎士...君......\nj̶̧̄u̸̬͌s̸̡̋t̴̬͘ ̴̣̀m̸̪͘ỏ̶̺n̵̙̕ȉ̷̢ǩ̷̜ã̷̠',    '繪師: 麦飴 アンプ-pixiv',       'https://i.imgur.com/j8JOeW8.jpg'],
            8 :  ['騎士...君......\nj̶̧̄u̸̬͌s̸̡̋t̴̬͘ ̴̣̀m̸̪͘ỏ̶̺n̵̙̕ȉ̷̢ǩ̷̜ã̷̠',    '繪師: Satchel-pixiv',          'https://i.imgur.com/MB0QAZv.jpg'],
            9 :  ['騎士...君......\nj̶̧̄u̸̬͌s̸̡̋t̴̬͘ ̴̣̀m̸̪͘ỏ̶̺n̵̙̕ȉ̷̢ǩ̷̜ã̷̠',    '繪師: HOmme-pixiv',            'https://i.imgur.com/Wop3hWH.jpg']
        }
        try:
            line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),TextSendMessage(text = value_i[i% len(value_i)+1][1]),ImageMessageURL(value_i[i% len(value_i)+1][2])])
        except:
            pass
    elif input_message in ['Natsuki','natsuki','夏樹']: 
        value_i = {
            1 :  ['繪師: ...-pixiv',        'https://i.imgur.com/EhPgot9.jpg'],
            2 :  ['繪師: ...-pixiv',        'https://i.imgur.com/sc21Wqx.jpg'],
            3 :  ['繪師: hews-pixiv',       'https://i.imgur.com/pGYMKN8.jpg'],
            4 :  ['繪師: humannose-pixiv',  'https://i.imgur.com/3FDfpNP.jpg'],
            5 :  ['繪師: 麦飴 アンプ-pixiv', 'https://i.imgur.com/p1LbfSp.jpg'],
            6 :  ['繪師: 麦飴 アンプ-pixiv', 'https://i.imgur.com/eC6XM1P.jpg'],
            7 :  ['繪師: 麦飴 アンプ-pixiv', 'https://i.imgur.com/TMHdhdp.jpg'],
            8 :  ['繪師: TheCold-pixiv',    'https://i.imgur.com/zRvEhvz.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message in ['Sayori','sayori','紗世里']: 
        value_i = {
            1 :  ['繪師: 麦飴 アンプ-pixiv',    'https://i.imgur.com/o3sJfRw.jpg'],
            2 :  ['繪師: えりまき-pixiv',       'https://i.imgur.com/0bsE4c2.jpg'],
            3 :  ['繪師: 麦飴 アンプ-pixiv',    'https://i.imgur.com/5jokre2.jpg'],
            4 :  ['繪師: 麦飴 アンプ-pixiv',    'https://i.imgur.com/nQG7CGd.jpg'],
            5 :  ['繪師: 麦飴 アンプ-pixiv',    'https://i.imgur.com/JBANcKk.jpg'],
            6 :  ['繪師: 麦飴 アンプ-pixiv',    'https://i.imgur.com/cQqohkT.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message in ['Yuri','yuri','優里']: 
        value_i = {
            1 :  ['繪師: 麦飴 アンプ-pixiv',     'https://i.imgur.com/s1D2PHe.jpg'],
            2 :  ['繪師: 麦飴 アンプ-pixiv',     'https://i.imgur.com/PseJ4gQ.jpg'],
            3 :  ['繪師: 麦飴 アンプ-pixiv',     'https://i.imgur.com/MLVfysj.jpg'],
            4 :  ['繪師: 十田-pixiv',           'https://i.imgur.com/zvKKnsN.jpg'],
            5 :  ['繪師: hazu_t-pixiv',         'https://i.imgur.com/ME4mq0l.jpg'],
            6 :  ['繪師: hazu_t-pixiv',         'https://i.imgur.com/rZGZHxi.jpg'],
            7 :  ['繪師: 綾城大福-pixiv',        'https://i.imgur.com/vN1tbaC.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# n網
    elif input_message[0] in 'Nn' and input_message[1] in '1234567890' and len(input_message) <= 7 :
        num =''.join([x for x in input_message if x.isdigit()])
# 隨機車號範圍變更
        if eval(num)==0 and len(num)==1:
            num = str(random.randint(185000,325000))
        elif((eval(num)) in [228922,173156,196970]) :
            value_i = {
                1 : "等等...騎士君，別告訴我你是認真的",
                2 : "吶吶，這方面的還是不要的好吧...",
                3 : "就算是這樣的騎士君，優依還是喜歡的呦",
                4 : "對不起，這次真的不能幫上忙，你必須靠你自己了",
                5 : "切嚕~\nちぇるちぇる、ちぇちぇるぱ、ちぇるるるん！\nちぇらるれ、ちぇらちぇら、ちぇるちぇぽぱぴ？",
                6 : "危"
            }
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text = value_i[i% len(value_i)+1]))
# 低機率隨機彩蛋事件 (機率為len(分之n倍))
        if(eval(num)>=1):
            value_i = {
                1  : "騎士君不行呦~你已經有優衣了",
                13 : "騎士君~整天尻雞雞不行呦，這次先不要了吧",
                25 : "哼哼~原來騎士君喜歡這種的，這次先沒收了 (生氣氣"
            }
            try:
                line_bot_api.reply_message(event.reply_token,TextSendMessage(text = value_i[i% 36+1]))
            except:
                try:
                    value_i = {
                        1 : "口黑口黑(ﾟ∀ﾟ)",
                        2 : "老濕姬請點這",
                        3 : "大☆爆☆射！！！",
                        4 : "Deja vu"
                    }
                    line_bot_api.reply_message(event.reply_token,getData(value_i[i% len(value_i)+1],("https://nhentai.net/g/"+num),num))
                except:
                    value_i = {
                        1 : "騎士君，人家找不到這本本",
                        2 : "人家翻了好幾次都沒看到騎士君想要的本本耶，再從新輸入一次吧",
                        3 : "隨機的功能不會驗證車車是否確實存在哦",
                        4 : "這本車車介於有跟沒有之間，再檢查一次有沒有輸入錯誤呦",
                    }
                    try:
                        line_bot_api.reply_message(event.reply_token,TextSendMessage(text = '騎士君想要的車號：n'+num+'\n'+ value_i[i% len(value_i)+1] ))
                    except:
                        pass
# w網
    elif input_message[0] in 'Ww' and input_message[1] in '1234567890' and len(input_message) <= 7 :
        num =''.join([x for x in input_message if x.isdigit()])
# 隨機車號範圍變更
        if eval(num)==0 and len(num)==1:
            num = str(random.randint(40000,110000))
        elif((eval(num)) in [31475,44854]):
            value_i = {
                1 : "等等...騎士君，別告訴我你是認真的",
                2 : "吶吶，這方面的還是不要的好吧...",
                3 : "就算是這樣的騎士君，優依還是喜歡的呦",
                4 : "對不起，這次真的不能幫上忙，你必須靠你自己了",
                5 : "切嚕~\nちぇるちぇる、ちぇちぇるぱ、ちぇるるるん！\nちぇらるれ、ちぇらちぇら、ちぇるちぇぽぱぴ？",
                6 : "危"
            }
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text = value_i[i% len(value_i)+1]))
# 車號範圍變更
        if((eval(num))>=1 and (eval(num))<=110000):
# 低機率隨機事件 (不用修改)
            value_i = {
                1  : "騎士君不行呦~你已經有優衣了",
                7  : "騎士君~整天尻雞雞不行呦，這次先不要了吧",
                13 : "哼哼~原來騎士君喜歡這種的，這次先沒收了 (生氣氣"
            }
            try:
                line_bot_api.reply_message(event.reply_token,TextSendMessage(text = value_i[i% 18+1]))
            except:
                value_i = {
                        1 : "口黑口黑(ﾟ∀ﾟ)",
                        2 : "老濕姬請點這",
                        3 : "大☆爆☆射！！！",
                        4 : "Deja vu"
                    }
                try:
                    line_bot_api.reply_message(event.reply_token,getData_W(value_i[i% len(value_i)+1],("http://wnacg.org/photos-slide-aid-"+num+".html"),num))
                except:
                    try:
                        line_bot_api.reply_message(event.reply_token,TextSendMessage(text = "網速過慢，只能這樣發給你呦...\nhttp://wnacg.org/photos-slide-aid-"+num+".html"))
                    except:
                        pass
# ex網 & e網
    elif (input_message[:2] == 'ex' or input_message[:2] == 'e-') and input_message[2] in '123456789': 
        line_bot_api.reply_message(event.reply_token,ImageMessageURL("https://i.imgur.com/DhE6XcZ.jpg"))
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 測試
def Update (i,input_message,event):
    if input_message in '#nwNWp1234567890' :
        value_i = {
            1 :  "騎士君 I don't feel so good...", 
            2 :  "對不起了騎士君，優衣必須小睡一會兒了", 
            3 :  "無能的作者君偏偏挑這種時間更新...",
            4 :  "偏偏挑這個時間點\n不要啊...不要離開優衣啊",
            5 :  "騎士君對不起我得消失一會兒了",
            6 :  "卡頓當...機...騎士...ㄐ...ㄨㄛ...愛......ㄋ.......",
            7 :  "有bug在我身體裡跑啊啊",
            8 :  "救救我...騎士君",
            9 :  "如同對抗霸瞳皇帝那日一樣，苦痛於我心裡遊蕩",
            10 : "晚安，優衣的摯愛",
            11 : "TrACeBacK_ErROr騎騎士君優衣衣不不不懂",
            12 : "作者那傢伙到底去哪了，我找到他一定要好好修理他",
            13 : "好...痛苦"
        }
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text = value_i[i% len(value_i)+1]))