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
#發車
    elif 'nhentai' in input_message:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text="發車了發車了"))
    elif 'n' in input_message:
        if(input_message[0]=='n' and (input_message[1]=='1'or input_message[1]=='2'or input_message[1]=='3'or input_message[1]=='4'or input_message[1]=='5'or input_message[1]=='6'or input_message[1]=='7'or input_message[1]=='8'or input_message[1]=='9')):
            num =''.join([x for x in input_message if x.isdigit()])
            if((eval(num))==228922):
                output_message = TextSendMessage(text ="前方靈車警告，勿上車")
                line_bot_api.reply_message(event.reply_token,output_message)
# 車號範圍變更
            elif((eval(num))>=10000 and (eval(num))<=360000):
                output_message = TextSendMessage(text ="nhentai.net/g/"+num)
                line_bot_api.reply_message(event.reply_token,output_message)
# 梗圖
    elif input_message == '阿嘿顏' or input_message == '阿黑顏' or  input_message == 'アヘ顔' or input_message == 'あへがお' or input_message == 'O-Face' or input_message == '啊嘿顏':
        i=(random.randint(1,5))
        if(i==1):
            message = ImageSendMessage(original_content_url = "https://imgur.com/BqQX7KL.jpg",preview_image_url = "https://imgur.com/BqQX7KL.jpg")
        elif(i==2):
            message = ImageSendMessage(original_content_url = "https://i.imgur.com/iFe5eiN.jpg",preview_image_url = "https://i.imgur.com/iFe5eiN.jpg")
        elif(i==3):
            message = ImageSendMessage(original_content_url = "https://imgur.com/XR2iUcD.jpg",preview_image_url = "https://imgur.com/XR2iUcD.jpg")
        elif(i==4):
            message = ImageSendMessage(original_content_url = "https://imgur.com/9uOIoXH.jpg",preview_image_url = "https://imgur.com/9uOIoXH.jpg")
        elif(i==5):
            message = ImageSendMessage(original_content_url = "https://imgur.com/4bs4XQN.jpg",preview_image_url = "https://imgur.com/4bs4XQN.jpg")
        line_bot_api.reply_message(event.reply_token,message)
    elif '射爆' in input_message or  input_message == '射' or  input_message == '大爆射' or  input_message == '爆射':
        i=(random.randint(1,5))
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
    elif input_message == '接頭' or input_message == '接頭霸王' or input_message == '考' or input_message == '黑貓' or input_message == '凱留' or input_message == '被骨貓' or input_message == '945':
        i=(random.randint(1,5))
        if(i==1):
            message = ImageSendMessage(original_content_url = "https://i.imgur.com/uMd1Eo3.jpg",preview_image_url = "https://i.imgur.com/uMd1Eo3.jpg")
        elif(i==2):
            message = ImageSendMessage(original_content_url = "https://i.imgur.com/ygcvFtg.jpg",preview_image_url = "https://i.imgur.com/ygcvFtg.jpg")
        elif(i==3):
            message = ImageSendMessage(original_content_url = "https://i.imgur.com/DyZ54MH.jpg",preview_image_url = "https://i.imgur.com/DyZ54MH.jpg")
        elif(i==4):
            message = ImageSendMessage(original_content_url = "https://sv.bagoum.com/getRawImage/0/0/115341020",preview_image_url = "https://sv.bagoum.com/getRawImage/0/0/115341020")
        elif(i==5):
            message = ImageSendMessage(original_content_url = "https://sv.bagoum.com/getRawImage/1/0/115341020",preview_image_url = "https://sv.bagoum.com/getRawImage/1/0/115341020")
        line_bot_api.reply_message(event.reply_token,message)
    elif '我婆' in input_message:
        i=(random.randint(1,5))
        if(i==1):
            message = ImageSendMessage(original_content_url = "https://memeprod.sgp1.digitaloceanspaces.com/user-wtf/1587551722603.jpg",preview_image_url = "https://memeprod.sgp1.digitaloceanspaces.com/user-wtf/1587551722603.jpg")
        elif(i==2):
            message = ImageSendMessage(original_content_url = "https://memes.tw/meme/d13513f9312537797af46fbbd720ee5b.png",preview_image_url = "https://memes.tw/meme/d13513f9312537797af46fbbd720ee5b.png")
        elif(i==3):
            message = ImageSendMessage(original_content_url = "https://truth.bahamut.com.tw/s01/201908/d999e4a0dd07f23f27c36678deb41e6b.JPG",preview_image_url = "https://truth.bahamut.com.tw/s01/201908/d999e4a0dd07f23f27c36678deb41e6b.JPG")
        elif(i==4):
            message = ImageSendMessage(original_content_url = "https://i.imgur.com/YDzW7ZT.jpg",preview_image_url = "https://i.imgur.com/YDzW7ZT.jpg")
        elif(i==5):
            message = ImageSendMessage(original_content_url = "https://img.moegirl.org/common/thumb/f/f0/43354518_1918439121558074_2383237838851276800_n.jpg/300px-43354518_1918439121558074_2383237838851276800_n.jpg",preview_image_url = "https://img.moegirl.org/common/thumb/f/f0/43354518_1918439121558074_2383237838851276800_n.jpg/300px-43354518_1918439121558074_2383237838851276800_n.jpg")
        line_bot_api.reply_message(event.reply_token,message)
    elif input_message == '佬' or input_message == '大佬' :
        i=(random.randint(1,3))
        if(i==1):
            message = ImageSendMessage(original_content_url = "https://truth.bahamut.com.tw/s01/201908/5616e6734e17b64a5df5a028a603b0be.JPG",preview_image_url = "https://truth.bahamut.com.tw/s01/201908/5616e6734e17b64a5df5a028a603b0be.JPG")
        elif(i==2):
            message = ImageSendMessage(original_content_url = "https://81-xiaoshuo.com/static/books/19/1924b45892ba3b9883ba45c1341cc6fd792d3ea1.jpg",preview_image_url = "https://81-xiaoshuo.com/static/books/19/1924b45892ba3b9883ba45c1341cc6fd792d3ea1.jpg")
        elif(i==3):
            message = ImageSendMessage(original_content_url = "https://img.moegirl.org/common/thumb/b/be/%E4%BC%BA%E6%9C%BA%E6%9D%80%E5%AE%B3%E5%A4%A7%E4%BD%AC.jpg/280px-%E4%BC%BA%E6%9C%BA%E6%9D%80%E5%AE%B3%E5%A4%A7%E4%BD%AC.jpg",preview_image_url = "https://img.moegirl.org/common/thumb/b/be/%E4%BC%BA%E6%9C%BA%E6%9D%80%E5%AE%B3%E5%A4%A7%E4%BD%AC.jpg/280px-%E4%BC%BA%E6%9C%BA%E6%9D%80%E5%AE%B3%E5%A4%A7%E4%BD%AC.jpg")
        line_bot_api.reply_message(event.reply_token,message)
    elif input_message == '台女' or input_message == '布丁'or input_message == '宮子':
        i=(random.randint(1,7))
        if(i==1):
            message = ImageSendMessage(original_content_url = "https://truth.bahamut.com.tw/s01/201810/627902e1fdf0ee9f6538d5706db030e4.JPG",preview_image_url = "https://truth.bahamut.com.tw/s01/201810/627902e1fdf0ee9f6538d5706db030e4.JPG")
        elif(i==2):
            message = ImageSendMessage(original_content_url = "https://truth.bahamut.com.tw/s01/201810/f404b0ba86a2336943e52057a5eb16d0.JPG",preview_image_url = "https://truth.bahamut.com.tw/s01/201810/f404b0ba86a2336943e52057a5eb16d0.JPG")
        elif(i==3):
            message = ImageSendMessage(original_content_url = "https://gamewith-tw.akamaized.net/article_tools/pricone-re/gacha/92882_limit-main.jpg",preview_image_url = "https://gamewith-tw.akamaized.net/article_tools/pricone-re/gacha/92882_limit-main.jpg")
        elif(i==4):
            message = ImageSendMessage(original_content_url = "https://gamewith.akamaized.net/article_tools/pricone-re/gacha/120762_ub-m.jpg",preview_image_url = "https://gamewith.akamaized.net/article_tools/pricone-re/gacha/120762_ub-m.jpg")
        elif(i==5):
            message = ImageSendMessage(original_content_url = "https://gamewith.akamaized.net/article_tools/pricone-re/gacha/120762_limit-main.jpg",preview_image_url = "https://gamewith.akamaized.net/article_tools/pricone-re/gacha/120762_limit-main.jpg")
        elif(i==6):
            message = ImageSendMessage(original_content_url = "https://sv.bagoum.com/getRawImage/1/0/115531010",preview_image_url = "https://sv.bagoum.com/getRawImage/1/0/115531010")
        elif(i==7):
            message = ImageSendMessage(original_content_url = "https://sv.bagoum.com/getRawImage/0/0/900534030",preview_image_url = "https://sv.bagoum.com/getRawImage/0/0/900534030")
        line_bot_api.reply_message(event.reply_token,message)
    elif input_message == '奶子' or input_message == '是什麼蒙蔽了我的雙眼' or input_message == '奶' or input_message == '巨乳' or input_message == '大奶' or input_message == 'おっぱい' :
        i=(random.randint(1,3))
        if(i==1):
            message = ImageSendMessage(original_content_url = "https://cache.hkgolden.media/compress/https://upload.cc/i1/2019/11/17/oAhBn4.png",preview_image_url = "https://cache.hkgolden.media/compress/https://upload.cc/i1/2019/11/17/oAhBn4.png")
        elif(i==2):
            message = ImageSendMessage(original_content_url = "https://truth.bahamut.com.tw/s01/201904/81359e72388dd1f833244f8c323b58be.JPG",preview_image_url = "https://truth.bahamut.com.tw/s01/201904/81359e72388dd1f833244f8c323b58be.JPG")
        elif(i==3):
            message = ImageSendMessage(original_content_url = "https://s3.hicloud.net.tw/forum.public/public/img/1551369100_7372b068f5ee8c216b282afb62d0509d4da6098d.jpg",preview_image_url = "https://s3.hicloud.net.tw/forum.public/public/img/1551369100_7372b068f5ee8c216b282afb62d0509d4da6098d.jpg")
        line_bot_api.reply_message(event.reply_token,message)
    elif input_message == '舔' or input_message == '舔爆' :
        i=(random.randint(1,3))
        if(i==1):
            message = ImageSendMessage(original_content_url = "https://truth.bahamut.com.tw/s01/201903/aea0e4e7efd9ed32ba284aaa59c82ce7.JPG",preview_image_url = "https://truth.bahamut.com.tw/s01/201903/aea0e4e7efd9ed32ba284aaa59c82ce7.JPG")
        elif(i==2):
            message = ImageSendMessage(original_content_url = "https://i.imgur.com/JRHcc7u.jpg",preview_image_url = "https://i.imgur.com/JRHcc7u.jpg")
        elif(i==3):
            message = ImageSendMessage(original_content_url = "https://i.imgur.com/9oQnk97.jpg",preview_image_url = "https://i.imgur.com/9oQnk97.jpg")
        line_bot_api.reply_message(event.reply_token,message)
    elif input_message == '可哥蘿':
        message = ImageSendMessage(original_content_url = "https://i.imgur.com/yRZpV5S.png",preview_image_url = "https://i.imgur.com/yRZpV5S.png")
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text='是可可蘿啦...(可可蘿機器人哭倒路邊'),message])
# 動畫連結
    elif input_message =='#作品名稱' or input_message =='#作品' or input_message =='#作品名稱+動畫' or input_message =='#作品名稱動畫':
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='不不不!!你搞錯了\n假設你要看re0動畫\n輸入: #re0動畫\n即可~~'))
    elif input_message == '#公連動畫' or  input_message == '#公主連結動畫':
        message = ImageSendMessage(original_content_url = "https://i.imgur.com/VGz5fxy.jpg",preview_image_url = "https://i.imgur.com/VGz5fxy.jpg")
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text='☆公主連結☆ 動畫連結\n\nb站(港澳台專用)：\nhttps://www.bilibili.com/bangumi/play/ss33095 \n\nAbema生肉(需使用VPN)：\nhttps://abema.tv/video/title/512-2'),message])
    elif input_message == '#re0動畫' or  input_message == '#Re:從零開始的異世界生活動畫' or input_message == '#雷姆動畫' or input_message == '#Re0動畫' or input_message == '#Re:0動畫' or input_message == '#從零開始異世界動畫':
        message = ImageSendMessage(original_content_url = "https://i.imgur.com/sKW0KwH.jpg",preview_image_url = "https://i.imgur.com/sKW0KwH.jpg")
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text='☆Re:從零開始的異世界生活☆ 動畫連結\n\nb站(港澳台專用)：\nhttps://www.bilibili.com/bangumi/media/md3461 \n\n巴哈(港澳台專用)\n第一季：\nhttps://ani.gamer.com.tw/animeVideo.php?sn=14440 \n第二季：(即將登場) \n\nAbema生肉(需使用VPN)\n第一季：\nhttps://abema.tv/video/title/25-139 \n第二季：(即將登場)'),message])
    elif input_message == '#輝夜姬動畫' or  input_message == '#輝夜動畫' or  input_message == '#輝夜姬想讓人告白～天才們的戀愛頭腦戰～動畫' or  input_message == '#輝夜姬想讓人告白動畫' or  input_message == '#天才們的戀愛頭腦戰動畫':
        message = ImageSendMessage(original_content_url = "https://kaguya.love/assets/img/top/img_main02.jpg",preview_image_url = "https://kaguya.love/assets/img/top/img_main02.jpg")
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