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
    newcoming_text = "我來到一個新世界了嗎，傳教的任務永不停歇\n永遠記得佬潘仍欠我們一個女裝\n\n輸入#log開始使用與說明"
    line_bot_api.reply_message(
            event.reply_token,
            TextMessage(text=newcoming_text)
        )
    print("JoinEvent =", JoinEvent)

# leave
@handler.add(LeaveEvent)
def handle_leave(event):
    print("leave Event =", event)
    print("就算世界踢除了我，佬潘仍欠我們一個女裝", event.source)

# 處理訊息

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):

    input_message = event.message.text
    if input_message == '#log':
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='尻尻有益身體健康，佬潘何日著女裝！\n\n1，n網只要輸入nXXXXXX就可以上車了呦\n射爆，阿嘿顏，公連角色梗...圖片支援！\n\n*防呆機制可能有不完整，見諒見諒*'))
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
    elif input_message == '阿嘿顏':
        i=(random.randint(1,5))
        if(i==1):
            message = ImageSendMessage(original_content_url = "https://images2.gamme.com.tw/news2/2018/07/76/qJeSpqSek6OYrqQ.jpg",preview_image_url = "https://images2.gamme.com.tw/news2/2018/07/76/qJeSpqSek6OYrqQ.jpg")
        elif(i==2):
            message = ImageSendMessage(original_content_url = "https://i2.read01.com/SIG=bj0il5/304e7378376e69426a37.jpg",preview_image_url = "https://i2.read01.com/SIG=bj0il5/304e7378376e69426a37.jpg")
        elif(i==3):
            message = ImageSendMessage(original_content_url = "https://www.teepr.com/wp-content/uploads/2019/05/%E9%98%BF%E5%98%BF%E9%A1%8F15.jpg",preview_image_url = "https://www.teepr.com/wp-content/uploads/2019/05/%E9%98%BF%E5%98%BF%E9%A1%8F15.jpg")
        elif(i==4):
            message = ImageSendMessage(original_content_url = "https://www.teepr.com/wp-content/uploads/2019/05/%E9%98%BF%E5%98%BF%E9%A1%8F9.jpg",preview_image_url = "https://www.teepr.com/wp-content/uploads/2019/05/%E9%98%BF%E5%98%BF%E9%A1%8F9.jpg")
        elif(i==5):
            message = ImageSendMessage(original_content_url = "https://i.imgur.com/lUFak2h.jpg",preview_image_url = "https://i.imgur.com/lUFak2h.jpg")
        line_bot_api.reply_message(event.reply_token,message)
    elif '射爆' in input_message:
        i=(random.randint(1,5))
        if(i==1):
            message = ImageSendMessage(original_content_url = "https://i.imgur.com/Q5zx4Jo.jpg",preview_image_url = "https://i.imgur.com/Q5zx4Jo.jpg")
        elif(i==2):
            message = ImageSendMessage(original_content_url = "https://img.moegirl.org/common/thumb/6/62/%E5%B0%84%E7%88%862.jpg/800px-%E5%B0%84%E7%88%862.jpg",preview_image_url = "https://img.moegirl.org/common/thumb/6/62/%E5%B0%84%E7%88%862.jpg/800px-%E5%B0%84%E7%88%862.jpg")
        elif(i==3):
            message = ImageSendMessage(original_content_url = "https://pbs.twimg.com/media/DPQzzZlV4AAS5m-.jpg",preview_image_url = "https://pbs.twimg.com/media/DPQzzZlV4AAS5m-.jpg")
        elif(i==4):
            message = ImageSendMessage(original_content_url = "https://img.moegirl.org/common/6/67/Wtmsb.jpg",preview_image_url = "https://img.moegirl.org/common/6/67/Wtmsb.jpg")
        elif(i==5):
            message = ImageSendMessage(original_content_url = "https://i.ytimg.com/vi/b1p8c99FgAQ/hqdefault.jpg",preview_image_url = "https://i.ytimg.com/vi/b1p8c99FgAQ/hqdefault.jpg")
        line_bot_api.reply_message(event.reply_token,message)
    elif input_message == '怕爆' or input_message == '怕':
        i=(random.randint(1,3))
        if(i==1):
            message = ImageSendMessage(original_content_url = "https://memes.tw/user-template/655eb7097c508df61f97809853121bf2.png",preview_image_url = "https://memes.tw/user-template/655eb7097c508df61f97809853121bf2.png")
        elif(i==2):
            message = ImageSendMessage(original_content_url = "https://memeprod.s3.ap-northeast-1.amazonaws.com/user-wtf/1572515832645.jpg",preview_image_url = "https://memeprod.s3.ap-northeast-1.amazonaws.com/user-wtf/1572515832645.jpg")
        elif(i==3):
            message = ImageSendMessage(original_content_url = "https://i.imgur.com/kas6Sad.jpg",preview_image_url = "https://i.imgur.com/kas6Sad.jpg")
        line_bot_api.reply_message(event.reply_token,message)
    elif input_message == '接頭' or input_message == '接頭霸王' or input_message == '考':
        i=(random.randint(1,3))
        if(i==1):
            message = ImageSendMessage(original_content_url = "https://i.imgur.com/uMd1Eo3.jpg",preview_image_url = "https://i.imgur.com/uMd1Eo3.jpg")
        elif(i==2):
            message = ImageSendMessage(original_content_url = "https://i.imgur.com/ygcvFtg.jpg",preview_image_url = "https://i.imgur.com/ygcvFtg.jpg")
        elif(i==3):
            message = ImageSendMessage(original_content_url = "https://i.imgur.com/DyZ54MH.jpg",preview_image_url = "https://i.imgur.com/DyZ54MH.jpg")
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
        i=(random.randint(1,5))
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
        line_bot_api.reply_message(event.reply_token,message)
#endmodule
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

#git add .
#git commit -am'ok' 
#git push heroku master