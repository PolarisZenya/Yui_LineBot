
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

def image_carousel_message(link,input_message):
    message = TemplateSendMessage(
        "type": "bubble",
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "text",
                    "text": "hello, world"
                }
            ]
        }
    )
    return message