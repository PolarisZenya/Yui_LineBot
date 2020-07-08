import json
import random
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, JoinEvent, LeaveEvent, TextMessage, TextSendMessage
)
from message import *
from new import *
from Function import *
from cv2 import cv2
import numpy as np
import tempfile, os
import datetime
import time
import webbrowser
from pydub import AudioSegment
import speech_recognition as sr
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

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):

    input_message = event.message.text
    if input_message == '#log':
        line_bot_api.reply_message(event.reply_token,TextSendMessage(
            text="尻尻有益身體健康，佬潘何日著女裝！等等李海珍別再ban我了www\n\n-nXXXXXX就可以上車了呦\n-公連角色梗、圖片支援！\n-輸入 #作品名稱+動畫 出現動畫連結！(開發中)\n\n*防呆機制可能有不完整*\n*人家目前不支援簡體中文呦~*\n*詳細功能仍在開發中* v1.01\n\n☆預計加入：閒聊chat模式☆"))
# 發車
    elif '發車' in input_message or 'nhentai' in input_message or  input_message == '卡' or '色情' in input_message:
        i=(random.randint(1,2))
        if(i==1):
            message = ImageSendMessage(original_content_url = "https://imgur.com/w38zXOh.jpg",preview_image_url = "https://imgur.com/w38zXOh.jpg")
            line_bot_api.reply_message(event.reply_token,message)
        elif(i==2):
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text="發車了發車了(叮叮叮!!"))
    elif 'n' in input_message:
        if(input_message[0]=='n' and (input_message[1]=='1'or input_message[1]=='2'or input_message[1]=='3'or input_message[1]=='4'or input_message[1]=='5'or input_message[1]=='6'or input_message[1]=='7'or input_message[1]=='8'or input_message[1]=='9')):
            num =''.join([x for x in input_message if x.isdigit()])
            if((eval(num))==228922):
                i=(random.randint(1,5))
                if(i==1):
                    output_message = TextSendMessage(text ="等等...騎士君，別告訴我你是認真的")
                elif(i==2):
                    output_message = TextSendMessage(text ="吶吶，這方面的還是不要的好吧...")
                elif(i==3):
                    output_message = TextSendMessage(text ="就算是這樣的騎士君，優依還是喜歡的呦")
                elif(i==4):
                    output_message = TextSendMessage(text ="對不起，這次真的不能幫上忙，你必須靠你自己了")
                elif(i==5):
                    output_message = TextSendMessage(text ="切嚕~\nちぇるちぇる、ちぇちぇるぱ、ちぇるるるん！\nちぇらるれ、ちぇらちぇら、ちぇるちぇぽぱぴ？")
                line_bot_api.reply_message(event.reply_token,output_message)
# 車號範圍變更
            elif((eval(num))>=10000 and (eval(num))<=360000):
                output_message = TextSendMessage(text ="nhentai.net/g/"+num)
                line_bot_api.reply_message(event.reply_token,output_message)
    elif '#譴責' in input_message:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text="我方就台湾民众近来的一系列错误言行，已经多次向台湾民众表明我们的严正立场：台湾民众有关人士的陈词滥调充满了政治偏见与谎言。我們坚决反对台湾民众独立的行为，中方已就此向台湾民众提出严正交涉和强烈抗议。在国际社会大家庭里,中国始终维护和平,促进发展,坚守道义,同各国携手构建人类命运共同体。台湾民众却损人利己,唯我独尊,背信弃义,在世界上大搞顺我者昌,逆我者亡。我方已就此向台湾民众提出严正交涉，表达强烈抗议。台湾民众如果独立，不仅将损害中方利益，损害中国和台湾民众关系，也将严重损害台湾民众自身的利益。还是我们经常说的那句话，请台湾民众不要高估自己的造谣能力，也不要低估别人的判断能力。谎言重复一千遍，依然还是谎言。台湾民众的图谋注定失败。台湾民众任何企图干预中国内政、阻碍中国发展的把戏都不会得逞，到头来只会是枉费心机一场空。对于台湾民众的错误做法，中方必将采取有力的措施坚决予以反制，坚定地维护自身主权、安全、发展利益。中国坚持走和平发展道路，积极为维护世界和平稳定贡献智慧力量。中国坚持对外开放，互利共赢，同世界分享中国发展的机遇。中国政府反对任何外部势力干预中国事务的决心坚定不移，维护国家主权、安全、发展利益的决心坚定不移。台湾民众独立是搬起石头砸自己的脚。我们要正告台湾民众，任何外国政府和势力都无权干预中国内政。希望台湾民众个别人士能以开放的心态和客观公正的态度对待中国，不要无中生有。我要告诉台湾民众一些政客，人贵有自知之明，请他还是趁早反省一下台湾民众自身的问题，放弃偏见和执念，停止喋喋不休的反华聒噪。台湾民众这一恶劣行径不仅损害中方利益，也会损害台湾民众自身的重要利益。台湾民众的拙劣表演充分暴露出其不可告人的险恶用心和政治企图。如果台湾民众一意孤行，我方将同意中方必将采取有力措施予以坚决反制。"))
