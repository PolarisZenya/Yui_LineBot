# json
from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *
#================================
from Animation import *
from FlexMessage import *
#================================
from cv2 import cv2
import numpy as np
import tempfile, os
import datetime
import time
import webbrowser
#from pydub import AudioSegment
#import speech_recognition as sr
#================================

app = Flask(__name__)
# Channel Access Token
line_bot_api = LineBotApi('PpZXtWUOfOocv4On1fWAHOFUZEdJu6WNW/XPDBbppZ3/573sZ/eyvlfZ1KP3t29JhHzzF4JgzaD1IIfrdKVWV6ocNbhBi5O4Qy5Cqpy+NHmBwYs0uZlVwiyW5bdgJPUGh4ZQG8bD6vhaSMVhjQsedAdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('ce990a6162a1aa9f706d9d826fc8d615')

# /callback  Post Request
@app.route("/callback", methods=['POST'])
def callback():
# get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
# get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
# handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# welcome
@handler.add(JoinEvent)
def handle_join(event):
    newcoming_text = "我來到一個新世界了嗎，傳教的任務永不停歇\n永遠記得佬潘仍欠我們一個女裝\n\n輸入#log開始使用與說明\n*人家目前不支援簡體中文呦~*"
    line_bot_api.reply_message(event.reply_token,TextMessage(text=newcoming_text))

# leave
@handler.add(LeaveEvent)
def handle_leave(event):
    leaving_text = "就算世界踢除了我，佬潘仍欠我們一個女裝\n再見了騎士君，我相信我們仍會重逢的"
    line_bot_api.reply_message(event.reply_token,TextMessage(text=leaving_text))

# 處理訊息
i = 1
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    input_message = event.message.text
    global i
    if(i==10000):
        i=0
    i += 1
    if input_message == '#log':
        line_bot_api.reply_message(
            event.reply_token,TextSendMessage(
                text="尻尻有益身體健康！拜託Line別再ban我了\n\n-nXXXXXX,wXXXXX就可以上車(e站也可試試)\n-公連角色梗、圖片支援！\n-輸入 #動畫+作品名稱 出現動畫連結！(開發中)\n\n*圖片畫質較高的回覆請耐心等待*\n*人家目前不支援簡體中文呦~*\n*詳細功能仍在開發中*\n*彩蛋很多放心吧~~*\n\n-已修復電腦版無法顯示圖片問題"
                )
            )
# 發車
    elif '發車' in input_message or 'nhentai' in input_message or '老司機' in input_message or  input_message == '卡' or '色情' in input_message or '上車' in input_message:
        if(i%2==1):
            message = ImageMessageURL("https://i.imgur.com/w38zXOh.jpg")
            line_bot_api.reply_message(event.reply_token,message)
        elif(i%2==0):
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text="發車了發車了(叮叮叮!!"))
# n網
    elif 'n' in input_message or 'N' in input_message:
        if((input_message[0]=='n' or input_message[0]=='N') and (input_message[1]=='1'or input_message[1]=='2'or input_message[1]=='3'or input_message[1]=='4'or input_message[1]=='5'or input_message[1]=='6'or input_message[1]=='7'or input_message[1]=='8'or input_message[1]=='9')):
            num =''.join([x for x in input_message if x.isdigit()])
            if((eval(num))==228922 or (eval(num))==173156 or (eval(num))==196970):
                if(i%5==1):
                    output_message = TextSendMessage(text ="等等...騎士君，別告訴我你是認真的")
                elif(i%5==2):
                    output_message = TextSendMessage(text ="吶吶，這方面的還是不要的好吧...")
                elif(i%5==3):
                    output_message = TextSendMessage(text ="就算是這樣的騎士君，優依還是喜歡的呦")
                elif(i%5==4):
                    output_message = TextSendMessage(text ="對不起，這次真的不能幫上忙，你必須靠你自己了")
                elif(i%5==0):
                    output_message = TextSendMessage(text ="切嚕~\nちぇるちぇる、ちぇちぇるぱ、ちぇるるるん！\nちぇらるれ、ちぇらちぇら、ちぇるちぇぽぱぴ？")
                line_bot_api.reply_message(event.reply_token,output_message)
