
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

def image_carousel_message(link,input_message):
#    line_bot_api = LineBotApi('発行されたCHANNEL_ACCESS_TOKEN')

    payload = {
        "type": "bubble",
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "image",
                    "url": "https://i.imgur.com/avyrhK4.jpg",
                    "aspectMode": "cover",
                    "size": "full"
                },
                {
                    "type": "image",
                    "url": "https://scdn.line-apps.com/n/channel_devcenter/img/flexsnapshot/clip/clip15.png",
                    "position": "absolute",
                    "aspectMode": "fit",
                    "aspectRatio": "1:1",
                    "offsetTop": "0px",
                    "offsetBottom": "0px",
                    "offsetStart": "0px",
                    "offsetEnd": "0px",
                    "size": "full"
                },
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "我就接頭霸王",
                                            "size": "xl",
                                            "color": "#ffffff"
                                        }
                                    ]
                                }
                            ],
                            "spacing": "xs"
                        }
                    ],
                    "offsetBottom": "0px",
                    "offsetStart": "0px",
                    "offsetEnd": "0px",
                    "paddingAll": "20px",
                    "position": "absolute"
                }
            ],
            "paddingAll": "0px"
        }
    }
#    container_obj = FlexSendMessage.new_from_json_dict(payload)
#    container_obj = FlexSendMessage.new_from_json_dict(payload)
    container_obj = ImageSendMessage(original_content_url = "https://i.imgur.com/d3oRiU7.jpg",preview_image_url = "https://i.imgur.com/d3oRiU7.jpg")
    return container_obj