# json, py flask
#============================================================
from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *
#============================================================
from User_input import *
#============================================================
app = Flask(__name__)
# Channel Access Token
line_bot_api = LineBotApi('PpZXtWUOfOocv4On1fWAHOFUZEdJu6WNW/XPDBbppZ3/573sZ/eyvlfZ1KP3t29JhHzzF4JgzaD1IIfrdKVWV6ocNbhBi5O4Qy5Cqpy+NHmBwYs0uZlVwiyW5bdgJPUGh4ZQG8bD6vhaSMVhjQsedAdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('ce990a6162a1aa9f706d9d826fc8d615')
#============================================================
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
#============================================================
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
    Judgment (i,input_message,event)
    i += 1

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