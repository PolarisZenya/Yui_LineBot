#============================================================
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *
# linebbot_std made node json in python
#============================================================
# 我就xx 自定義梗圖
def image_bubble_message(link,input_message):
    flex_message = FlexSendMessage(
        alt_text = input_message,
        contents = {
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
                                                "color": "#ffffff",
                                                "weight": "bold"
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
    )
    return flex_message

# 巴哈 bili abema (a,b,c)
def Anime_Return_abc(
    url_baha,
    url_bili,
    url_abema,
    anime_name,
    pic_baha,
    pic_bili,
    pic_abema
    ):

    flex_message = FlexSendMessage(
        alt_text = (anime_name+'動畫連結'),
        contents = {
            "type": "carousel",
            "contents": [
                {
                    "type": "bubble",
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "image",
                                "url": pic_baha,
                                "size": "full",
                                "aspectMode": "cover",
                                "aspectRatio": "3:4",
                                "gravity": "top"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": anime_name,
                                                "size": "xl",
                                                "color": "#ffffff",
                                                "weight": "bold"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "巴哈姆特動漫瘋",
                                                "color": "#ebebeb",
                                                "size": "sm",
                                                "offsetBottom": "1px"
                                            }
                                        ],
                                        "spacing": "lg"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "filler"
                                            },
                                            {
                                                "type": "box",
                                                "layout": "baseline",
                                                "contents": [
                                                    {
                                                        "type": "filler"
                                                    },
                                                    {
                                                        "type": "text",
                                                        "text": "立即前往觀看",
                                                        "color": "#ffffff",
                                                        "flex": 0,
                                                        "offsetTop": "-2px"
                                                    },
                                                    {
                                                        "type": "filler"
                                                    }
                                                ],
                                                "spacing": "sm"
                                            },
                                            {
                                                "type": "filler"
                                            }
                                        ],
                                        "borderWidth": "1px",
                                        "cornerRadius": "4px",
                                        "spacing": "sm",
                                        "borderColor": "#ffffff",
                                        "margin": "xxl",
                                        "height": "40px",
                                        "action": {
                                            "type": "uri",
                                            "label": "action",
                                            "uri": url_baha
                                        }
                                    }
                                ],
                                "position": "absolute",
                                "offsetBottom": "0px",
                                "offsetStart": "0px",
                                "offsetEnd": "0px",
                                "backgroundColor": "#55B5B0BB",
                                "paddingAll": "20px",
                                "paddingTop": "18px"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "filler"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "推薦",
                                                "size": "xs",
                                                "color": "#ffffff",
                                                "align": "center"
                                            }
                                        ]
                                    },
                                    {
                                      "type": "filler"
                                    }
                                ],
                                "position": "absolute",
                                "cornerRadius": "20px",
                                "offsetTop": "18px",
                                "backgroundColor": "#ff334bCC",
                                "offsetStart": "18px",
                                "height": "25px",
                                "width": "53px"
                            }
                        ],
                        "paddingAll": "0px"
                    }
                },
                {
                    "type": "bubble",
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "image",
                                "url": pic_bili,
                                "size": "full",
                                "aspectMode": "cover",
                                "aspectRatio": "3:4",
                                "gravity": "top"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": anime_name,
                                                "size": "xl",
                                                "color": "#ffffff",
                                                "weight": "bold"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "哔哩哔哩(゜-゜)つロ干杯~-bilibili",
                                                "color": "#ebebeb",
                                                "size": "sm",
                                                "offsetBottom": "1px"
                                            }
                                        ],
                                        "spacing": "lg"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "filler"
                                            },
                                            {
                                                "type": "box",
                                                "layout": "baseline",
                                                "contents": [
                                                    {
                                                        "type": "filler"
                                                    },
                                                    {
                                                        "type": "text",
                                                        "text": "立即前往觀看",
                                                        "color": "#ffffff",
                                                        "flex": 0,
                                                        "offsetTop": "-2px"
                                                    },
                                                    {
                                                        "type": "filler"
                                                    }
                                                ],
                                                "spacing": "sm"
                                            },
                                            {
                                                "type": "filler"
                                            }
                                        ],
                                        "borderWidth": "1px",
                                        "cornerRadius": "4px",
                                        "spacing": "sm",
                                        "borderColor": "#ffffff",
                                        "margin": "xxl",
                                        "height": "40px",
                                        "action": {
                                            "type": "uri",
                                            "label": "action",
                                            "uri": url_bili
                                        }
                                    }
                                ],
                                "position": "absolute",
                                "offsetBottom": "0px",
                                "offsetStart": "0px",
                                "offsetEnd": "0px",
                                "backgroundColor": "#6DA3BCBB",
                                "paddingAll": "20px",
                                "paddingTop": "18px"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "filler"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "简中",
                                                "size": "xs",
                                                "color": "#ffffff",
                                                "align": "center"
                                            }
                                        ]
                                    },
                                    {
                                      "type": "filler"
                                    }
                                ],
                                "position": "absolute",
                                "cornerRadius": "20px",
                                "offsetTop": "18px",
                                "backgroundColor": "#ff334bCC",
                                "offsetStart": "18px",
                                "height": "25px",
                                "width": "53px"
                            }
                        ],
                        "paddingAll": "0px"
                    }
                },
                {
                    "type": "bubble",
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "image",
                                "url": pic_abema,
                                "size": "full",
                                "aspectMode": "cover",
                                "aspectRatio": "3:4",
                                "gravity": "top"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": anime_name,
                                                "size": "xl",
                                                "color": "#ffffff",
                                                "weight": "bold"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "AbemaTV",
                                                "color": "#ebebeb",
                                                "size": "sm",
                                                "offsetBottom": "1px"
                                            }
                                        ],
                                        "spacing": "lg"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "filler"
                                            },
                                            {
                                                "type": "box",
                                                "layout": "baseline",
                                                "contents": [
                                                    {
                                                        "type": "filler"
                                                    },
                                                    {
                                                        "type": "text",
                                                        "text": "立即前往觀看",
                                                        "color": "#ffffff",
                                                        "flex": 0,
                                                        "offsetTop": "-2px"
                                                    },
                                                    {
                                                        "type": "filler"
                                                    }
                                                ],
                                                "spacing": "sm"
                                            },
                                            {
                                                "type": "filler"
                                            }
                                        ],
                                        "borderWidth": "1px",
                                        "cornerRadius": "4px",
                                        "spacing": "sm",
                                        "borderColor": "#ffffff",
                                        "margin": "xxl",
                                        "height": "40px",
                                        "action": {
                                            "type": "uri",
                                            "label": "action",
                                            "uri": url_abema
                                        }
                                    }
                                ],
                                "position": "absolute",
                                "offsetBottom": "0px",
                                "offsetStart": "0px",
                                "offsetEnd": "0px",
                                "backgroundColor": "#494949BB",
                                "paddingAll": "20px",
                                "paddingTop": "18px"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "filler"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "日本語",
                                                "size": "xs",
                                                "color": "#ffffff",
                                                "align": "center"
                                            }
                                        ]
                                    },
                                    {
                                      "type": "filler"
                                    }
                                ],
                                "position": "absolute",
                                "cornerRadius": "20px",
                                "offsetTop": "18px",
                                "backgroundColor": "#ff334bCC",
                                "offsetStart": "18px",
                                "height": "25px",
                                "width": "53px"
                            }
                        ],
                        "paddingAll": "0px"
                    }
                }
            ]
        }    
    )
    return flex_message

