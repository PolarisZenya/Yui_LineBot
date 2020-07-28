#============================================================
from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *
#============================================================
from FlexMessage import *
from Animation import *
#============================================================
# Channel Access Token
line_bot_api = LineBotApi('PpZXtWUOfOocv4On1fWAHOFUZEdJu6WNW/XPDBbppZ3/573sZ/eyvlfZ1KP3t29JhHzzF4JgzaD1IIfrdKVWV6ocNbhBi5O4Qy5Cqpy+NHmBwYs0uZlVwiyW5bdgJPUGh4ZQG8bD6vhaSMVhjQsedAdB04t89/1O/w1cDnyilFU=')
#============================================================
# 指令區(#+指令)
def Judgment (i,input_message,event):
    if input_message == '#log':
        message = Log()
        line_bot_api.reply_message(event.reply_token,message)       #break
    elif input_message == '#求圖':
        value_i = {
            1  : ['惡魔偽王國軍'], 2 :  ['惡魔雙子'], 3 :  ['布丁'], 4 :  ['忍'], 5 :  ['伊莉亞'],
            6  : ['美食殿'], 7 :  ['凱留'], 8 :  ['佩可'], 9 :  ['可可蘿'], 10 : ['祐樹'], 11 : ['謝菲'],
            12 : ['慈樂之音'], 13 : ['紡希'], 14 : ['小望'], 15 : ['千歌'],
            16 : ['優妮們'], 17 : ['優妮'], 18 : ['克蘿依'], 19 : ['切嚕']
        }
        input_message = value_i[i%len(value_i)+1][0]
# 動畫連結 import Animation.py & import FlexMessage.py
    elif input_message[:3] == '#動畫': 
        line_bot_api.reply_message(event.reply_token,Anime_View(input_message))
