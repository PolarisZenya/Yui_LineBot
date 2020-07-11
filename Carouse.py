
from linebot import LineBotApi
from linebot.models import TextSendMessage,  FlexSendMessage

def image_carousel_message(input_message):
    line_bot_api = LineBotApi('ok')

    payload = {
        "type": "bubble",
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "image",
                    "url": 'https://i.imgur.com/avyrhK4.jpg',
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
    line_bot_api.push_message('UserID', messages=container_obj)