# 梗圖
    elif input_message == '阿嘿顏' or input_message == '阿黑顏' or  input_message == 'アヘ顔' or input_message == 'あへがお' or input_message == 'O-Face' or input_message == '啊嘿顏':
        i=(random.randint(1,5))
        if(i==1):
            message = ImageSendMessage(original_content_url = "https://imgur.com/BqQX7KL.jpg",preview_image_url = "https://imgur.com/BqQX7KL.jpg")
        elif(i==2):
            message = ImageSendMessage(original_content_url = "https://imgur.com/iFe5eiN.jpg",preview_image_url = "https://imgur.com/iFe5eiN.jpg")
        elif(i==3):
            message = ImageSendMessage(original_content_url = "https://imgur.com/XR2iUcD.jpg",preview_image_url = "https://imgur.com/XR2iUcD.jpg")
        elif(i==4):
            message = ImageSendMessage(original_content_url = "https://imgur.com/9uOIoXH.jpg",preview_image_url = "https://imgur.com/9uOIoXH.jpg")
        elif(i==5):
            message = ImageSendMessage(original_content_url = "https://imgur.com/4bs4XQN.jpg",preview_image_url = "https://imgur.com/4bs4XQN.jpg")
        line_bot_api.reply_message(event.reply_token,message)
    elif '射爆' in input_message or  input_message == '射' or '爆射' in input_message or input_message == '射了':
        i=(random.randint(1,7))
        if(i==1):
            message = ImageSendMessage(original_content_url = "https://imgur.com/VEmKBTm.jpg",preview_image_url = "https://imgur.com/VEmKBTm.jpg")
        elif(i==2):
            message = ImageSendMessage(original_content_url = "https://imgur.com/nhWCFTP.jpg",preview_image_url = "https://imgur.com/nhWCFTP.jpg")
        elif(i==3):
            message = ImageSendMessage(original_content_url = "https://imgur.com/lWzPVq4.jpg",preview_image_url = "https://imgur.com/lWzPVq4.jpg")
        elif(i==4):
            message = ImageSendMessage(original_content_url = "https://imgur.com/m043hLL.jpg",preview_image_url = "https://imgur.com/m043hLL.jpg")
        elif(i==5):
            message = ImageSendMessage(original_content_url = "https://imgur.com/a3BN5xg.jpg",preview_image_url = "https://imgur.com/a3BN5xg.jpg")
        elif(i==6):
            message = ImageSendMessage(original_content_url = "https://imgur.com/Ny71JoP.jpg",preview_image_url = "https://imgur.com/Ny71JoP.jpg")
        elif(i==7):
            message = ImageSendMessage(original_content_url = "https://imgur.com/bqNJce8.jpg",preview_image_url = "https://imgur.com/bqNJce8.jpg")
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text='大☆爆☆射！！！'),message])
    elif input_message == '怕爆' or input_message == '怕':
        i=(random.randint(1,4))
        if(i==1):
            message = ImageSendMessage(original_content_url = "https://imgur.com/Qww9qPE.jpg",preview_image_url = "https://imgur.com/Qww9qPE.jpg")
        elif(i==2):
            message = ImageSendMessage(original_content_url = "https://imgur.com/vhbLxU4.jpg",preview_image_url = "https://imgur.com/vhbLxU4.jpg")
        elif(i==3):
            message = ImageSendMessage(original_content_url = "https://imgur.com/I9u5jID.jpg",preview_image_url = "https://imgur.com/I9u5jID.jpg")
        elif(i==4):
            message = ImageSendMessage(original_content_url = "https://imgur.com/H72pl7m.png",preview_image_url = "https://imgur.com/H72pl7m.png")
        line_bot_api.reply_message(event.reply_token,message)
    elif '我婆' in input_message:
        i=(random.randint(1,5))
        if(i==1):
            message = ImageSendMessage(original_content_url = "https://imgur.com/OnDeK8f.jpg",preview_image_url = "https://imgur.com/OnDeK8f.jpg")
        elif(i==2):
            message = ImageSendMessage(original_content_url = "https://imgur.com/rWcQJwD.jpg",preview_image_url = "https://imgur.com/rWcQJwD.jpg")
        elif(i==3):
            message = ImageSendMessage(original_content_url = "https://imgur.com/8ne7OeN.jpg",preview_image_url = "https://imgur.com/8ne7OeN.jpg")
        elif(i==4):
            message = ImageSendMessage(original_content_url = "https://imgur.com/gVl6v1z.jpg",preview_image_url = "https://imgur.com/gVl6v1z.jpg")
        elif(i==5):
            message = ImageSendMessage(original_content_url = "https://imgur.com/Ebvx2LH.jpg",preview_image_url = "https://imgur.com/Ebvx2LH.jpg")
        line_bot_api.reply_message(event.reply_token,message)
    elif input_message == '佬' or input_message == '大佬' :
        i=(random.randint(1,4))
        if(i==1):
            message = ImageSendMessage(original_content_url = "https://imgur.com/oH7jUmZ.jpg",preview_image_url = "https://imgur.com/oH7jUmZ.jpg")
        elif(i==2):
            message = ImageSendMessage(original_content_url = "https://imgur.com/Mn7QLMR.jpg",preview_image_url = "https://imgur.com/Mn7QLMR.jpg")
        elif(i==3):
            message = ImageSendMessage(original_content_url = "https://imgur.com/K3lkjyv.jpg",preview_image_url = "https://imgur.com/K3lkjyv.jpg")
        elif(i==4):
            message = ImageSendMessage(original_content_url = "https://imgur.com/8niUWf6.jpg",preview_image_url = "https://imgur.com/8niUWf6.jpg")
        line_bot_api.reply_message(event.reply_token,message)
    elif input_message == '奶子' or input_message == '是什麼蒙蔽了我的雙眼' or input_message == '奶' or input_message == '巨乳' or input_message == '大奶' or input_message == 'おっぱい' :
        i=(random.randint(1,3))
        if(i==1):
            message = ImageSendMessage(original_content_url = "https://imgur.com/lLanAHP.jpg",preview_image_url = "https://imgur.com/lLanAHP.jpg")
        elif(i==2):
            message = ImageSendMessage(original_content_url = "https://imgur.com/BXRoBtm.jpg",preview_image_url = "https://imgur.com/BXRoBtm.jpg")
        elif(i==3):
            message = ImageSendMessage(original_content_url = "https://imgur.com/5oM7q7O.jpg",preview_image_url = "https://imgur.com/5oM7q7O.jpg")
        line_bot_api.reply_message(event.reply_token,message)
    elif input_message == '舔' or input_message == '舔爆' :
        i=(random.randint(1,3))
        if(i==1):
            message = ImageSendMessage(original_content_url = "https://imgur.com/SOVbAW0.jpg",preview_image_url = "https://imgur.com/SOVbAW0.jpg")
        elif(i==2):
            message = ImageSendMessage(original_content_url = "https://imgur.com/t75A3vZ.jpg",preview_image_url = "https://imgur.com/t75A3vZ.jpg")
        elif(i==3):
            message = ImageSendMessage(original_content_url = "https://imgur.com/v3DpiAK.jpg",preview_image_url = "https://imgur.com/v3DpiAK.jpg")
        line_bot_api.reply_message(event.reply_token,message)