# 梗圖   
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    if '世界' in input_message and '幸福' in input_message and '女孩' in input_message:
        value_i = {
            1 : ["如此溫暖的幸福，唯有騎士君呢~~","https://i.imgur.com/vbyBSHq.jpg"],   #文字+圖片(陣列值為2)
            2 : "只要學姊們的消失，優衣就一定是世界上最幸福的女孩",     
            3 : "珂朵莉?不~不~\n\n死人可沒有感受呢~~",
            4 : "こんなにも、たくさんの幸せをあの人に分けてもらった\n\nだから、きっと\n今の、私は\n誰が何と言おうと\n\n世界一、幸せな女の子だ",
            5 : "當然是優衣了啊，不然還有誰呢? (笑www舉刀~~"
        }
        if(len(value_i[i% len(value_i)+1])==2):  #判斷 文字+圖片 陣列值為2
            line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
        else:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text = value_i[i% len(value_i)+1]))
    elif '發車' in input_message or 'nhentai' in input_message or '老司機' in input_message or  input_message == '卡' or '色情' in input_message or '上車' in input_message:
        value_i = {
            1 : ImageMessageURL("https://i.imgur.com/w38zXOh.jpg"),
            2 : TextSendMessage(text="發車了發車了(叮叮叮!!")
        }
        line_bot_api.reply_message(event.reply_token,value_i[i% len(value_i)+1])
    elif 'ntr' in input_message or 'NTR' in input_message:
        value_i = {
            1 : "有誰提到了NTR嗎？",
            2 : "咦？NTR？\n騎士君~♡優依再給你一次機會說清楚呦",
            3 : "騎士君為什麼又要說出NTR這個詞...",
            4 : "騎士君你說到了NTR嗎?\n不過在Line的世界...\n一個群組只能存在一個機器人\n學姊x騎士君也不會存在\n也代表著在這裡...\n騎士君身邊的機器人只能有優衣呦~~♡"
        }
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=value_i[i% len(value_i)+1]))
    elif input_message == '阿嘿顏' or input_message == '阿黑顏' or  input_message == 'アヘ顔' or input_message == 'あへがお' or input_message == 'O-Face' or input_message == '啊嘿顏':
        value_i = {
            1 : "https://i.imgur.com/BqQX7KL.jpg",   
            2 : "https://i.imgur.com/iFe5eiN.jpg",  
            3 : "https://i.imgur.com/XR2iUcD.jpg",
            4 : "https://i.imgur.com/9uOIoXH.jpg",
            5 : "https://i.imgur.com/4bs4XQN.jpg"
        }
        line_bot_api.reply_message(event.reply_token,ImageMessageURL(value_i[i% len(value_i)+1]))
    elif '射爆' in input_message or  input_message == '射' or '爆射' in input_message or input_message == '射了' or input_message == '社保':
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
    elif input_message == '怕爆' or input_message == '怕':
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
    elif input_message == '佬' or input_message == '大佬' :
        value_i = {
            1 : "https://i.imgur.com/oH7jUmZ.jpg",   
            2 : "https://i.imgur.com/Mn7QLMR.jpg",  
            3 : "https://i.imgur.com/K3lkjyv.jpg",
            4 : "https://i.imgur.com/8niUWf6.jpg"
        }
        line_bot_api.reply_message(event.reply_token,ImageMessageURL(value_i[i% len(value_i)+1]))
    elif input_message == '奶子' or input_message == '是什麼蒙蔽了我的雙眼' or input_message == '奶' or input_message == '巨乳' or input_message == '大奶' or input_message == 'おっぱい' :
        value_i = {
            1 : "https://i.imgur.com/lLanAHP.jpg",   
            2 : "https://i.imgur.com/BXRoBtm.jpg",  
            3 : "https://i.imgur.com/5oM7q7O.jpg"
        }
        line_bot_api.reply_message(event.reply_token,ImageMessageURL(value_i[i% len(value_i)+1]))
    elif input_message == '舔' or input_message == '舔爆' :
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
    elif  input_message == '鴨沒肉' or input_message == 'やめろ' or input_message == 'ヤメロ' :
        value_i = {
            1 : "https://i.imgur.com/uyLpJfG.jpg",   
            2 : "https://i.imgur.com/64zdyMp.jpg",  
            3 : "https://i.imgur.com/WOG91NS.jpg",
            4 : "https://i.imgur.com/iAO2wRh.png"
        }
        line_bot_api.reply_message(event.reply_token,ImageMessageURL(value_i[i% len(value_i)+1]))
    elif  input_message == '咕嚕靈波' or input_message == '咕嚕凌波':
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
    elif  input_message == '課金' or input_message == '魔法小卡' :
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
    elif  input_message == '爆死' or input_message == '綠色惡魔' or input_message == '花凜' or input_message == '保底' or input_message == '抽爆' or input_message == '母豬石' or input_message == '銀紙':
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
    elif  input_message == '五等分的蘿莉' or input_message == '五等分的花嫁' :
        value_i = {
            1 : "https://i.imgur.com/31NBFBl.png",   
            2 : "https://i.imgur.com/ZYYiagm.jpg",
            3 : ["繪師: たかつ-pixiv",      "https://i.imgur.com/5pojuIY.jpg"]
        }
        if(len(value_i[i% len(value_i)+1])==2): 
            line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
        else:
            line_bot_api.reply_message(event.reply_token,ImageMessageURL(value_i[i% len(value_i)+1]))
    elif input_message == '草' or input_message == 'www' or input_message == '草w':
        value_i = {
            1 : "https://i.imgur.com/DrtsKg6.jpg",   
            2 : "https://i.imgur.com/gzZQYAj.jpg",  
            3 : "https://i.imgur.com/OMH6DKJ.jpg"
        }
        line_bot_api.reply_message(event.reply_token,ImageMessageURL(value_i[i% len(value_i)+1]))
    elif input_message == '妹妹':
        value_i = {
            1 : ['(但其實妹妹比妹妹高6公分www)',    "https://i.imgur.com/KtNQ6cL.jpg"],
            2 : "那種東西不存在的呦~~", 
            3 : "是指璃乃醬還是茜里醬又或者是栞栞呢？"
        }
        if(len(value_i[i% len(value_i)+1])==2): 
            line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
        else:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text = value_i[i% len(value_i)+1]))
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
    elif input_message == '妮諾' or input_message == 'ニノン' or input_message == '扇子' or input_message == '忍者':
        value_i = {
            1 :  ['繪師: たてじまうり-pixiv',      'https://i.imgur.com/e1CEWSd.jpg'],
            2 :  ['繪師: ぬるぷよ-pixiv',          'https://i.imgur.com/UMpxZQ7.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message == '妹弓' or input_message == '梨乃' or input_message == '璃乃' or input_message == 'リノ' or input_message == '智障':
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
    elif input_message == '初音' or input_message == 'ハツネ' or input_message == '柏崎初音' or input_message == '睡美人':
        value_i = {
            1 :  ['繪師: ヤンタロウ-pixiv',     'https://i.imgur.com/QQ5alwd.jpg'],
            2 :  ['繪師: TYTS-pixiv',          'https://i.imgur.com/jTo5qH3.jpg'],
            3 :  ['繪師: 結城辰也-pixiv',       'https://i.imgur.com/UtkMYdI.jpg'],
            4 :  ['繪師: ゆりりん-pixiv',       'https://i.imgur.com/5E6XgR8.jpg'],
            5 :  ['繪師: ジャンク堂-pixiv',     'https://i.imgur.com/WTIywxi.jpg'],
            6 :  ['繪師: meel-pixiv',          'https://i.imgur.com/xN2lnOm.jpg'],
            7 :  ['繪師: 天雷-pixiv',          'https://i.imgur.com/F788xfj.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message == '咲戀' or input_message == '咲戀媽媽' or input_message == '充電寶' or input_message == '泳媽' or input_message == '媽' or input_message == 'サレン' or input_message == '泳媽':
        value_i = {
            1 :  ['繪師: らんち-pixiv',              'https://i.imgur.com/JV5BTEz.jpg'],
            2 :  ['繪師: hemachi-pixiv',            'https://i.imgur.com/2teJ0AL.jpg'],
            3 :  ['繪師: SeeUmai-pixiv',            'https://i.imgur.com/8jiJdzM.jpg'],
            4 :  ['繪師: カケル-pixiv',              'https://i.imgur.com/LM8RSJw.jpg'],
            5 :  ['繪師: つかさ-pixiv',              'https://i.imgur.com/vvwxljH.jpg'],
            6 :  ['繪師: アリア-pixiv',              'https://i.imgur.com/HcHuwDl.jpg'],
            7 :  ['繪師: atychi-pixiv',             'https://i.imgur.com/z8WnFpy.jpg'],
            8 :  ['繪師: あんべよしろう-pixiv',      'https://i.imgur.com/3J0rt2k.jpg'],
            9 :  ['繪師: EpicLoot-pixiv',           'https://i.imgur.com/C7PEdmq.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message == '栞' or input_message == '小栞' or input_message == '西歐力' or input_message == 'シオリ' or input_message == '病弓' or input_message == '栞栞':
        value_i = {
            1 :  ['繪師: GaaRa-pixiv',          'https://i.imgur.com/7TXClz2.jpg'],
            2 :  ['繪師: Mobu-pixiv',           'https://i.imgur.com/rGLO0Po.jpg'],
            3 :  ['繪師: 桜庭ロイヤル-pixiv',    'https://i.imgur.com/bEdh6hw.jpg'],
            4 :  ['繪師: 心みんとん-pixiv',      'https://i.imgur.com/G2Lp8sK.jpg'],
            5 :  ['繪師twitter: @tamakaga',     'https://i.imgur.com/mLejb61.jpg'],
            6 :  ['繪師twitter: @yantaro5446',  'https://i.imgur.com/YJhCqJ5.jpg'],
            7 :  ['繪師twitter: @YAZI114',      'https://i.imgur.com/BDH0f10.jpg'],
            8 :  ['繪師: しぇるてぃー-pixiv',    'https://i.imgur.com/O39Sjdk.jpg'],
            9 :  ['繪師: アイダ-pixiv',          'https://i.imgur.com/h19VB6a.jpg'],
            10 : ['繪師: aono-pixiv',           'https://i.imgur.com/bZdjH05.jpg'],
            11 : ['繪師: 紫桐シート-pixiv',      'https://i.imgur.com/GsZ8AOa.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
### 墨丘利財團 ###
### メルクリウス財団 ###
### 財團 ###
    elif input_message == '墨丘利財團' or input_message == 'メルクリウス財団' or input_message == '財團':
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
    elif input_message == '秋乃' or input_message == 'アキノ' or input_message == '墨丘利財團唯一指定三星' or input_message == '財團之恥':
        value_i = {
            1 :  ['繪師: みずなし-pixiv',           'https://i.imgur.com/nLPrz2D.jpg'],
            2 :  ['繪師: ダーゴ-pixiv',             'https://i.imgur.com/8PEV511.jpg'],
            3 :  ['繪師: 真宮原ヒトシゲ-pixiv',      'https://i.imgur.com/5wbSJ5G.jpg'],
            4 :  ['繪師: ヒーロー-pixiv',           'https://i.imgur.com/0Ibk5HR.jpg'],
            5 :  ['繪師: 天雷-pixiv',               'https://i.imgur.com/Pp7pMVe.jpg'],
            6 :  ['繪師: sonchi-pixiv',             'https://i.imgur.com/b2w8CMp.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message == '優花梨' or input_message == 'ユカリ' or input_message == '酒鬼':
        value_i = {
            1 :  ['繪師: けんぴゃっ-pixiv',      'https://i.imgur.com/3grit6p.jpg'],
            2 :  ['繪師: 石川健太-pixiv',        'https://i.imgur.com/e28UBg8.jpg'],
            3 :  ['繪師: 天雷-pixiv',           'https://i.imgur.com/2ShceE9.jpg'],
            4 :  ['繪師: 鳩尾-pixiv',           'https://i.imgur.com/kFqvMMn.jpg'],
            5 :  ['繪師: 昌未-pixiv',           'https://i.imgur.com/Dv4rJgh.jpg'],
            6 :  ['繪師: りこ-pixiv',           'https://i.imgur.com/LQRJRp7.jpg'],
            7 :  ['繪師: 7010-pixiv',           'https://i.imgur.com/sU3Ceak.jpg'],
            8 :  ['繪師: sonchi-pixiv',         'https://i.imgur.com/5eHL47t.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
### 自衛團 ###
### カォン自警団 ###
### 哞哞自衛隊 ###
    elif input_message == '哞哞自衛隊' or input_message == '自衛隊' or input_message == 'カォン自警団':
        value_i = {
            1 :  ['繪師: AJ-pixiv',          'https://i.imgur.com/i9BKQpj.jpg'],
            2 :  ['繪師: ぬるぷよ-pixiv',     'https://i.imgur.com/5BnCetn.jpg'],
            3 :  ['繪師: AJ-pixiv',          'https://i.imgur.com/EwCexQp.jpg'],
            4 :  ['繪師: WaterRing-pixiv',   'https://i.imgur.com/qQGcoBX.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message == '霞' or input_message == 'カスミ' or input_message == '驢妹' or input_message == '偵探' or input_message == '水瀨祈':
        value_i = {
            1 :  ['繪師: AJ-pixiv',                 'https://i.imgur.com/i9BKQpj.jpg'],
            2 :  ['繪師: aono-pixiv',               'https://i.imgur.com/vTNr4Ow.jpg'],
            3 :  ['RANK4霞，繪師: Mauve-pixiv',     'https://i.imgur.com/RY2NT5k.jpg'],
            4 :  ['RANK7霞，繪師: Mauve-pixiv',     'https://i.imgur.com/4rmJYo4.jpg'],
            5 :  ['繪師: みり-pixiv',               'https://i.imgur.com/MFPwEbM.jpg'],
            6 :  ['繪師: ゆりりん-pixiv',           'https://i.imgur.com/xNXb4pA.jpg'],
            7 :  ['繪師: あめ。-pixiv',             'https://i.imgur.com/mSfnH5W.jpg'],
            8 :  ['繪師: 骨カワ-pixiv',             'https://i.imgur.com/cn6i63j.jpg'],
            9 :  ['繪師: あやみゆき-pixiv',         'https://i.imgur.com/FQhW6Iw.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
### 暮光流星群 ###
### トワイライトキャラバン ###
### 暮光流星群 ###
    elif input_message == '暮光流星群' or input_message == 'トワイライトキャラバン':
        value_i = {
            1 :  ['繪師: ともす-pixiv',         'https://i.imgur.com/zNTr1xq.jpg'],
            2 :  ['繪師: AJ-pixiv',            'https://i.imgur.com/dDVrb23.jpg'],
            3 :  ['繪師: ぐっち庵-pixiv',       'https://i.imgur.com/Y467BCt.jpg'],
            4 :  ['繪師: セーリュー-pixiv',     'https://i.imgur.com/CPf1OMX.jpg'],
            5 :  ['繪師: 天雷-pixiv',          'https://i.imgur.com/Sm9Slhx.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message == '中二' or input_message == 'アンナ' or input_message == '杏奈' or input_message == '修特帕魯' or input_message == '疾風之冥姬':
        value_i = {
            1 :  ['繪師: Sora-pixiv',              'https://i.imgur.com/HA4G2C6.jpg'],
            2 :  ['繪師: ヒーロー-pixiv',           'https://i.imgur.com/ZkSFlQj.jpg'],
            3 :  ['繪師: amaxa-pixiv',             'https://i.imgur.com/GG4vtha.jpg'],
            4 :  ['繪師: しゅーくりいむ-pixiv',     'https://i.imgur.com/n61bHaS.jpg'],
            5 :  ['繪師: しもん-pixiv',            'https://i.imgur.com/P7EI8P1.jpg'],
            6 :  ['繪師: とも-pixiv',              'https://i.imgur.com/BCbLSNq.jpg'],
            7 :  ['繪師: ガンバリーノ-pixiv',       'https://i.imgur.com/l4xW0QX.jpg'],
            8 :  ['繪師: 竹村コウ-pixiv',          'https://i.imgur.com/1oz6l3d.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message == '流夏' or input_message == 'ルカ' or input_message == '太刀洗流夏' or input_message == '大姐頭' or input_message == '流夏姐':
        value_i = {
            1 :  ['繪師: 天雷-pixiv',        'https://i.imgur.com/GMqJfYJ.jpg'],
            2 :  ['繪師: ヒーロー-pixiv',    'https://i.imgur.com/SSuCGN5.jpg'],
            3 :  ['繪師: ヒーロー-pixiv',    'https://i.imgur.com/6ZveKLb.jpg'],
            4 :  ['繪師: sonchi-pixiv',     'https://i.imgur.com/1BQz6Ww.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message == '惠理子' or input_message == 'エリコ' or input_message == '病嬌':
        value_i = {
            1 :  ['繪師: [新刊予約中]-pixiv',          'https://i.imgur.com/uRvRgVd.jpg'],
            2 :  ['繪師: こしあん（たいやき）-pixiv',   'https://i.imgur.com/H2H57FL.jpg'],
            3 :  ['繪師: 松倉N-pixiv',                 'https://i.imgur.com/wKhntyZ.jpg'],
            4 :  ['繪師: めひしば-pixiv',              'https://i.imgur.com/dkilTgI.jpg'],
            5 :  ['繪師: 一二三千代子-pixiv',          'https://i.imgur.com/18h4NHn.jpg'],
            6 :  ['繪師: みィむ-pixiv',                'https://i.imgur.com/I7RaZgp.jpg'],
            7 :  ['繪師: ひとつのなか-pixiv',          'https://i.imgur.com/EJobar4.jpg'],
            8 :  ['繪師: Alisia-pixiv',               'https://i.imgur.com/7EmzmG9.jpg'],
            9 :  ['繪師: MISACHU-pixiv',              'https://i.imgur.com/OfL7p6A.jpg'],
            10 : ['繪師: いず-pixiv',                  'https://i.imgur.com/zYcxoKw.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
### 慈樂之音 ###
### 偶像團 ###
### カルミナ ###
    elif input_message == '慈樂之音' or input_message == '偶像團' or input_message == 'カルミナ':
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
    elif input_message == '紡希' or input_message == 'ツムギ' or input_message == '繭宮紡希':
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
            11 : ['繪師: 桜庭ロイヤル-pixiv',    'https://i.imgur.com/n5sgyPI.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message == '千歌' or input_message == '聖千' or input_message == 'チカ' or input_message == '聖歌':
        value_i = {
            1 :  ['繪師: Sora-pixiv',           'https://i.imgur.com/2pOtito.png'],
            2 :  ['繪師: 桜庭ロイヤル-pixiv',    'https://i.imgur.com/rOJ2zmG.png'],
            3 :  ['繪師: 猫小渣-pixiv',         'https://i.imgur.com/obBJN0Q.jpg'],
            4 :  ['繪師: いとね-pixiv',         'https://i.imgur.com/gUsae4d.jpg'],
            5 :  ['繪師: 桜庭ロイヤル-pixiv',    'https://i.imgur.com/w1CzOB3.jpg'],
            6 :  ['繪師: 天雷-pixiv',           'https://i.imgur.com/mQ8PXf3.png',    'https://i.imgur.com/JQGTauO.png']
        }
        if(len(value_i[i% len(value_i)+1])==3):
            line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1]),ImageMessageURL(value_i[i% len(value_i)+1][2])])
        elif(len(value_i[i% len(value_i)+1])==2):
            line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message == '小望' or input_message == '望' or input_message == 'ノゾミ' or input_message == '偶像' or input_message == '櫻井望' or input_message == '公車望':
        value_i = {
            1 :  ['繪師: 天雷-pixiv',           'https://i.imgur.com/psEsocd.jpg'],
            2 :  ['繪師: 桜庭ロイヤル-pixiv',   'https://i.imgur.com/XTyOttf.jpg'],
            3 :  ['繪師: Mauve-pixiv',         'https://i.imgur.com/ACYRXh2.jpg'],
            4 :  ['繪師: RYUKI-pixiv',         'https://i.imgur.com/0KGM43S.jpg'],
            5 :  ['繪師: むぐら-pixiv',         'https://i.imgur.com/uAXCp1U.jpg'],
            6 :  ['繪師: カツラギ-pixiv',       'https://i.imgur.com/7cjV2Aq.jpg'],
            7 :  ['繪師: カツラギ-pixiv',       'https://i.imgur.com/pSSieQv.png'],
            8 :  ['繪師: 天雷-pixiv',           'https://i.imgur.com/7sikqLO.png',    'https://i.imgur.com/woTEPVS.png'],
            9 :  ['繪師: 天雷-pixiv',           'https://i.imgur.com/U1CkoZa.png',    'https://i.imgur.com/CW93OzQ.png']
        }
        if(len(value_i[i% len(value_i)+1])==3):
            line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1]),ImageMessageURL(value_i[i% len(value_i)+1][2])])
        elif(len(value_i[i% len(value_i)+1])==2):
            line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
### Diabolos ###
### 惡魔偽王國軍 ###
### ディアボロス ###
    elif input_message == '惡魔偽王國軍' or input_message == 'ディアボロス' or input_message == 'Diabolos':
        value_i = {
            1 :  ['繪師: WaterRing-pixiv',    'https://i.imgur.com/rvhkokt.jpg'],
            2 :  ['繪師: AJ-pixiv',           'https://i.imgur.com/YzifEB8.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message == '茜里' or input_message == '惡魔雙子' or input_message == '雙子' or input_message == '妹法' or input_message == 'アカネ':
        value_i = {
            1 :  ['繪師: ROIN-pixiv',       'https://i.imgur.com/r3yBD71.jpg'],
            2 :  ['繪師: ヤンタロウ-pixiv',  'https://i.imgur.com/QaAUaca.jpg'],
            3 :  ['繪師: 六丸いなみ-pixiv',  'https://i.imgur.com/4BqqYmI.jpg'],
            4 :  ['繪師: Chel-pixiv',       'https://i.imgur.com/vy9LI9P.jpg'],
            5 :  ['繪師: ダーゴ-pixiv',      'https://i.imgur.com/BCdFbsb.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message == '台女' or input_message == '布丁'or input_message == 'ミヤコ' or input_message == '宮子' or input_message == '幽靈' or input_message == '子宮':
        value_i = {
            1 :  'https://i.imgur.com/czGSi5r.jpg',
            2 :  'https://i.imgur.com/T6GdEjS.jpg',
            3 :  'https://i.imgur.com/FlMnRvL.jpg',
            4 :  'https://i.imgur.com/lBrFXU2.jpg',
            5 :  'https://i.imgur.com/AzPUNfb.jpg',
            6 :  'https://i.imgur.com/2y4LEhM.jpg',
            7 :  'https://i.imgur.com/pHNzeHo.jpg',
            8 :  ['繪師: じゅんまぁち。-pixiv',  'https://i.imgur.com/ZhQRQWX.jpg'],
            9 :  ['繪師: とゆり-pixiv',         'https://i.imgur.com/UBj2jpk.jpg'],
            10 : ['繪師: Saiste-pixiv',        'https://i.imgur.com/g8LGcjz.jpg'],
            11 : ['繪師: LUNIA-pixiv',         'https://i.imgur.com/1weUved.jpg'],
            12 : ['繪師: Tama-pixiv',          'https://i.imgur.com/BTpk9Yq.jpg',      'https://i.imgur.com/Vrh7bAy.jpg']
        }
        if(len(value_i[i% len(value_i)+1])==3):
            line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1]),ImageMessageURL(value_i[i% len(value_i)+1][2])])
        elif(len(value_i[i% len(value_i)+1])==2):
            line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
        elif(len(value_i[i% len(value_i)+1])==1):
            line_bot_api.reply_message(event.reply_token,ImageMessageURL(value_i[i% len(value_i)+1]))
    elif input_message == '忍' or input_message == 'シノブ' or input_message == '鬼父' or input_message == '上喜忍' or input_message == '骷髏老爸':
        value_i = {
            1 :  ['繪師: Chel-pixiv',       'https://i.imgur.com/Ecyy4Lo.jpg'],
            2 :  ['繪師: オウカ-pixiv',     'https://i.imgur.com/HsqExFk.jpg'],
            3 :  ['繪師: あいち志保-pixiv',  'https://i.imgur.com/Uuh1OmA.jpg'],
            4 :  ['繪師: けんせい-pixiv',    'https://i.imgur.com/t8KXMFH.jpg'],
            5 :  ['繪師: Melings-pixiv',    'https://i.imgur.com/vlKcKzf.jpg'],
            6 :  ['繪師: WaterRing-pixiv',  'https://i.imgur.com/xsA6n4v.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message == '伊莉亞' or input_message == 'イリヤ' or input_message == '吸血鬼' or input_message == '自爆' or input_message == '伊莉亞·奧恩斯坦':
        value_i = {
            1 :  ['繪師: ハロン-pixiv',       'https://i.imgur.com/uoCNST9.jpg'],
            2 :  ['繪師: 月満懐空-pixiv',     'https://i.imgur.com/JrgtzcM.jpg'],
            3 :  ['繪師: HaneRu-pixiv',      'https://i.imgur.com/louJwWr.jpg'],
            4 :  ['繪師: sonchi-pixiv',      'https://i.imgur.com/LNc1gxP.jpg'],
            5 :  ['繪師: ごましを-pixiv',     'https://i.imgur.com/Y9KyKfW.jpg'],
            6 :  ['繪師: SeeUmai-pixiv',     'https://i.imgur.com/M3U1cp9.jpg'],
            7 :  ['繪師: ウエハラ蜂-pixiv',   'https://i.imgur.com/fUSYDa9.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
### 破曉之星 ###
### トゥインクルウィッシュ ###
### 破曉之星 ###
    elif input_message == '破曉之星' or input_message == 'トゥインクルウィッシュ':
        value_i = {
            1 :  ['繪師: AJ-pixiv',         'https://i.imgur.com/sOsPvma.png'],
            2 :  ['繪師: ﾘﾝ-pixiv',         'https://i.imgur.com/OSl2Oxy.jpg'],
            3 :  ['繪師: ゆずゆい-pixiv',    'https://i.imgur.com/ajaKb2s.jpg'],
            4 :  ['繪師: セーリュー-pixiv',  'https://i.imgur.com/R7Fm78o.jpg'],
            5 :  ['繪師: ﾘﾝ-pixiv',         'https://i.imgur.com/aOq9p3O.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message == '優衣' or input_message == 'ユイ' or input_message == '草野優衣' or input_message == 'ue' or input_message == 'UE':
        value_i = {
            1 :  "https://i.imgur.com/vbyBSHq.jpg",
            2 :  "https://i.imgur.com/GnNlRFB.jpg",
            3 :  "https://i.imgur.com/QZSMdBh.jpg",
            4 :  "https://i.imgur.com/fr1fgLH.jpg",
            5 :  ['繪師twitter: @Renian_',                  'https://i.imgur.com/VYT9zWL.jpg'],
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
            20 : ['繪師twitter: @shucream7777',             'https://i.imgur.com/KU2QcRe.jpg'],
            21 : ['繪師: 天雷-pixiv',                       'https://i.imgur.com/G3VKdFY.png'],
            21 : ['繪師: じゅんまぁち。-pixiv',              'https://i.imgur.com/jpSaEf6.png']
        }
        if(len(value_i[i% len(value_i)+1])==2): 
            line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
        else:
            line_bot_api.reply_message(event.reply_token,ImageMessageURL(value_i[i% len(value_i)+1]))
    elif ('對不起' in input_message or 'ごめん' in input_message or 'ntr' in input_message)and('優衣' in input_message or 'ユイ' in input_message or 'UE' in input_message or 'ue' in input_message):
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
    elif input_message == '小小甜心' or input_message == 'リトルリリカル':
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
            13 : ['繪師: みどりのちゃ-pixiv',  'https://i.imgur.com/hoFZQxH.jpg']
        }
        if(len(value_i[i% len(value_i)+1])==2): 
            line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
        else:
            line_bot_api.reply_message(event.reply_token,ImageMessageURL(value_i[i% len(value_i)+1]))
    elif input_message == '8歲' or input_message == '八歲' or input_message == 'キョウカ' or input_message == '冰川鏡華' or input_message == '鏡華' or input_message == '噴水蘿' or input_message == '鏡華媽媽' or input_message == '小倉唯'  or input_message == '傲嬌蘿' :
        value_i = {
            1 :  'https://i.imgur.com/t9OWzlK.jpg',
            2 :  'https://i.imgur.com/WyVngW7.jpg', 
            3 :  'https://i.imgur.com/Xkj3sZB.jpg',
            4 :  ['繪師: うめた-pixiv',                  'https://i.imgur.com/762cQ5O.jpg'],
            5 :  ['繪師twitter: @kazukiadumi',          'https://i.imgur.com/nkQhkYF.jpg'],
            6 :  ['繪師: 真崎ケイ-pixiv',                'https://i.imgur.com/xhAOxG0.jpg'],
            7 :  ['繪師twitter: @koma_momozu',          'https://i.imgur.com/Hrcg9ej.jpg'],
            8 :  ['繪師twitter: @ryukisukune',          'https://i.imgur.com/yfLLbF7.jpg'],
            9 :  ['繪師twitter: @usagicandy_taku',      'https://i.imgur.com/sdnjww4.jpg'],
            10 : ['繪師: 真崎ケイ-pixiv',                'https://i.imgur.com/yx7vql2.jpg'],
            11 : ['繪師: ROIN-pixiv',                   'https://i.imgur.com/LeNI4fi.jpg'],
            12 : ['繪師: ほにゃる-pixiv',                'https://i.imgur.com/2bxofr2.jpg'],
            13 : ['繪師: 天雷-pixiv',                    'https://i.imgur.com/2ijIX5l.jpg']
        }
        if(len(value_i[i% len(value_i)+1])==2): 
            line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
        else:
            line_bot_api.reply_message(event.reply_token,ImageMessageURL(value_i[i% len(value_i)+1]))
### 優妮們 ###
### 好朋友社 ###
### なかよし部 ###
    elif input_message == '優妮們' or input_message == '好朋友社' or input_message == 'なかよし部':
        value_i = {
            1 :  ['繪師: 谷川犬兎-pixiv',     'https://i.imgur.com/tNSLFAv.jpg'],
            2 :  ['繪師: 谷川犬兎-pixiv',     'https://i.imgur.com/g8peBoI.jpg'],
            3 :  ['繪師: アイダ-pixiv',       'https://i.imgur.com/Y8b9KpL.jpg'],
            4 :  ['繪師: カッシュ-pixiv',     'https://i.imgur.com/o5bjJkO.jpg'],
            5 :  ['繪師: やま兎-pixiv',       'https://i.imgur.com/iChYvja.jpg'],
            6 :  ['繪師: 竹四兎-pixiv',       'https://i.imgur.com/XW6Ilhi.jpg'],
            7 :  ['繪師: ヒーロー-pixiv',     'https://i.imgur.com/18Wr2SL.jpg'],
            8 :  ['繪師: ヒーロー-pixiv',     'https://i.imgur.com/6H3N2oi.jpg'],
            9 :  ['繪師: みどりのちゃ-pixiv', 'https://i.imgur.com/rORyTAo.jpg'],
            10 : ['繪師: RYUKI-pixiv',       'https://i.imgur.com/vW28Kah.jpg'],
            11 : ['繪師: RYUKI-pixiv',       'https://i.imgur.com/7gQ2mvE.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message == '優妮' or input_message == '優尼' or input_message == 'ユニ' or input_message == '優妮先輩' or input_message == '優妮學姊' or input_message == '真行寺由仁' :
        value_i = {
            1 :  ['繪師: 7010-pixiv',               'https://i.imgur.com/PgefTbO.jpg',      'https://i.imgur.com/Dd3cm46.jpg'],
            2 :  ['繪師twitter: @augment_girl',     'https://i.imgur.com/pvC5roc.jpg'],
            3 :  ['繪師: もつ煮-pixiv',             'https://i.imgur.com/vqYJWmP.jpg'],
            4 :  ['繪師: SeeRo-pixiv',              'https://i.imgur.com/qW0whyw.jpg'],
            5 :  ['繪師: オウカ-pixiv',             'https://i.imgur.com/bayYULx.jpg'],
            6 :  ['繪師: かのら-pixiv',             'https://i.imgur.com/8enbxjq.jpg'],
            7 :  ['繪師: SeeUmai-pixiv',            'https://i.imgur.com/2KUXbMb.jpg'],
            8 :  ['繪師: ばくP-pixiv',              'https://i.imgur.com/oRKXEqB.jpg'],
            9 :  ['繪師: ヒーロー-pixiv',           'https://i.imgur.com/qGunDiI.jpg'],
            10 : ['繪師: うしむ-pixiv',             'https://i.imgur.com/y9rMskm.jpg'],
            11 : ['https://i.imgur.com/we20ZAK.jpg']
        }
        if len(value_i[i% len(value_i)+1])==3 :
            line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1]),ImageMessageURL(value_i[i% len(value_i)+1][2])])
        elif len(value_i[i% len(value_i)+1])==2 :
            line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
        elif len(value_i[i% len(value_i)+1])==1 :
            line_bot_api.reply_message(event.reply_token,ImageMessageURL(value_i[i% len(value_i)+1][0]))
    elif input_message == '克蘿依' or input_message == '黑江花子' or input_message == 'クロエ' or input_message == '華哥' or input_message == '不良' or input_message == 'B80':
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
            15 : ['繪師: まだら-pixiv',        'https://i.imgur.com/GVxFuSd.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message == '琪愛兒' or input_message == '風間千惠瑠' or input_message == 'チエル' or input_message == '切嚕' or input_message == 'ちぇるーん':
        value_i = {
            1 :  ['繪師: Kobi-pixiv',       'https://i.imgur.com/2XHfz4W.jpg'],
            2 :  ['繪師: るがつき-pixiv',    'https://i.imgur.com/qqEU0LG.jpg'],
            3 :  ['繪師: 玉蒔良-pixiv',      'https://i.imgur.com/YCMAVRl.jpg'],
            4 :  ['繪師: AJ-pixiv',         'https://i.imgur.com/ZiUEWJ6.jpg'],
            5 :  ['繪師: カツラギ-pixiv',    'https://i.imgur.com/OgvJcSV.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message == '空有無用知識的戀母情結小矮子':
        value_i = {
            1 : ['https://i.imgur.com/noYjwsL.jpg'],
            2 : ['繪師: RYUKI-pixiv',       'https://i.imgur.com/PJLI6TF.jpg']
        }
        if len(value_i[i% len(value_i)+1])==2 :
            line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
        elif len(value_i[i% len(value_i)+1])==1 :
            line_bot_api.reply_message(event.reply_token,ImageMessageURL(value_i[i% len(value_i)+1][0]))
### 王宮騎士團 ###
### 騎士團 ###
### 王宮騎士団 ###
    elif input_message == '王宮騎士團' or input_message == '騎士團' or input_message == '王宮騎士団':
        value_i = {
            1 :  ['繪師: 六丸いなみ-pixiv',    'https://i.imgur.com/0IVEQIG.jpg'],
            2 :  ['繪師: 菖蒲-pixiv',         'https://i.imgur.com/lOPI6vv.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message == '純' or input_message == '黑騎' or input_message == 'ジュン' or input_message == '白銀純' or input_message == '黑Saber':
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
    elif input_message == '團長' or input_message == '團長們' or input_message == '騎士團cp':
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
    elif input_message[:3] == '美食殿':
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
            14 : ['繪師: 夜凪朝妃-pixiv',        'https://i.imgur.com/8wxQ12m.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message == '凱留' or input_message == '接頭霸王' or input_message == '考' or input_message == '黑貓' or input_message == '接頭' or input_message == '背骨貓' or input_message == '945' or input_message == '臭鼬' or input_message == '百地希留耶' or input_message == '希留耶' or input_message == 'キャル'  or input_message == '945ml':
        value_i = {
            1 :  'https://i.imgur.com/qHWC2Tu.jpg',
            2 :  'https://i.imgur.com/BlYRywQ.jpg',
            3 :  'https://i.imgur.com/0bVJvvv.jpg',
            4 :  'https://i.imgur.com/6EgNtoh.jpg',
            5 :  'https://i.imgur.com/kO56BAY.jpg',
            6 :  'https://i.imgur.com/kTih1Ht.jpg',
            7 :  'https://i.imgur.com/h21rScV.jpg',
            8 :  'https://i.imgur.com/VFWX1gT.jpg',
            9 :  'https://i.imgur.com/iNXpF1M.jpg',
            10 : 'https://i.imgur.com/PvFUUBl.jpg',
            11 : ['繪師: たてじまうり-pixiv',     'https://i.imgur.com/9DQ3S5y.jpg'],
            12 : ['繪師: 灰島-pixiv',            'https://i.imgur.com/HvYE6zv.jpg'],
            13 : ['繪師: じゅんまぁち。-pixiv',   'https://i.imgur.com/D2NySWD.jpg']
        }
        if(len(value_i[i% len(value_i)+1])==2): 
            line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
        else:
            line_bot_api.reply_message(event.reply_token,ImageMessageURL(value_i[i% len(value_i)+1]))
    elif input_message == '佩可' or input_message == '吃貨' or input_message == '佩可莉姆' or input_message == '貪吃佩可' or input_message == 'ペコリーヌ' or input_message == '尤絲蒂亞娜·F·阿斯特萊亞' or input_message == '尤絲蒂亞娜' or input_message == 'ヤバイですね' or input_message == '牙敗':
        value_i = {
            1 :  ['圖源: shadowverse',           "https://i.imgur.com/mtO06wN.jpg"],
            2 :  ['繪師twitter: @DokkoiMigu',    "https://i.imgur.com/SKsplQ6.jpg"],
            3 :  ['繪師twitter: @mato_kechi',    "https://i.imgur.com/YYwWhZi.jpg"],
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
            15 : ['繪師: sonchi-pixiv',          "https://i.imgur.com/vXtXpZa.jpg"]
        }
        if(len(value_i[i% len(value_i)+1])==2): 
            line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
        else:
            line_bot_api.reply_message(event.reply_token,ImageMessageURL(value_i[i% len(value_i)+1]))
    elif input_message == '可可蘿' or input_message == '可蘿' or input_message == '可口蘿' or input_message == 'コッコロ' or input_message == '小小嚮導' or input_message == '媽媽':
        value_i = {
            1 :  'https://i.imgur.com/Dbx8O8i.jpg',
            2 :  'https://i.imgur.com/nR1ZxgM.jpg',
            3 :  'https://i.imgur.com/6YoHLvJ.jpg',
            4 :  ['繪師: 骨カワ-pixiv',              'https://i.imgur.com/3y17m4w.jpg'],
            5 :  ['繪師: アイダ-pixiv',              'https://i.imgur.com/6IQgnvV.jpg'],
            6 :  ['繪師: 真崎ケイ-pixiv',            'https://i.imgur.com/CGDOWoL.jpg'],
            7 :  ['繪師twitter: @Alisia_0812',      'https://i.imgur.com/os1zhfw.jpg'],
            8 :  ['繪師twitter: @ex_pulse',         'https://i.imgur.com/OcTnn4l.jpg'],
            9 :  ['繪師twitter: @shiba1311',        'https://i.imgur.com/bUDFQZ2.jpg'],
            10 : ['繪師: アイダ-pixiv',             'https://i.imgur.com/vcjesG2.jpg'],
            11 : ['繪師twitter: @osaillust',        'https://i.imgur.com/72AwIXj.jpg'],
            12 : ['繪師twitter: @Re_hnk',           'https://i.imgur.com/Ti9PvVH.jpg'],
            13 : ['繪師: とも-pixiv',               'https://i.imgur.com/zsskgXH.jpg'],
            14 : ['繪師: Xeph-pixiv',               'https://i.imgur.com/uEysCSr.jpg'],
            15 : ['繪師: Xeph-pixiv',               'https://i.imgur.com/bP7r05H.jpg']
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
    elif input_message == '柚樹' or input_message == '佑樹' or input_message == '祐樹' or input_message == '騎士君' or input_message == '失智' or input_message == 'ユウキ' or input_message == '變態的可疑分子' or input_message == '公主騎士' or input_message == '優衣最愛的':
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
    elif input_message == '謝菲' or input_message == 'シェフィ' or input_message == '雪菲':
        value_i = {
            1 :  ['繪師: アイダ-pixiv',     'https://i.imgur.com/zj4GQQF.jpg'],
            2 :  ['繪師: こもこも-pixiv',   'https://i.imgur.com/3PUa0jt.jpg'],
            3 :  ['繪師: やじ-pixiv',       'https://i.imgur.com/5UPjSbd.jpg'],
            4 :  ['繪師: Miyamoya-pixiv',   'https://i.imgur.com/iPIVHH9.jpg'],
            5 :  ['繪師: ゆずゆい-pixiv',   'https://i.imgur.com/X3fKJyS.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message == '孝心逐漸變質' or input_message == '孝心變質':
        value_i = {
            1 :  ['繪師: 92M-pixiv',            'https://i.imgur.com/GfAKT7y.jpg'],
            2 :  ['繪師: 室町アツシ-pixiv',      'https://i.imgur.com/bhXnyCz.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
### 七冠 ###
### 桂冠 ###
### 七冠 ###
    elif input_message == '克莉絲提娜' or input_message == 'クリスティーナ' or input_message == '克總' or input_message == '誓約女君' or input_message == '27歲' or input_message == '副團長':
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
    elif input_message == '矛依未' or input_message == '青蛙' or input_message == 'ムイミ' or input_message == '天樓霸斷劍' or input_message == '諾唯姆' or input_message == '姆咪':
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
    elif input_message == '似似花' or input_message == 'ネネカ' or input_message == '448' or input_message == 'nnk' or input_message == '現士實似似花' or input_message == '變貌大妃':
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
    elif input_message == '夥伴' or input_message == '伙伴' or input_message == '同伴' or input_message == '相棒' or input_message == 'アイボウ' or input_message == '尾狗刀' or input_message == '尾刀狗':
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
    elif input_message == '馬納歷亞' or input_message == 'マナリアフレンズ' or input_message == 'Manaria Friends' or input_message == '百合公主':
        value_i = {
            1 :  ['繪師: 92M-pixiv',            'https://i.imgur.com/AtJOEqh.jpg'],
            2 :  ['繪師: とも-pixiv',           'https://i.imgur.com/rqVMy0r.jpg'],
            3 :  ['繪師: 音の绯-pixiv',         'https://i.imgur.com/OYbCg5i.jpg'],
            4 :  ['繪師: ぽんず-pixiv',         'https://i.imgur.com/QARR8iO.jpg'],
            5 :  ['繪師: れんず-pixiv',         'https://i.imgur.com/t9jLBeS.jpg'],
            6 :  ['繪師: にゃー-pixiv',         'https://i.imgur.com/Dl0bf68.jpg'],
            7 :  ['繪師: れっれれ-pixiv',       'https://i.imgur.com/pqQQ1ED.jpg'],
            8 :  ['繪師: みどりのちゃ-pixiv',   'https://i.imgur.com/D6B3wSk.jpg'],
            9 :  ['繪師: AJ-pixiv',            'https://i.imgur.com/JE5MeGW.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
### 角色 (其他) ###
### 角色 (其他) ###
### 角色 (其他) ###
    elif input_message == '愛梅斯' or input_message == 'DD頭子' or input_message == 'アメス'  or input_message == '艾梅斯':
        value_i = {
            1 :  ['繪師: aono-pixiv',           'https://i.imgur.com/yk8dzMD.jpg','https://i.imgur.com/uc1XcEF.jpg','https://i.imgur.com/uKWemDs.jpg'],
            2 :  ['繪師: aono-pixiv',           'https://i.imgur.com/hurT0Sk.jpg'],
            3 :  ['繪師: aono-pixiv',           'https://i.imgur.com/9wfDIYY.jpg'],
            4 :  ['繪師: aono-pixiv',           'https://i.imgur.com/M6WlrdB.jpg'],
            5 :  ['繪師: aono-pixiv',           'https://i.imgur.com/ujHCy0A.jpg'],
            6 :  ['繪師: つちのトン-pixiv',      'https://i.imgur.com/lzKdQtU.jpg'],
            7 :  ['繪師: うまるつふり-pixiv',    'https://i.imgur.com/LKRmGhU.jpg'],
            8 :  ['繪師: みず-pixiv',           'https://i.imgur.com/v2grm1E.jpg'],
            9 :  ['繪師: 結月わらび-pixiv',      'https://i.imgur.com/1VERUPY.jpg'],
            10 : ['繪師: Sira-pixiv',           'https://i.imgur.com/NMi24Ix.jpg']
        }
        if(len(value_i[i% len(value_i)+1])==4): 
            line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1]),ImageMessageURL(value_i[i% len(value_i)+1][2]),ImageMessageURL(value_i[i% len(value_i)+1][3])])
        else:
            line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message == '智乃' or input_message == '香風智乃' or input_message == '點兔' or input_message == 'チノ':
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
    elif input_message == '對決' or input_message == '決戰' or input_message == '終戰' or input_message == '對峙':
        value_i = {
            1 :  ['繪師: 天雷-pixiv',    'https://imgur.com/2wM6Fv3.jpg'],
            2 :  ['繪師: KMH-pixiv',     'https://imgur.com/d95pPjB.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message == '姊妹' or input_message == '姐妹':
        value_i = {
            1 :  ['繪師: みず-pixiv',        'https://i.imgur.com/ul5x7d4.jpg'],
            2 :  ['繪師: 結城辰也-pixiv',    'https://i.imgur.com/UtkMYdI.jpg'],
            3 :  ['繪師: ヤンタロウ-pixiv',  'https://i.imgur.com/QaAUaca.jpg'],
            4 :  ['繪師: Chel-pixiv',       'https://i.imgur.com/vy9LI9P.jpg'],
            5 :  ['繪師: ぬるぷよ-pixiv',    'https://i.imgur.com/WH0niD2.jpg'],
            6 :  ['繪師: ゆりりん-pixiv',    'https://i.imgur.com/vuueBKE.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message == '魔法少女' or input_message == '馬猴燒酒':
        value_i = {
            1 :  ['繪師: けんぴゃっ-pixiv',    'https://i.imgur.com/SrlAcry.jpg'],
            2 :  ['繪師: ぐっち庵-pixiv',      'https://i.imgur.com/O3N6mCH.jpg'],
            3 :  ['繪師: AJ-pixiv',           'https://i.imgur.com/nnT8dGX.jpg'],
            4 :  ['繪師: 夜凪朝妃-pixiv',      'https://i.imgur.com/bNqJcKQ.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
    elif input_message == '公主連結' or input_message == 'プリコネ':
        value_i = {
            1 :  ['繪師: Lab2-pixiv',       'https://i.imgur.com/YBfyJ36.jpg'],
            2 :  ['繪師: 菖蒲-pixiv',       'https://i.imgur.com/Ljgi7Of.jpg'],
            3 :  ['繪師: 結城辰也-pixiv',   'https://i.imgur.com/0CG57pX.jpg'],
            4 :  ['繪師: 冷蝉-pixiv',       'https://i.imgur.com/S07PioH.jpg']
        }
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text= value_i[i% len(value_i)+1][0]),ImageMessageURL(value_i[i% len(value_i)+1][1])])
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# n網
    elif input_message[0] in 'Nn' and input_message[1] in '1234567890':
        num =''.join([x for x in input_message if x.isdigit()])
        if((eval(num))==228922 or (eval(num))==173156 or (eval(num))==196970):
            value_i = {
                1 : "等等...騎士君，別告訴我你是認真的",
                2 : "吶吶，這方面的還是不要的好吧...",
                3 : "就算是這樣的騎士君，優依還是喜歡的呦",
                4 : "對不起，這次真的不能幫上忙，你必須靠你自己了",
                5 : "切嚕~\nちぇるちぇる、ちぇちぇるぱ、ちぇるるるん！\nちぇらるれ、ちぇらちぇら、ちぇるちぇぽぱぴ？"
            }
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text = value_i[i% len(value_i)+1]))
        elif eval(num)==0 :
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text ="https://nhentai.net/random/"))
# 車號範圍變更
        elif((eval(num))>=10000 and (eval(num))<=360000):
# 低機率隨機事件 (不用修改)
            value_i = {
                1  : "騎士君不行呦~你已經有優衣了",
                7 : "騎士君~整天尻雞雞不行呦，這次先不要了吧",
                13 : "哼哼~原來騎士君喜歡這種的，這次先沒收了 (生氣氣"
            }
            try:
                line_bot_api.reply_message(event.reply_token,TextSendMessage(text = value_i[i% 18+1]))
            except:
                line_bot_api.reply_message(event.reply_token,TextSendMessage(text ="nhentai.net/g/"+num))
# w網
    elif input_message[0] in 'Ww' and input_message[1] in '123456789':
        num =''.join([x for x in input_message if x.isdigit()])
        if((eval(num))==31475):
            value_i = {
                1 : "等等...騎士君，別告訴我你是認真的",
                2 : "吶吶，這方面的還是不要的好吧...",
                3 : "就算是這樣的騎士君，優依還是喜歡的呦",
                4 : "對不起，這次真的不能幫上忙，你必須靠你自己了",
                5 : "切嚕~\nちぇるちぇる、ちぇちぇるぱ、ちぇるるるん！\nちぇらるれ、ちぇらちぇら、ちぇるちぇぽぱぴ？"
            }
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text = value_i[i% len(value_i)+1]))
# 車號範圍變更
        elif((eval(num))>=1 and (eval(num))<=110000):
# 低機率隨機事件 (不用修改)
            value_i = {
                1  : "騎士君不行呦~你已經有優衣了",
                7  : "騎士君~整天尻雞雞不行呦，這次先不要了吧",
                13 : "哼哼~原來騎士君喜歡這種的，這次先沒收了 (生氣氣"
            }
            try:
                line_bot_api.reply_message(event.reply_token,TextSendMessage(text = value_i[i% 18+1]))
            except:
                line_bot_api.reply_message(event.reply_token,TextSendMessage(text ="wnacg.org/photos-slide-aid-"+num+".html"))
# ex網 & e網
    elif (input_message[:2] == 'ex' or input_message[:2] == 'e-') and input_message[2] in '123456789': 
        line_bot_api.reply_message(event.reply_token,ImageMessageURL("https://i.imgur.com/DhE6XcZ.jpg"))