# 車號範圍變更
            elif((eval(num))>=10000 and (eval(num))<=360000):
                output_message = TextSendMessage(text ="nhentai.net/g/"+num)
                line_bot_api.reply_message(event.reply_token,output_message)
# w網
    elif 'w' in input_message or 'W' in input_message:
        if((input_message[0]=='w' or input_message[0]=='W') and (input_message[1]=='1' or input_message[1]=='2' or input_message[1]=='3' or input_message[1]=='4' or input_message[1]=='5' or input_message[1]=='6' or input_message[1]=='7' or input_message[1]=='8' or input_message[1]=='9')):
            num =''.join([x for x in input_message if x.isdigit()])
            if((eval(num))==31475):
                if(i%5==1):
                    output_message = TextSendMessage(text ="等等...騎士君，別告訴我你是認真的")
                elif(i%5==2):
                    output_message = TextSendMessage(text ="吶吶，這方面的還是不要的好吧...")
                elif(i%5==3):
                    output_message = TextSendMessage(text ="就算是這樣的騎士君，優依還是喜歡的呦")
                elif(i%5==4):
                    output_message = TextSendMessage(text ="對不起，這次真的不能幫上忙，你必須靠你自己了")
                elif(i%5==0):
                    output_message = TextSendMessage(text ="切嚕~\nちぇるちぇる、ちぇちぇるぱ、ちぇるるるん！\nちぇらるれ、ちぇらちぇら、ちぇるちぇぽぱぴ？")
                line_bot_api.reply_message(event.reply_token,output_message)
# 車號範圍變更
            if((eval(num))>=1 and (eval(num))<=110000):
                output_message = TextSendMessage(text ="wnacg.org/photos-slide-aid-"+num+".html")
                line_bot_api.reply_message(event.reply_token,output_message)
# ex網 & e網
    elif 'ex' in input_message or 'e-' in input_message:
        if(input_message[0]=='e' and (input_message[1]=='x' or input_message[1]=='-') and (input_message[2]=='1' or input_message[2]=='2' or input_message[2]=='3' or input_message[2]=='4' or input_message[2]=='5' or input_message[2]=='6' or input_message[2]=='7' or input_message[2]=='8' or input_message[2]=='9')):
            message = ImageMessageURL("https://i.imgur.com/DhE6XcZ.jpg")
            line_bot_api.reply_message(event.reply_token,message)