# bili abema (b,c)
def Anime_Return_bc(
    url_bili,
    url_abema,
    anime_name,
    pic_bili,
    pic_abema
    ):

    flex_message = FlexSendMessage(
        alt_text = (anime_name+'動畫連結'),
        contents = {
            "type": "carousel",
            "contents": [
                {
                    "type": "bubble",
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "image",
                                "url": pic_bili,
                                "size": "full",
                                "aspectMode": "cover",
                                "aspectRatio": "3:4",
                                "gravity": "top"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": anime_name,
                                                "size": "xl",
                                                "color": "#ffffff",
                                                "weight": "bold"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "哔哩哔哩(゜-゜)つロ干杯~-bilibili",
                                                "color": "#ebebeb",
                                                "size": "sm",
                                                "offsetBottom": "1px"
                                            }
                                        ],
                                        "spacing": "lg"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "filler"
                                            },
                                            {
                                                "type": "box",
                                                "layout": "baseline",
                                                "contents": [
                                                    {
                                                        "type": "filler"
                                                    },
                                                    {
                                                        "type": "text",
                                                        "text": "立即前往觀看",
                                                        "color": "#ffffff",
                                                        "flex": 0,
                                                        "offsetTop": "-2px"
                                                    },
                                                    {
                                                        "type": "filler"
                                                    }
                                                ],
                                                "spacing": "sm"
                                            },
                                            {
                                                "type": "filler"
                                            }
                                        ],
                                        "borderWidth": "1px",
                                        "cornerRadius": "4px",
                                        "spacing": "sm",
                                        "borderColor": "#ffffff",
                                        "margin": "xxl",
                                        "height": "40px",
                                        "action": {
                                            "type": "uri",
                                            "label": "action",
                                            "uri": url_bili
                                        }
                                    }
                                ],
                                "position": "absolute",
                                "offsetBottom": "0px",
                                "offsetStart": "0px",
                                "offsetEnd": "0px",
                                "backgroundColor": "#6DA3BCBB",
                                "paddingAll": "20px",
                                "paddingTop": "18px"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "filler"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "简中",
                                                "size": "xs",
                                                "color": "#ffffff",
                                                "align": "center"
                                            }
                                        ]
                                    },
                                    {
                                      "type": "filler"
                                    }
                                ],
                                "position": "absolute",
                                "cornerRadius": "20px",
                                "offsetTop": "18px",
                                "backgroundColor": "#ff334bCC",
                                "offsetStart": "18px",
                                "height": "25px",
                                "width": "53px"
                            }
                        ],
                        "paddingAll": "0px"
                    }
                },
                {
                    "type": "bubble",
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "image",
                                "url": pic_abema,
                                "size": "full",
                                "aspectMode": "cover",
                                "aspectRatio": "3:4",
                                "gravity": "top"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": anime_name,
                                                "size": "xl",
                                                "color": "#ffffff",
                                                "weight": "bold"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "AbemaTV",
                                                "color": "#ebebeb",
                                                "size": "sm",
                                                "offsetBottom": "1px"
                                            }
                                        ],
                                        "spacing": "lg"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "filler"
                                            },
                                            {
                                                "type": "box",
                                                "layout": "baseline",
                                                "contents": [
                                                    {
                                                        "type": "filler"
                                                    },
                                                    {
                                                        "type": "text",
                                                        "text": "立即前往觀看",
                                                        "color": "#ffffff",
                                                        "flex": 0,
                                                        "offsetTop": "-2px"
                                                    },
                                                    {
                                                        "type": "filler"
                                                    }
                                                ],
                                                "spacing": "sm"
                                            },
                                            {
                                                "type": "filler"
                                            }
                                        ],
                                        "borderWidth": "1px",
                                        "cornerRadius": "4px",
                                        "spacing": "sm",
                                        "borderColor": "#ffffff",
                                        "margin": "xxl",
                                        "height": "40px",
                                        "action": {
                                            "type": "uri",
                                            "label": "action",
                                            "uri": url_abema
                                        }
                                    }
                                ],
                                "position": "absolute",
                                "offsetBottom": "0px",
                                "offsetStart": "0px",
                                "offsetEnd": "0px",
                                "backgroundColor": "#494949BB",
                                "paddingAll": "20px",
                                "paddingTop": "18px"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "filler"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "日本語",
                                                "size": "xs",
                                                "color": "#ffffff",
                                                "align": "center"
                                            }
                                        ]
                                    },
                                    {
                                      "type": "filler"
                                    }
                                ],
                                "position": "absolute",
                                "cornerRadius": "20px",
                                "offsetTop": "18px",
                                "backgroundColor": "#ff334bCC",
                                "offsetStart": "18px",
                                "height": "25px",
                                "width": "53px"
                            }
                        ],
                        "paddingAll": "0px"
                    }
                }
            ]
        }    
    )
    return flex_message

