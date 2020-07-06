import json
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

#======這裡是呼叫的檔案內容=====
from message import *
from new import *
from Function import *
#======這裡是呼叫的檔案內容=====

#======python的函數庫==========
from cv2 import cv2
import numpy as np
import tempfile, os
import datetime
import time
import webbrowser
from pydub import AudioSegment
import speech_recognition as sr
#======python的函數庫==========

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('GnLHZ7dNTVeOZ9bz7q5ZmBaalAnhMW9WAYi4xhXoarVqUW3+1fYLaRZOsJez/h0ANXhaDtxUgq3idiqY9BT4ZV0fqGby8936OlY2jBqabnz890HTQCzDcFC/iBt/v/gN+FuDSEijNXa+658E7OMhowdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('9e211a0a84942e57de83f1b2f6421fd7')

# 監聽所有來自 /callback 的 Post Request
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
    newcoming_text = "老濕姬救星來也，永遠記得佬潘仍欠我們一個女裝"

    line_bot_api.reply_message(
            event.reply_token,
            TextMessage(text=newcoming_text)
        )
    print("JoinEvent =", JoinEvent)

# leave
@handler.add(LeaveEvent)
def handle_leave(event):
    print("leave Event =", event)
    print("就算世界踢除了我，佬潘仍欠我們一個女裝，輸入#log開始使用與說明", event.source)

# 處理訊息

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):

    input_message = event.message.text
    if input_message == '#log':
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='尻尻有益身體健康，佬潘何日著女裝！\n\n1，n網只要輸入nXXXXXX就可以上車了呦\n\n2，還在開發中那諾！\n\n*防呆機制可能有不完整，見諒見諒*'))
    elif 'n' in input_message:
        if(input_message[0]=='n'):
            num =''.join([x for x in input_message if x.isdigit()])
            if((eval(num))>=10000 and (eval(num))<=360000):
                output_message = TextSendMessage(text ="nhentai.net/g/"+num)
                line_bot_api.reply_message(event.reply_token,output_message)
    
#    message = ImageSendMessage(
#        original_content_url = "nhentai.net/g/" + event.message.text + "/1.png",
#        preview_image_url = "nhentai.net/g/" + event.message.text  +"/1.png"
#       )
#    line_bot_api.reply_message(event.reply_token,message)

#end
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

#git add .
#git commit -am'ok' 
#git push heroku master