
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

def image_carousel_message(link,input_message):
    message = TemplateSendMessage(
        alt_text='圖片旋轉木馬',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url=link,
                    action=MessageTemplateAction(
                        label=input_message,
                        text = ''
                    )
                )
            ]
        )
    )
    return message