def Chino_H(
    chino_URL_1,
    chino_URL_2,
    chino_URL_3,
    chino_URL_4,
    chino_URL_5,
    chino_URL_6,
    chino_URL_7,
    chino_URL_8,
    chino_URL_9,
    chino_URL_10,
    pixiv_URL
    ):
    flex_message = FlexSendMessage(
        alt_text = ('大量智乃發生中~~'),
        contents = {
            "type": "carousel",
            "contents": [
                {
                    "type": "bubble",
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "image",
                                "url": chino_URL_1,
                                "size": "full",
                                "aspectMode": "cover",
                                "gravity": "top",
                                "aspectRatio": "3:2"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "filler"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "真崎ケイ-pixiv",
                                                "color": "#ffffff",
                                                "align": "center",
                                                "size": "xs",
                                                "offsetTop": "3px"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "filler"
                                    }
                                ],
                                "position": "absolute",
                                "cornerRadius": "20px",
                                "offsetTop": "18px",
                                "backgroundColor": "#1997E5CC",
                                "offsetStart": "18px",
                                "height": "25px",
                                "width": "100px",
                                "action": {
                                    "type": "uri",
                                    "label": "action",
                                    "uri": pixiv_URL
                                }
                            }
                        ],
                        "paddingAll": "0px"
                    }
                },
                {
                    "type": "bubble",
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "image",
                                "url": chino_URL_2,
                                "size": "full",
                                "aspectMode": "cover",
                                "gravity": "top",
                                "aspectRatio": "3:2"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "filler"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "真崎ケイ-pixiv",
                                                "color": "#ffffff",
                                                "align": "center",
                                                "size": "xs",
                                                "offsetTop": "3px"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "filler"
                                    }
                                ],
                                "position": "absolute",
                                "cornerRadius": "20px",
                                "offsetTop": "18px",
                                "backgroundColor": "#1997E5CC",
                                "offsetStart": "18px",
                                "height": "25px",
                                "width": "100px",
                                "action": {
                                    "type": "uri",
                                    "label": "action",
                                    "uri": pixiv_URL
                                }
                            }
                        ],
                        "paddingAll": "0px"
                    }
                },
                {
                    "type": "bubble",
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "image",
                                "url": chino_URL_3,
                                "size": "full",
                                "aspectMode": "cover",
                                "gravity": "top",
                                "aspectRatio": "3:2"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "filler"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "真崎ケイ-pixiv",
                                                "color": "#ffffff",
                                                "align": "center",
                                                "size": "xs",
                                                "offsetTop": "3px"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "filler"
                                    }
                                ],
                                "position": "absolute",
                                "cornerRadius": "20px",
                                "offsetTop": "18px",
                                "backgroundColor": "#1997E5CC",
                                "offsetStart": "18px",
                                "height": "25px",
                                "width": "100px",
                                "action": {
                                    "type": "uri",
                                    "label": "action",
                                    "uri": pixiv_URL
                                }
                            }
                        ],
                        "paddingAll": "0px"
                    }
                },
                {
                    "type": "bubble",
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "image",
                                "url": chino_URL_4,
                                "size": "full",
                                "aspectMode": "cover",
                                "gravity": "top",
                                "aspectRatio": "3:2"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "filler"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "真崎ケイ-pixiv",
                                                "color": "#ffffff",
                                                "align": "center",
                                                "size": "xs",
                                                "offsetTop": "3px"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "filler"
                                    }
                                ],
                                "position": "absolute",
                                "cornerRadius": "20px",
                                "offsetTop": "18px",
                                "backgroundColor": "#1997E5CC",
                                "offsetStart": "18px",
                                "height": "25px",
                                "width": "100px",
                                "action": {
                                    "type": "uri",
                                    "label": "action",
                                    "uri": pixiv_URL
                                }
                            }
                        ],
                        "paddingAll": "0px"
                    }
                },
                {
                    "type": "bubble",
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "image",
                                "url": chino_URL_5,
                                "size": "full",
                                "aspectMode": "cover",
                                "gravity": "top",
                                "aspectRatio": "3:2"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "filler"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "真崎ケイ-pixiv",
                                                "color": "#ffffff",
                                                "align": "center",
                                                "size": "xs",
                                                "offsetTop": "3px"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "filler"
                                    }
                                ],
                                "position": "absolute",
                                "cornerRadius": "20px",
                                "offsetTop": "18px",
                                "backgroundColor": "#1997E5CC",
                                "offsetStart": "18px",
                                "height": "25px",
                                "width": "100px",
                                "action": {
                                    "type": "uri",
                                    "label": "action",
                                    "uri": pixiv_URL
                                }
                            }
                        ],
                        "paddingAll": "0px"
                    }
                },
                {
                    "type": "bubble",
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "image",
                                "url": chino_URL_6,
                                "size": "full",
                                "aspectMode": "cover",
                                "gravity": "top",
                                "aspectRatio": "3:2"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "filler"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "真崎ケイ-pixiv",
                                                "color": "#ffffff",
                                                "align": "center",
                                                "size": "xs",
                                                "offsetTop": "3px"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "filler"
                                    }
                                ],
                                "position": "absolute",
                                "cornerRadius": "20px",
                                "offsetTop": "18px",
                                "backgroundColor": "#1997E5CC",
                                "offsetStart": "18px",
                                "height": "25px",
                                "width": "100px",
                                "action": {
                                    "type": "uri",
                                    "label": "action",
                                    "uri": pixiv_URL
                                }
                            }
                        ],
                        "paddingAll": "0px"
                    }
                },
                {
                    "type": "bubble",
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "image",
                                "url": chino_URL_7,
                                "size": "full",
                                "aspectMode": "cover",
                                "gravity": "top",
                                "aspectRatio": "3:2"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "filler"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "真崎ケイ-pixiv",
                                                "color": "#ffffff",
                                                "align": "center",
                                                "size": "xs",
                                                "offsetTop": "3px"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "filler"
                                    }
                                ],
                                "position": "absolute",
                                "cornerRadius": "20px",
                                "offsetTop": "18px",
                                "backgroundColor": "#1997E5CC",
                                "offsetStart": "18px",
                                "height": "25px",
                                "width": "100px",
                                "action": {
                                    "type": "uri",
                                    "label": "action",
                                    "uri": pixiv_URL
                                }
                            }
                        ],
                        "paddingAll": "0px"
                    }
                },
                {
                    "type": "bubble",
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "image",
                                "url": chino_URL_8,
                                "size": "full",
                                "aspectMode": "cover",
                                "gravity": "top",
                                "aspectRatio": "3:2"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "filler"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "真崎ケイ-pixiv",
                                                "color": "#ffffff",
                                                "align": "center",
                                                "size": "xs",
                                                "offsetTop": "3px"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "filler"
                                    }
                                ],
                                "position": "absolute",
                                "cornerRadius": "20px",
                                "offsetTop": "18px",
                                "backgroundColor": "#1997E5CC",
                                "offsetStart": "18px",
                                "height": "25px",
                                "width": "100px",
                                "action": {
                                    "type": "uri",
                                    "label": "action",
                                    "uri": pixiv_URL
                                }
                            }
                        ],
                        "paddingAll": "0px"
                    }
                },
                {
                    "type": "bubble",
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "image",
                                "url": chino_URL_9,
                                "size": "full",
                                "aspectMode": "cover",
                                "gravity": "top",
                                "aspectRatio": "3:2"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "filler"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "真崎ケイ-pixiv",
                                                "color": "#ffffff",
                                                "align": "center",
                                                "size": "xs",
                                                "offsetTop": "3px"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "filler"
                                    }
                                ],
                                "position": "absolute",
                                "cornerRadius": "20px",
                                "offsetTop": "18px",
                                "backgroundColor": "#1997E5CC",
                                "offsetStart": "18px",
                                "height": "25px",
                                "width": "100px",
                                "action": {
                                    "type": "uri",
                                    "label": "action",
                                    "uri": pixiv_URL
                                }
                            }
                        ],
                        "paddingAll": "0px"
                    }
                },
                {
                    "type": "bubble",
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "image",
                                "url": chino_URL_10,
                                "size": "full",
                                "aspectMode": "cover",
                                "gravity": "top",
                                "aspectRatio": "3:2"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "filler"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "真崎ケイ-pixiv",
                                                "color": "#ffffff",
                                                "align": "center",
                                                "size": "xs",
                                                "offsetTop": "3px"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "filler"
                                    }
                                ],
                                "position": "absolute",
                                "cornerRadius": "20px",
                                "offsetTop": "18px",
                                "backgroundColor": "#1997E5CC",
                                "offsetStart": "18px",
                                "height": "25px",
                                "width": "100px",
                                "action": {
                                    "type": "uri",
                                    "label": "action",
                                    "uri": pixiv_URL
                                }
                            }
                        ],
                        "paddingAll": "0px"
                    }
                }
            ]
        }
    )
    return flex_message