# 梗圖
    elif input_message == '阿嘿顏' or input_message == '阿黑顏' or  input_message == 'アヘ顔' or input_message == 'あへがお' or input_message == 'O-Face' or input_message == '啊嘿顏':
        if(i%5==1):
            message = ImageMessageURL("https://i.imgur.com/BqQX7KL.jpg")
        elif(i%5==2):
            message = ImageMessageURL("https://i.imgur.com/iFe5eiN.jpg")
        elif(i%5==3):
            message = ImageMessageURL("https://i.imgur.com/XR2iUcD.jpg")
        elif(i%5==4):
            message = ImageMessageURL("https://i.imgur.com/9uOIoXH.jpg")
        elif(i%5==0):
            message = ImageMessageURL("https://i.imgur.com/4bs4XQN.jpg")
        line_bot_api.reply_message(event.reply_token,message)
    elif '射爆' in input_message or  input_message == '射' or '爆射' in input_message or input_message == '射了':
        if(i%7==1):
            message = ImageMessageURL("https://i.imgur.com/VEmKBTm.jpg")
        elif(i%7==2):
            message = ImageMessageURL("https://i.imgur.com/nhWCFTP.jpg")
        elif(i%7==3):
            message = ImageMessageURL("https://i.imgur.com/lWzPVq4.jpg")
        elif(i%7==4):
            message = ImageMessageURL("https://i.imgur.com/m043hLL.jpg")
        elif(i%7==5):
            message = ImageMessageURL("https://i.imgur.com/a3BN5xg.jpg")
        elif(i%7==6):
            message = ImageMessageURL("https://i.imgur.com/Ny71JoP.jpg")
        elif(i%7==0):
            message = ImageMessageURL("https://i.imgur.com/bqNJce8.jpg")
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text='大☆爆☆射！！！'),message])
    elif input_message == '怕爆' or input_message == '怕':
        if(i%4==1):
            message = ImageMessageURL("https://i.imgur.com/Qww9qPE.jpg")
        elif(i%4==2):
            message = ImageMessageURL("https://i.imgur.com/vhbLxU4.jpg")
        elif(i%4==3):
            message = ImageMessageURL("https://i.imgur.com/I9u5jID.jpg")
        elif(i%4==0):
            message = ImageMessageURL("https://i.imgur.com/H72pl7m.png")
        line_bot_api.reply_message(event.reply_token,message)
    elif '我婆' in input_message:
        if(i%5==1):
            message = ImageMessageURL("https://i.imgur.com/OnDeK8f.jpg")
        elif(i%5==2):
            message = ImageMessageURL("https://i.imgur.com/rWcQJwD.jpg")
        elif(i%5==3):
            message = ImageMessageURL("https://i.imgur.com/8ne7OeN.jpg")
        elif(i%5==4):
            message = ImageMessageURL("https://i.imgur.com/gVl6v1z.jpg")
        elif(i%5==0):
            message = ImageMessageURL("https://i.imgur.com/Ebvx2LH.jpg")
        line_bot_api.reply_message(event.reply_token,message)
    elif input_message == '佬' or input_message == '大佬' :
        if(i%4==1):
            message = ImageMessageURL("https://i.imgur.com/oH7jUmZ.jpg")
        elif(i%4==2):
            message = ImageMessageURL("https://i.imgur.com/Mn7QLMR.jpg")
        elif(i%4==3):
            message = ImageMessageURL("https://i.imgur.com/K3lkjyv.jpg")
        elif(i%4==0):
            message = ImageMessageURL("https://i.imgur.com/8niUWf6.jpg")
        line_bot_api.reply_message(event.reply_token,message)
    elif input_message == '奶子' or input_message == '是什麼蒙蔽了我的雙眼' or input_message == '奶' or input_message == '巨乳' or input_message == '大奶' or input_message == 'おっぱい' :
        if(i%3==1):
            message = ImageMessageURL("https://i.imgur.com/lLanAHP.jpg")
        elif(i%3==2):
            message = ImageMessageURL("https://i.imgur.com/BXRoBtm.jpg")
        elif(i%3==0):
            message = ImageMessageURL("https://i.imgur.com/5oM7q7O.jpg")
        line_bot_api.reply_message(event.reply_token,message)
    elif input_message == '舔' or input_message == '舔爆' :
        if(i%3==1):
            message = ImageMessageURL("https://i.imgur.com/SOVbAW0.jpg")
        elif(i%3==2):
            message = ImageMessageURL("https://i.imgur.com/t75A3vZ.jpg")
        elif(i%3==0):
            message = ImageMessageURL("https://i.imgur.com/v3DpiAK.jpg")
        line_bot_api.reply_message(event.reply_token,message)
    elif  '道歉' in input_message and  '露' in input_message:
        if(i%4==1):
            message = ImageMessageURL("https://i.imgur.com/HZLp9n5.jpg")
        elif(i%4==2):
            message = ImageMessageURL("https://i.imgur.com/mJ5u9FR.jpg")
        elif(i%4==3):
            message = ImageMessageURL("https://i.imgur.com/TwiqUp5.jpg")
        elif(i%4==0):
            message = ImageMessageURL("https://i.imgur.com/TjkbiNZ.jpg")
        line_bot_api.reply_message(event.reply_token,message)
    elif input_message == '草':
        if(i%3==1):
            message = ImageMessageURL("https://i.imgur.com/DrtsKg6.jpg")
        elif(i%3==2):
            message = ImageMessageURL("https://i.imgur.com/gzZQYAj.jpg")
        elif(i%3==0):
            message = ImageMessageURL("https://i.imgur.com/OMH6DKJ.jpg")
        line_bot_api.reply_message(event.reply_token,message)
    elif input_message == '妹妹':
        if(i%3==1):
            output_message = TextSendMessage(text ="那種東西不存在的呦~~")
            line_bot_api.reply_message(event.reply_token,output_message)
        elif(i%3==2):
            output_message = TextSendMessage(text ="是指璃乃醬還是茜里醬呢？")
            line_bot_api.reply_message(event.reply_token,output_message)
        elif(i%3==0):
            output_message = ImageMessageURL("https://i.imgur.com/KtNQ6cL.jpg")
            line_bot_api.reply_message(event.reply_token,[output_message,TextSendMessage(text='(但其實璃乃比茜里高6公分www)')])