# 角色篇
    elif input_message == '台女' or input_message == '布丁' or input_message == '宮子' or input_message == '幽靈' or input_message == '子宮':
        i=(random.randint(1,13))
        if(i==1):
            message = VideoSendMessage(original_content_url = "https://imgur.com/kbM1c5R.mp4",preview_image_url = "https://imgur.com/yufWFwG.png")
        elif(i==2):
            message = VideoSendMessage(original_content_url = "https://imgur.com/nlJBghU.mp4",preview_image_url = "https://imgur.com/t8G0CNd.png")
        elif(i==3):
            message = ImageSendMessage(original_content_url = "https://imgur.com/S8h3irX.jpg",preview_image_url = "https://imgur.com/S8h3irX.jpg")
        elif(i==4):
            message = ImageSendMessage(original_content_url = "https://imgur.com/czGSi5r.jpg",preview_image_url = "https://imgur.com/czGSi5r.jpg")
        elif(i==5):
            message = ImageSendMessage(original_content_url = "https://imgur.com/T6GdEjS.jpg",preview_image_url = "https://imgur.com/T6GdEjS.jpg")
        elif(i==6):
            message = ImageSendMessage(original_content_url = "https://imgur.com/FlMnRvL.jpg",preview_image_url = "https://imgur.com/FlMnRvL.jpg")
        elif(i==7):
            message = ImageSendMessage(original_content_url = "https://imgur.com/lBrFXU2.jpg",preview_image_url = "https://imgur.com/lBrFXU2.jpg")
        elif(i==8):
            message = VideoSendMessage(original_content_url = "https://imgur.com/AzPUNfb.jpg",preview_image_url = "https://imgur.com/AzPUNfb.jpg")
        elif(i==9):
            message = ImageSendMessage(original_content_url = "https://imgur.com/2y4LEhM.jpg",preview_image_url = "https://imgur.com/2y4LEhM.jpg")
        elif(i==10):
            message = ImageSendMessage(original_content_url = "https://imgur.com/pHNzeHo.jpg",preview_image_url = "https://imgur.com/pHNzeHo.jpg")
        elif(i==11):
            message = ImageSendMessage(original_content_url = "https://imgur.com/W437Krq.png",preview_image_url = "https://imgur.com/W437Krq.png")
        elif(i==12):
            message = ImageSendMessage(original_content_url = "https://imgur.com/mTT8EiE.png",preview_image_url = "https://imgur.com/mTT8EiE.png")
        elif(i==13):
            message = ImageSendMessage(original_content_url = "https://imgur.com/lEOwXPG.jpg",preview_image_url = "https://imgur.com/lEOwXPG.jpg")
        line_bot_api.reply_message(event.reply_token,message)
    elif input_message == '8歲' or input_message == '八歲' or input_message == 'キョウカ' or input_message == '冰川鏡華' or input_message == '鏡華' or input_message == '噴水蘿' or input_message == '鏡華媽媽' or input_message == '小倉唯'  or input_message == '傲嬌蘿' :
        i=(random.randint(1,8))
        if(i==1):
            message = ImageSendMessage(original_content_url = "https://imgur.com/t9OWzlK.jpg",preview_image_url = "https://imgur.com/t9OWzlK.jpg")
            line_bot_api.reply_message(event.reply_token,message)
        elif(i==2):
            message = ImageSendMessage(original_content_url = "https://imgur.com/oVNaNZL.jpg",preview_image_url = "https://imgur.com/oVNaNZL.jpg")
            line_bot_api.reply_message(event.reply_token,message)
        elif(i==3):
            message = ImageSendMessage(original_content_url = "https://imgur.com/nkQhkYF.jpg",preview_image_url = "https://imgur.com/nkQhkYF.jpg")
            line_bot_api.reply_message(event.reply_token,[TextSendMessage(text='繪師twitter: @kazukiadumi'),message])
        elif(i==4):
            message = ImageSendMessage(original_content_url = "https://imgur.com/cLnHzmw.jpg",preview_image_url = "https://imgur.com/cLnHzmw.jpg")
            line_bot_api.reply_message(event.reply_token,[TextSendMessage(text='繪師twitter: @usagicandy_taku'),message])
        elif(i==5):
            message = ImageSendMessage(original_content_url = "https://imgur.com/Hrcg9ej.jpg",preview_image_url = "https://imgur.com/Hrcg9ej.jpg")
            line_bot_api.reply_message(event.reply_token,[TextSendMessage(text='繪師twitter: @koma_momozu'),message])
        elif(i==6):
            message = ImageSendMessage(original_content_url = "https://imgur.com/pwRMWCx.jpg",preview_image_url = "https://imgur.com/pwRMWCx.jpg")
            line_bot_api.reply_message(event.reply_token,message)
        elif(i==7):
            message = ImageSendMessage(original_content_url = "https://imgur.com/Bpy0dPB.jpg",preview_image_url = "https://imgur.com/Bpy0dPB.jpg")
            line_bot_api.reply_message(event.reply_token,[TextSendMessage(text='繪師twitter: @ryukisukune'),message])
        elif(i==8):
            message = ImageSendMessage(original_content_url = "https://imgur.com/Xkj3sZB.jpg",preview_image_url = "https://imgur.com/Xkj3sZB.jpg")
    elif input_message == '接頭' or input_message == '接頭霸王' or input_message == '考' or input_message == '黑貓' or input_message == '凱留' or input_message == '被骨貓' or input_message == '945' or input_message == '臭鼬' or input_message == '百地希留耶' or input_message == '希留耶' or input_message == 'キャル' :
        i=(random.randint(1,7))
        if(i==1):
            message = ImageSendMessage(original_content_url = "https://imgur.com/qHWC2Tu.jpg",preview_image_url = "https://imgur.com/qHWC2Tu.jpg")
        elif(i==2):
            message = ImageSendMessage(original_content_url = "https://imgur.com/BlYRywQ.jpg",preview_image_url = "https://imgur.com/BlYRywQ.jpg")
        elif(i==3):
            message = ImageSendMessage(original_content_url = "https://imgur.com/0bVJvvv.jpg",preview_image_url = "https://imgur.com/0bVJvvv.jpg")
        elif(i==4):
            message = ImageSendMessage(original_content_url = "https://imgur.com/6EgNtoh.jpg",preview_image_url = "https://imgur.com/6EgNtoh.jpg")
        elif(i==5):
            message = ImageSendMessage(original_content_url = "https://imgur.com/kO56BAY.jpg",preview_image_url = "https://imgur.com/kO56BAY.jpg")
        elif(i==6):
            message = ImageSendMessage(original_content_url = "https://imgur.com/kTih1Ht.jpg",preview_image_url = "https://imgur.com/kTih1Ht.jpg")
        elif(i==7):
            message = ImageSendMessage(original_content_url = "https://imgur.com/h21rScV.jpg",preview_image_url = "https://imgur.com/h21rScV.jpg")
        line_bot_api.reply_message(event.reply_token,message)
    elif input_message == '可可蘿' or input_message == '可蘿' or input_message == '可口蘿' or input_message == 'コッコロ' or input_message == '小小嚮導' or input_message == '媽媽':
        i=(random.randint(1,9))
        if(i==1):
            message = ImageSendMessage(original_content_url = "https://imgur.com/Dbx8O8i.jpg",preview_image_url = "https://imgur.com/Dbx8O8i.jpg")
            line_bot_api.reply_message(event.reply_token,message)
        elif(i==2):
            message = ImageSendMessage(original_content_url = "https://imgur.com/nR1ZxgM.jpg",preview_image_url = "https://imgur.com/nR1ZxgM.jpg")
            line_bot_api.reply_message(event.reply_token,message)
        elif(i==3):
            message = ImageSendMessage(original_content_url = "https://imgur.com/PI9E6f5.jpg",preview_image_url = "https://imgur.com/PI9E6f5.jpg")
            line_bot_api.reply_message(event.reply_token,message)
        elif(i==4):
            message = ImageSendMessage(original_content_url = "https://imgur.com/Ti9PvVH.jpg",preview_image_url = "https://imgur.com/Ti9PvVH.jpg")
            line_bot_api.reply_message(event.reply_token,[TextSendMessage(text='繪師twitter: @Re_hnk'),message])
        elif(i==5):
            message = ImageSendMessage(original_content_url = "https://imgur.com/ClTlG86.jpg",preview_image_url = "https://imgur.com/ClTlG86.jpg")
            line_bot_api.reply_message(event.reply_token,[TextSendMessage(text='繪師twitter: @IamAntKun'),message])
        elif(i==6):
            message = ImageSendMessage(original_content_url = "https://imgur.com/os1zhfw.jpg",preview_image_url = "https://imgur.com/os1zhfw.jpg")
            line_bot_api.reply_message(event.reply_token,[TextSendMessage(text='繪師twitter: @Alisia_0812'),message])
        elif(i==7):
            message = ImageSendMessage(original_content_url = "https://imgur.com/OcTnn4l.jpg",preview_image_url = "https://imgur.com/OcTnn4l.jpg")
            line_bot_api.reply_message(event.reply_token,[TextSendMessage(text='繪師twitter: @ex_pulse'),message])
        elif(i==8):
            message = ImageSendMessage(original_content_url = "https://imgur.com/bUDFQZ2.jpg",preview_image_url = "https://imgur.com/bUDFQZ2.jpg")
            line_bot_api.reply_message(event.reply_token,[TextSendMessage(text='繪師twitter: @shiba1311'),message])
        elif(i==9):
            message = ImageSendMessage(original_content_url = "https://imgur.com/k1KEd3k.jpg",preview_image_url = "https://imgur.com/k1KEd3k.jpg")
            line_bot_api.reply_message(event.reply_token,[TextSendMessage(text='繪師twitter: @msr_mrk'),message])
    elif input_message == '佩可' or input_message == '吃貨' or input_message == '貪吃佩可' or input_message == 'ペコリーヌ' or input_message == '尤絲蒂亞娜·F·阿斯特萊亞' or input_message == '尤絲蒂亞娜' or input_message == 'ヤバイですね' or input_message == '牙敗':
        i=(random.randint(1,4))
        if(i==1):
            message = ImageSendMessage(original_content_url = "https://imgur.com/SKsplQ6.jpg",preview_image_url = "https://imgur.com/SKsplQ6.jpg")
            line_bot_api.reply_message(event.reply_token,[TextSendMessage(text='繪師twitter: @DokkoiMigu'),message])
        elif(i==2):
            message = ImageSendMessage(original_content_url = "https://imgur.com/YYwWhZi.jpg",preview_image_url = "https://imgur.com/YYwWhZi.jpg")
            line_bot_api.reply_message(event.reply_token,[TextSendMessage(text='繪師twitter: @mato_kechi'),message])
        elif(i==3):
            message = ImageSendMessage(original_content_url = "https://imgur.com/mtO06wN.jpg",preview_image_url = "https://imgur.com/mtO06wN.jpg")
            line_bot_api.reply_message(event.reply_token,message)
        elif(i==4):
            message = ImageSendMessage(original_content_url = "https://imgur.com/8Uqo7Oz.jpg",preview_image_url = "https://imgur.com/8Uqo7Oz.jpg")
            line_bot_api.reply_message(event.reply_token,[TextSendMessage(text='繪師twitter: @riko0202'),message])
    elif input_message == '可哥蘿':
        message = ImageSendMessage(original_content_url = "https://imgur.com/gIF9vdY.png",preview_image_url = "https://imgur.com/gIF9vdY.png")
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text='是可可蘿啦...(可可蘿機器人哭倒路邊'),message])
# 動畫連結
    elif input_message =='#作品名稱' or input_message =='#作品' or input_message =='#作品名稱+動畫' or input_message =='#作品名稱動畫':
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='不不不!!你搞錯了\n假設你要看re0動畫\n輸入: #re0動畫\n即可~~'))
    elif input_message == '#公連動畫' or  input_message == '#公主連結動畫':
        i=(random.randint(1,7))
        if(i==1):
            message = ImageSendMessage(original_content_url = "https://imgur.com/IulcU1a.jpg",preview_image_url = "https://imgur.com/IulcU1a.jpg")
        if(i==2):
            message = ImageSendMessage(original_content_url = "https://imgur.com/CksvDjN.jpg",preview_image_url = "https://imgur.com/CksvDjN.jpg")
        if(i==3):
            message = ImageSendMessage(original_content_url = "https://imgur.com/FLSUOjR.jpg",preview_image_url = "https://imgur.com/FLSUOjR.jpg")
        if(i==4):
            message = ImageSendMessage(original_content_url = "https://imgur.com/FYblE8E.jpg",preview_image_url = "https://imgur.com/FYblE8E.jpg")
        if(i==5):
            message = ImageSendMessage(original_content_url = "https://imgur.com/gxMQkHy.jpg",preview_image_url = "https://imgur.com/gxMQkHy.jpg")
        if(i==6):
            message = ImageSendMessage(original_content_url = "https://imgur.com/sBYyPxS.jpg",preview_image_url = "https://imgur.com/sBYyPxS.jpg")
        if(i==7):
            message = ImageSendMessage(original_content_url = "https://imgur.com/dqDTLAH.jpg",preview_image_url = "https://imgur.com/dqDTLAH.jpg")
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text='☆公主連結☆ 動畫連結\n\nb站(港澳台專用)：\nhttps://www.bilibili.com/bangumi/play/ss33095 \n\nAbema生肉(需使用VPN)：\nhttps://abema.tv/video/title/512-2'),message])
    elif input_message == '#re0動畫' or  input_message == '#Re:從零開始的異世界生活動畫' or input_message == '#雷姆動畫' or input_message == '#Re0動畫' or input_message == '#Re:0動畫' or input_message == '#從零開始異世界動畫':
        i=(random.randint(1,4))
        if(i==1):
            message = ImageSendMessage(original_content_url = "https://imgur.com/dy5SWPI.jpg",preview_image_url = "https://imgur.com/dy5SWPI.jpg")
        if(i==2):
            message = ImageSendMessage(original_content_url = "https://imgur.com/fVkLdJV.jpg",preview_image_url = "https://imgur.com/fVkLdJV.jpg")
        if(i==3):
            message = ImageSendMessage(original_content_url = "https://imgur.com/rQVZCGT.jpg",preview_image_url = "https://imgur.com/rQVZCGT.jpg")
        if(i==4):
            message = ImageSendMessage(original_content_url = "https://imgur.com/WSzx0X4.jpg",preview_image_url = "https://imgur.com/WSzx0X4.jpg")
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text='☆Re:從零開始的異世界生活☆ 動畫連結\n\nb站(港澳台專用)：\nhttps://www.bilibili.com/bangumi/media/md3461 \n\n巴哈(港澳台專用)\n第一季：\nhttps://ani.gamer.com.tw/animeVideo.php?sn=14440 \n第二季：(即將登場) \n\nAbema生肉(需使用VPN)\n第一季：\nhttps://abema.tv/video/title/25-139 \n第二季：(即將登場)'),message])
    elif input_message == '#輝夜姬動畫' or  input_message == '#輝夜動畫' or  input_message == '#輝夜姬想讓人告白～天才們的戀愛頭腦戰～動畫' or  input_message == '#輝夜姬想讓人告白動畫' or  input_message == '#天才們的戀愛頭腦戰動畫':
        i=(random.randint(1,3))
        if(i==1):
            message = ImageSendMessage(original_content_url = "https://imgur.com/ZS7xDXG.jpg",preview_image_url = "https://imgur.com/ZS7xDXG.jpg")
        if(i==2):
            message = ImageSendMessage(original_content_url = "https://imgur.com/4Ntx0Rw.jpg",preview_image_url = "https://imgur.com/4Ntx0Rw.jpg")
        if(i==3):
            message = ImageSendMessage(original_content_url = "https://imgur.com/oiyKEI8.jpg",preview_image_url = "https://imgur.com/oiyKEI8.jpg")
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text='☆輝夜姬想讓人告白～天才們的戀愛頭腦戰～☆ 動畫連結\n\nb站(港澳台專用)：\nhttps://www.bilibili.com/bangumi/media/md5267730 \n\n巴哈(港澳台專用)\n第一季：\nhttps://ani.gamer.com.tw/animeVideo.php?sn=11431 \n第二季：\nhttps://ani.gamer.com.tw/animeVideo.php?sn=15298 \n\nAbema生肉(需使用VPN)\n第一季：\nhttps://abema.tv/video/title/26-66 \n第二季：\nhttps://abema.tv/video/title/26-96 '),message])


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