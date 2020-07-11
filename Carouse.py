
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

def image_carousel_message(link,input_message):
    line_bot_api = LineBotApi('発行されたCHANNEL_ACCESS_TOKEN')

    payload = {
        "type": "bubble",
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "image",
                    "url": link,
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
                                            "text": input_message,
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

    container_obj = FlexSendMessage.new_from_json_dict(payload)
    line_bot_api.push_message('送りたい相手のUserID', messages=container_obj)
    return container_obj