# import FlexMessage.py
    elif input_message[0] == '我' and input_message[1] == '就':
        if(input_message == '我就爛' and i%2==1):
            message = ImageMessageURL("https://i.imgur.com/ZqjhK79.jpg")
        elif(input_message == '我就爛' and i%2==0):
            message = ImageMessageURL("https://i.imgur.com/nXsxbUW.jpg")
        elif(i%2==1):
            message = image_bubble_message('https://i.imgur.com/avyrhK4.jpg',input_message)
        elif(i%2==0):
            message = image_bubble_message('https://i.imgur.com/2OfFdhk.jpg',input_message)
        line_bot_api.reply_message(event.reply_token,message)
# 角色篇
    elif input_message == '智乃' or input_message == '香風智乃' or input_message == '點兔' or input_message == 'チノ':
        if(i%10==1):
            message = ImageMessageURL("https://i.imgur.com/lINQsqA.jpg")
            line_bot_api.reply_message(event.reply_token,message)
        elif(i%10==2):
            message = ImageMessageURL("https://i.imgur.com/ZjvdEr7.jpg")
            line_bot_api.reply_message(event.reply_token,message)
        elif(i%10==3):
            message = ImageMessageURL("https://i.imgur.com/CsZho7K.jpg")
            line_bot_api.reply_message(event.reply_token,message)
        elif(i%10==4):
            message = ImageMessageURL("https://i.imgur.com/x6y3KiT.jpg")
            line_bot_api.reply_message(event.reply_token,message)
        elif(i%10==5):
            message = ImageMessageURL("https://i.imgur.com/NfuUCXH.jpg")
            line_bot_api.reply_message(event.reply_token,message)
        elif(i%10==6):
            message = ImageMessageURL("https://i.imgur.com/DIMIze8.jpg")
            line_bot_api.reply_message(event.reply_token,[TextSendMessage(text='繪師: かにビーム-pixiv'),message])
        elif(i%10==7):
            message = ImageMessageURL("https://i.imgur.com/ZqmBXrD.jpg")
            line_bot_api.reply_message(event.reply_token,[TextSendMessage(text='繪師: かにビーム-pixiv'),message])
        elif(i%10==8):
            message = ImageMessageURL("https://i.imgur.com/Dxysvop.jpg")
            line_bot_api.reply_message(event.reply_token,[TextSendMessage(text='繪師: かにビーム-pixiv'),message])
        elif(i%10==9):
            message = ImageMessageURL("https://i.imgur.com/NocwYLL.jpg")
            line_bot_api.reply_message(event.reply_token,[TextSendMessage(text='繪師: Hitsu-pixiv'),message])
        elif(i%10==0):
            message = ImageMessageURL("https://i.imgur.com/2ciqFyu.jpg")
            line_bot_api.reply_message(event.reply_token,[TextSendMessage(text='智乃香風 is not fuck your Waifu ok?'),message])
    elif input_message == '台女' or input_message == '布丁' or input_message == '宮子' or input_message == '幽靈' or input_message == '子宮':
        if(i%9==1):
            message = ImageMessageURL("https://i.imgur.com/czGSi5r.jpg")
        elif(i%9==2):
            message = ImageMessageURL("https://i.imgur.com/T6GdEjS.jpg")
        elif(i%9==3):
            message = ImageMessageURL("https://i.imgur.com/FlMnRvL.jpg")
        elif(i%9==4):
            message = ImageMessageURL("https://i.imgur.com/lBrFXU2.jpg")
        elif(i%9==5):
            message = ImageMessageURL("https://i.imgur.com/AzPUNfb.jpg")
        elif(i%9==6):
            message = ImageMessageURL("https://i.imgur.com/2y4LEhM.jpg")
        elif(i%9==7):
            message = ImageMessageURL("https://i.imgur.com/pHNzeHo.jpg")
        elif(i%9==8):
            message = ImageMessageURL("https://i.imgur.com/W437Krq.png")
        elif(i%9==0):
            message = ImageMessageURL("https://i.imgur.com/mTT8EiE.png")
        line_bot_api.reply_message(event.reply_token,message)
    elif input_message == '8歲' or input_message == '八歲' or input_message == 'キョウカ' or input_message == '冰川鏡華' or input_message == '鏡華' or input_message == '噴水蘿' or input_message == '鏡華媽媽' or input_message == '小倉唯'  or input_message == '傲嬌蘿' :
        if(i%9==1):
            message = ImageMessageURL("https://i.imgur.com/t9OWzlK.jpg")
            line_bot_api.reply_message(event.reply_token,message)
        elif(i%9==2):
            message = ImageMessageURL("https://i.imgur.com/oVNaNZL.jpg")
            line_bot_api.reply_message(event.reply_token,message)
        elif(i%9==3):
            message = ImageMessageURL("https://i.imgur.com/pwRMWCx.jpg")
            line_bot_api.reply_message(event.reply_token,message)
        elif(i%9==4):
            message = ImageMessageURL("https://i.imgur.com/Xkj3sZB.jpg")
            line_bot_api.reply_message(event.reply_token,message)
        elif(i%9==5):
            message = ImageMessageURL("https://i.imgur.com/nkQhkYF.jpg")
            line_bot_api.reply_message(event.reply_token,[TextSendMessage(text='繪師twitter: @kazukiadumi'),message])
        elif(i%9==6):
            message = ImageMessageURL("https://i.imgur.com/cLnHzmw.jpg")
            line_bot_api.reply_message(event.reply_token,[TextSendMessage(text='繪師twitter: @usagicandy_taku'),message])
        elif(i%9==7):
            message = ImageMessageURL("https://i.imgur.com/Hrcg9ej.jpg")
            line_bot_api.reply_message(event.reply_token,[TextSendMessage(text='繪師twitter: @koma_momozu'),message])
        elif(i%9==8):
            message = ImageMessageURL("https://i.imgur.com/yfLLbF7.jpg")
            line_bot_api.reply_message(event.reply_token,[TextSendMessage(text='繪師twitter: @ryukisukune'),message])
        elif(i%9==0):
            message = ImageMessageURL("https://i.imgur.com/sdnjww4.jpg")
            line_bot_api.reply_message(event.reply_token,[TextSendMessage(text='繪師twitter: @usagicandy_taku'),message])
    elif input_message == '接頭' or input_message == '接頭霸王' or input_message == '考' or input_message == '黑貓' or input_message == '凱留' or input_message == '被骨貓' or input_message == '945' or input_message == '臭鼬' or input_message == '百地希留耶' or input_message == '希留耶' or input_message == 'キャル'  or input_message == '被骨':
        if(i%7==1):
            message = ImageMessageURL("https://i.imgur.com/qHWC2Tu.jpg")
        elif(i%7==2):
            message = ImageMessageURL("https://i.imgur.com/BlYRywQ.jpg")
        elif(i%7==3):
            message = ImageMessageURL("https://i.imgur.com/0bVJvvv.jpg")
        elif(i%7==4):
            message = ImageMessageURL("https://i.imgur.com/6EgNtoh.jpg")
        elif(i%7==5):
            message = ImageMessageURL("https://i.imgur.com/kO56BAY.jpg")
        elif(i%7==6):
            message = ImageMessageURL("https://i.imgur.com/kTih1Ht.jpg")
        elif(i%7==7):
            message = ImageMessageURL("https://i.imgur.com/h21rScV.jpg")
        line_bot_api.reply_message(event.reply_token,message)
    elif input_message == '可可蘿' or input_message == '可蘿' or input_message == '可口蘿' or input_message == 'コッコロ' or input_message == '小小嚮導' or input_message == '媽媽':
        if(i%10==1):
            message = ImageMessageURL("https://i.imgur.com/Dbx8O8i.jpg")
            line_bot_api.reply_message(event.reply_token,message)
        elif(i%10==2):
            message = ImageMessageURL("https://i.imgur.com/nR1ZxgM.jpg")
            line_bot_api.reply_message(event.reply_token,message)
        elif(i%10==3):
            message = ImageMessageURL("https://i.imgur.com/PI9E6f5.jpg")
            line_bot_api.reply_message(event.reply_token,message)
        elif(i%10==4):
            message = ImageMessageURL("https://i.imgur.com/6YoHLvJ.jpg")
            line_bot_api.reply_message(event.reply_token,message)
        elif(i%10==5):
            message = ImageMessageURL("https://i.imgur.com/Ti9PvVH.jpg")
            line_bot_api.reply_message(event.reply_token,[TextSendMessage(text='繪師twitter: @Re_hnk'),message])
        elif(i%10==6):
            message = ImageMessageURL("https://i.imgur.com/ClTlG86.jpg")
            line_bot_api.reply_message(event.reply_token,[TextSendMessage(text='繪師twitter: @IamAntKun'),message])
        elif(i%10==7):
            message = ImageMessageURL("https://i.imgur.com/os1zhfw.jpg")
            line_bot_api.reply_message(event.reply_token,[TextSendMessage(text='繪師twitter: @Alisia_0812'),message])
        elif(i%10==8):
            message = ImageMessageURL("https://i.imgur.com/OcTnn4l.jpg")
            line_bot_api.reply_message(event.reply_token,[TextSendMessage(text='繪師twitter: @ex_pulse'),message])
        elif(i%10==9):
            message = ImageMessageURL("https://i.imgur.com/bUDFQZ2.jpg")
            line_bot_api.reply_message(event.reply_token,[TextSendMessage(text='繪師twitter: @shiba1311'),message])
        elif(i%10==0):
            message = ImageMessageURL("https://i.imgur.com/k1KEd3k.jpg")
            line_bot_api.reply_message(event.reply_token,[TextSendMessage(text='繪師twitter: @msr_mrk'),message])
    elif input_message == '可哥蘿':
        message = ImageMessageURL("https://i.imgur.com/gIF9vdY.png")
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text='是可可蘿啦...(可可蘿機器人哭倒路邊'),message])
    elif input_message == '佩可' or input_message == '吃貨' or input_message == '貪吃佩可' or input_message == 'ペコリーヌ' or input_message == '尤絲蒂亞娜·F·阿斯特萊亞' or input_message == '尤絲蒂亞娜' or input_message == 'ヤバイですね' or input_message == '牙敗':
        if(i%4==1):
            message = ImageMessageURL("https://i.imgur.com/mtO06wN.jpg")
            line_bot_api.reply_message(event.reply_token,message)
        elif(i%4==2):
            message = ImageMessageURL("https://i.imgur.com/SKsplQ6.jpg")
            line_bot_api.reply_message(event.reply_token,[TextSendMessage(text='繪師twitter: @DokkoiMigu'),message])
        elif(i%4==3):
            message = ImageMessageURL("https://i.imgur.com/YYwWhZi.jpg")
            line_bot_api.reply_message(event.reply_token,[TextSendMessage(text='繪師twitter: @mato_kechi'),message])
        elif(i%4==0):
            message = ImageMessageURL("https://i.imgur.com/8Uqo7Oz.jpg")
            line_bot_api.reply_message(event.reply_token,[TextSendMessage(text='繪師twitter: @riko0202'),message])

# 動畫連結 import Animation.py & import FlexMessage.py
    elif input_message[0] == '#' and input_message[1] == '動' and input_message[2] == '畫':
        message = Anime_View(input_message)
        line_bot_api.reply_message(event.reply_token,message)
# endmodule
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

# 創建時間2020/7/7

# heroku login
# heroku git:remote linebot_name
# git init
#===================================
# git add .
# git commit -am'ok' 
# git push heroku master
#===================================

# 會要求who you are再用terminal(Ctrl+~)回應