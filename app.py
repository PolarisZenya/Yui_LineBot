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
    newcoming_text = "佬潘必須女裝"

    line_bot_api.reply_message(
            event.reply_token,
            TextMessage(text=newcoming_text)
        )
    print("JoinEvent =", JoinEvent)
# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TextSendMessage(text = "nhentai.net/g/"+ event.message.text)
    line_bot_api.reply_message(event.reply_token,message)

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