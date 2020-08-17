#============================================================
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *
# linebbot_std made node json in python
#============================================================
def Log():
    flex_message = FlexSendMessage(
        alt_text = "使用教學指令",
#        quick_reply=QuickClick(),
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
                                "type": "text",
                                "text": "#log功能集",
                                "weight": "bold",
                                "size": "xl",
                                "align": "start",
                                "offsetBottom": "5px",
                                "color": "#9F1D2C"
                            },
                            {
                                "type": "separator",
                                "color": "#9F1D2C"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "margin": "lg",
                                "spacing": "sm",
                                "contents": [
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "公連角色梗、圖片支援！",
                                                "wrap": True,
                                                "color": "#666666",
                                                "size": "lg",
                                                "flex": 5,
                                                "weight": "bold"
                                            }
                                        ],
                                        "offsetTop": "-3px"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "直接輸入便可使用(包含指令)",
                                                "color": "#aaaaaa",
                                                "size": "sm",
                                                "flex": 1
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": " ex. 台女、8歲、#求圖...",
                                                "color": "#aaaaaa",
                                                "size": "sm",
                                                "flex": 1
                                            }
                                        ]
                                    },
                                    {
                                        "type": "separator",
                                        "color": "#9F1D2C"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "群組梗圖回應~~",
                                                "wrap": True,
                                                "color": "#666666",
                                                "size": "lg",
                                                "flex": 5,
                                                "weight": "bold"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "偵測使用者輸入回應關鍵字或圖片",
                                                "color": "#aaaaaa",
                                                "size": "sm",
                                                "flex": 1
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": " ex. 我就xx、大佬、射爆...",
                                                "color": "#aaaaaa",
                                                "size": "sm",
                                                "flex": 1
                                            }
                                        ]
                                    },
                                    {
                                        "type": "separator",
                                        "color": "#9F1D2C"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "動畫超連結指令(開發中)",
                                                "wrap": True,
                                                "color": "#666666",
                                                "size": "lg",
                                                "flex": 5,
                                                "weight": "bold"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "目前提供以下3種正版通路",
                                                "color": "#aaaaaa",
                                                "size": "sm",
                                                "flex": 1
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "巴哈母特動漫瘋、bili、Abema",
                                                "color": "#aaaaaa",
                                                "size": "sm",
                                                "flex": 1
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "輸入 #動畫 + 你想要看的動畫(季數)",
                                                "color": "#aaaaaa",
                                                "size": "sm",
                                                "flex": 1
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "ex. #動畫 公連、#動畫 輝夜 第二季...",
                                                "color": "#aaaaaa",
                                                "size": "sm",
                                                "flex": 1
                                            }
                                        ]
                                    }
                                ]
                            }
                        ]
                    },
                    "size": "kilo"
                },
                {
                    "type": "bubble",
                    "header": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "spacer",
                                "size": "xl"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "spacer",
                                        "size": "xl"
                                    }
                                ]
                            },
                            {
                                "type": "image",
                                "url": "https://i.imgur.com/hlcPfy4.jpg",
                                "position": "absolute",
                                "offsetTop": "-70px",
                                "aspectMode": "fit",
                                "size": "full",
                                "offsetStart": "12px"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "spacer",
                                        "size": "xl"
                                    }
                                ]
                            },
                            {
                                "type": "spacer",
                                "size": "xl"
                            }
                        ],
                        "backgroundColor": "#45A3DD",
                        "paddingTop": "19px",
                        "paddingBottom": "16px"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "使用者回覆具隨機性！！",
                                        "wrap": True,
                                        "color": "#666666",
                                        "size": "lg",
                                        "flex": 5,
                                        "weight": "bold"
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "每個行為都具有3~25種隨機性回覆",
                                        "color": "#aaaaaa",
                                        "size": "sm",
                                        "flex": 1
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "可不用擔心每次都是同樣的罐頭文",
                                        "color": "#aaaaaa",
                                        "size": "sm",
                                        "flex": 1
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "盡可能的保持新鮮感 (發出肝哭泣聲",
                                        "color": "#aaaaaa",
                                        "size": "sm",
                                        "flex": 1
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "(人家圖圖也是有限的...)",
                                        "color": "#aaaaaa",
                                        "size": "sm",
                                        "flex": 1
                                    }
                                ]
                            },
                            {
                                "type": "separator",
                                "color": "#666666"
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "順便推廣個自家FB社團~~",
                                        "color": "#666666",
                                        "size": "lg",
                                        "flex": 5,
                                        "weight": "bold"
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "超異域公主連結✩Re:Dive交流區",
                                        "color": "#3F8EBF",
                                        "size": "sm",
                                        "flex": 5,
                                        "weight": "bold"
                                    }
                                ],
                                "action": {
                                "type": "uri",
                                "label": "action",
                                "uri": "https://www.facebook.com/groups/2090300834327237"
                                }
                            }
                        ],
                        "spacing": "md",
                        "paddingAll": "12px"
                    },
                    "size": "kilo",
                    "styles": {
                        "footer": {
                            "separator": False
                        }
                    }
                },
                {
                    "type": "bubble",
                    "size": "kilo",
                    "header": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "spacer",
                                "size": "xl"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "spacer",
                                        "size": "xl"
                                    }
                                ]
                            },
                            {
                                "type": "image",
                                "url": "https://i.imgur.com/8Xl9Lmp.jpg",
                                "position": "absolute",
                                "offsetTop": "-70px",
                                "aspectMode": "fit",
                                "size": "full",
                                "offsetStart": "12px"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "spacer",
                                        "size": "xl"
                                    }
                                ]
                            },
                            {
                                "type": "spacer",
                                "size": "xl"
                            }
                        ],
                        "backgroundColor": "#45A3DD",
                        "paddingTop": "19px",
                        "paddingBottom": "16px"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "目前未提供情報...",
                                        "wrap": True,
                                        "color": "#666666",
                                        "size": "lg",
                                        "flex": 5,
                                        "weight": "bold"
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "推薦使用前輩們的布丁、可蘿機器人",
                                        "color": "#aaaaaa",
                                        "size": "sm",
                                        "flex": 1
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "(其實是作者懶懶，都沒在追情報)",
                                        "color": "#aaaaaa",
                                        "size": "sm",
                                        "flex": 1
                                    }
                                ]
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
                                                "type": "image",
                                                "url": "https://i.imgur.com/gresO8I.jpg",
                                                "aspectMode": "cover"
                                            }
                                        ],
                                        "action": {
                                            "type": "uri",
                                            "label": "action",
                                            "uri": "https://forum.gamer.com.tw/C.php?bsn=30861&snA=13556"
                                        }
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "image",
                                                "url": "https://i.imgur.com/S66w8Qz.jpg",
                                                "aspectMode": "cover"
                                            }
                                        ],
                                        "action": {
                                            "type": "uri",
                                            "label": "action",
                                            "uri": "https://forum.gamer.com.tw/C.php?bsn=30861&snA=12791"
                                        }
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "\"也特別感謝布丁機器人的生父-罕罕\"",
                                        "color": "#aaaa0050",
                                        "size": "sm",
                                        "flex": 1,
                                        "align": "center"
                                    }
                                ],
                                "offsetBottom": "-7px"
                            }
                        ],
                        "spacing": "md",
                        "paddingAll": "12px"
                    },
                    "styles": {
                        "footer": {
                            "separator": False
                        }
                    }
                },
                {
                    "type": "bubble",
                    "size": "kilo",
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": "老司機飆車啦！！",
                                "weight": "bold",
                                "size": "xl",
                                "align": "start",
                                "offsetBottom": "5px",
                                "color": "#9F1D2C"
                            },
                            {
                                "type": "separator",
                                "color": "#9F1D2C"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "margin": "lg",
                                "spacing": "sm",
                                "contents": [
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "這才是人家創機器人的初心",
                                                "wrap": True,
                                                "color": "#666666",
                                                "size": "lg",
                                                "flex": 5,
                                                "offsetTop": "-2px",
                                                "weight": "bold"
                                            }
                                        ],
                                        "offsetTop": "0px"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "沒錯你沒看錯！！(激動)",
                                                "color": "#aaaaaa",
                                                "size": "sm",
                                                "flex": 1
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "冒著前幾個機器人都被Line封鎖風險",
                                                "color": "#aaaaaa",
                                                "size": "sm",
                                                "flex": 1
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "我就發車，發色圖，拿我怎樣 (沒",
                                                "color": "#aaaaaa",
                                                "size": "sm",
                                                "flex": 1,
                                                "weight": "bold"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "separator",
                                        "color": "#9F1D2C"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "快速發車器",
                                                "wrap": True,
                                                "color": "#666666",
                                                "size": "lg",
                                                "flex": 5,
                                                "weight": "bold"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "目前支援n網&w網,e網ex網(開發中)",
                                                "color": "#aaaaaa",
                                                "size": "sm",
                                                "flex": 1
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "有很基本的防呆功能(sry了真步bot)",
                                                "color": "#aaaaaa",
                                                "size": "sm",
                                                "flex": 1
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "直接輸入想要看的網加上車號",
                                                "color": "#aaaaaa",
                                                "size": "sm",
                                                "flex": 1
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "ex. n320580，w102180...",
                                                "color": "#aaaaaa",
                                                "size": "sm",
                                                "flex": 1
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "(n站可輸入n0產生隨機本本！)",
                                                "color": "#aaaaaa",
                                                "size": "sm",
                                                "flex": 1
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "車子將於1秒內抵達官邸",
                                                "color": "#aaaaaa",
                                                "size": "sm",
                                                "flex": 1
                                            }
                                        ]
                                    }
                                ]
                            }
                        ]
                    }
                }
            ]
        }
    )
    return flex_message
# 我就xx 自定義梗圖
def image_bubble_message(link,input_message,color):
    flex_message = FlexSendMessage(
        alt_text = input_message,
#        quick_reply=QuickClick(),
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
                        "url": color,
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
#        quick_reply=QuickClick(),
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
#        quick_reply=QuickClick(),
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

# 巴哈 bili abema (a,c)
def Anime_Return_ac(
    url_baha,
    url_abema,
    anime_name,
    pic_baha,
    pic_abema
    ):
    flex_message = FlexSendMessage(
        alt_text = (anime_name+'動畫連結'),
#        quick_reply=QuickClick(),
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

# 一次放10張智乃圖
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
#        quick_reply=QuickClick(),
        contents = {
            "type": "carousel",
            "contents": [
                {
                    "type": "bubble",
                    "size": "giga",
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
                                        "type": "text",
                                        "text": "真崎ケイ-pixiv",
                                        "color": "#ffffff",
                                        "align": "center",
                                        "size": "xs",
                                        "offsetTop": "4px"
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
                    "size": "giga",
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
                                        "type": "text",
                                        "text": "真崎ケイ-pixiv",
                                        "color": "#ffffff",
                                        "align": "center",
                                        "size": "xs",
                                        "offsetTop": "4px"
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
                    "size": "giga",
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
                                        "type": "text",
                                        "text": "真崎ケイ-pixiv",
                                        "color": "#ffffff",
                                        "align": "center",
                                        "size": "xs",
                                        "offsetTop": "4px"
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
                    "size": "giga",
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
                                        "type": "text",
                                        "text": "真崎ケイ-pixiv",
                                        "color": "#ffffff",
                                        "align": "center",
                                        "size": "xs",
                                        "offsetTop": "4px"
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
                    "size": "giga",
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
                                        "type": "text",
                                        "text": "真崎ケイ-pixiv",
                                        "color": "#ffffff",
                                        "align": "center",
                                        "size": "xs",
                                        "offsetTop": "4px"
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
                    "size": "giga",
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
                                        "type": "text",
                                        "text": "真崎ケイ-pixiv",
                                        "color": "#ffffff",
                                        "align": "center",
                                        "size": "xs",
                                        "offsetTop": "4px"
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
                    "size": "giga",
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
                                        "type": "text",
                                        "text": "真崎ケイ-pixiv",
                                        "color": "#ffffff",
                                        "align": "center",
                                        "size": "xs",
                                        "offsetTop": "4px"
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
                    "size": "giga",
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
                                        "type": "text",
                                        "text": "真崎ケイ-pixiv",
                                        "color": "#ffffff",
                                        "align": "center",
                                        "size": "xs",
                                        "offsetTop": "4px"
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
                    "size": "giga",
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
                                        "type": "text",
                                        "text": "真崎ケイ-pixiv",
                                        "color": "#ffffff",
                                        "align": "center",
                                        "size": "xs",
                                        "offsetTop": "4px"
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
                    "size": "giga",
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
                                        "type": "text",
                                        "text": "真崎ケイ-pixiv",
                                        "color": "#ffffff",
                                        "align": "center",
                                        "size": "xs",
                                        "offsetTop": "4px"
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
def Hentai_Path_1(Action_but,
                URL,
                PicURL,
                Title,
                Num
    ):
    flex_message = FlexSendMessage(
        alt_text = ('現正發車中~~'),
#        quick_reply=QuickClick(),
        contents = {
            "type": "carousel",
            "contents": [
                {
                    "type": "bubble",
                    "size": "giga",
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "image",
                                "url": PicURL,
                                "size": "full",
                                "aspectMode": "cover",
                                "aspectRatio": "2:3",
                                "gravity": "top"
                            },
                            {
                                "type": "image",
                                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/flexsnapshot/clip/clip15.png",
                                "size": "full",
                                "aspectMode": "cover",
                                "aspectRatio": "2:3",
                                "gravity": "top",
                                "position": "absolute"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": Title,
                                                "size": "xl",
                                                "color": "#ffffff",
                                                "weight": "bold",
                                                "wrap": True
                                            }
                                        ],
                                        "offsetTop": "16px"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "size": "sm",
                                                "color": "#ffffff",
                                                "wrap": True,
                                                "text": "n"+Num,
                                                "align": "end",
                                                "weight": "bold",
                                                "offsetTop": "5px"
                                            },
                                            {
                                                "type": "icon",
                                                "url": "https://i.imgur.com/uLAimaY.png",
                                                "size": "xxl",
                                                "offsetTop": "12px"
                                            }
                                        ],
                                        "offsetTop": "8px",
                                        "paddingBottom": "2px"
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
                                                        "text": Action_but,
                                                        "color": "#ffffff",
                                                        "flex": 0,
                                                        "offsetBottom": "3px"
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
                                            "uri": URL
                                        }
                                    }
                                ],
                                "position": "absolute",
                                "offsetBottom": "0px",
                                "offsetStart": "0px",
                                "offsetEnd": "0px",
                                "backgroundColor": "#494949BB",
                                "paddingAll": "20px",
                                "paddingTop": "0px"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "nhentai.net",
                                        "color": "#ff334b",
                                        "align": "center",
                                        "size": "xs",
                                        "offsetTop": "4px"
                                    }
                                ],
                                "position": "absolute",
                                "cornerRadius": "20px",
                                "offsetTop": "18px",
                                "backgroundColor": "#000000aa",
                                "offsetStart": "18px",
                                "height": "25px",
                                "width": "90px",
                                "action": {
                                    "type": "uri",
                                    "label": "action",
                                    "uri": "https://nhentai.net/"
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

def Hentai_Path(Action_but,
                URL,
                PicURL,
                Title,
                Num,
                #recommand
                site_1,
                name_1,
                picture_1,
                number_1,
                site_2,
                name_2,
                picture_2,
                number_2,
                site_3,
                name_3,
                picture_3,
                number_3,
                site_4,
                name_4,
                picture_4,
                number_4,
                site_5,
                name_5,
                picture_5,
                number_5
    ):
    flex_message = FlexSendMessage(
        alt_text = ('n網現正發車中~~'),
#        quick_reply=QuickClick(),
        contents = {
            "type": "carousel",
            "contents": [
                {
                    "type": "bubble",
                    "size": "giga",
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "image",
                                "url": PicURL,
                                "size": "full",
                                "aspectMode": "cover",
                                "aspectRatio": "2:3",
                                "gravity": "top"
                            },
                            {
                                "type": "image",
                                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/flexsnapshot/clip/clip15.png",
                                "size": "full",
                                "aspectMode": "cover",
                                "aspectRatio": "2:3",
                                "gravity": "top",
                                "position": "absolute"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": Title,
                                                "size": "xl",
                                                "color": "#ffffff",
                                                "weight": "bold",
                                                "wrap": True
                                            }
                                        ],
                                        "offsetTop": "16px"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "size": "sm",
                                                "color": "#ffffff",
                                                "wrap": True,
                                                "text": "n"+Num,
                                                "align": "end",
                                                "weight": "bold",
                                                "offsetTop": "5px"
                                            },
                                            {
                                                "type": "icon",
                                                "url": "https://i.imgur.com/uLAimaY.png",
                                                "size": "xxl",
                                                "offsetTop": "12px"
                                            }
                                        ],
                                        "offsetTop": "8px",
                                        "paddingBottom": "2px"
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
                                                        "text": Action_but,
                                                        "color": "#ffffff",
                                                        "flex": 0,
                                                        "offsetBottom": "3px"
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
                                            "uri": URL
                                        }
                                    }
                                ],
                                "position": "absolute",
                                "offsetBottom": "0px",
                                "offsetStart": "0px",
                                "offsetEnd": "0px",
                                "backgroundColor": "#494949BB",
                                "paddingAll": "20px",
                                "paddingTop": "0px"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "nhentai.net",
                                        "color": "#ff334b",
                                        "align": "center",
                                        "size": "xs",
                                        "offsetTop": "4px"
                                    }
                                ],
                                "position": "absolute",
                                "cornerRadius": "20px",
                                "offsetTop": "18px",
                                "backgroundColor": "#000000aa",
                                "offsetStart": "18px",
                                "height": "25px",
                                "width": "90px",
                                "action": {
                                    "type": "uri",
                                    "label": "action",
                                    "uri": "https://nhentai.net/"
                                }
                            }
                        ],
                        "paddingAll": "0px"
                    }
                },
                {
                    "type": "bubble",
                    "size": "giga",
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "image",
                                "url": picture_1,
                                "size": "full",
                                "aspectRatio": "2:3",
                                "gravity": "top",
                                "aspectMode": "cover"
                            },
                            {
                                "type": "image",
                                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/flexsnapshot/clip/clip15.png",
                                "size": "full",
                                "aspectMode": "cover",
                                "aspectRatio": "2:3",
                                "gravity": "top",
                                "position": "absolute"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": name_1,
                                                "size": "xl",
                                                "color": "#ffffff",
                                                "weight": "bold",
                                                "wrap": True
                                            }
                                        ],
                                        "offsetTop": "16px"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "size": "sm",
                                                "color": "#ffffff",
                                                "wrap": True,
                                                "text": "n"+number_1,
                                                "align": "end",
                                                "weight": "bold",
                                                "offsetTop": "5px"
                                            },
                                            {
                                                "type": "icon",
                                                "url": "https://i.imgur.com/uLAimaY.png",
                                                "size": "xxl",
                                                "offsetTop": "12px"
                                            }
                                        ],
                                        "offsetTop": "8px",
                                        "paddingBottom": "2px"
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
                                                        "text": Action_but,
                                                        "color": "#ffffff",
                                                        "flex": 0,
                                                        "offsetBottom": "3px"
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
                                            "uri": site_1
                                        }
                                    }
                                ],
                                "position": "absolute",
                                "offsetBottom": "0px",
                                "offsetStart": "0px",
                                "offsetEnd": "0px",
                                "backgroundColor": "#494949BB",
                                "paddingAll": "20px",
                                "paddingTop": "0px"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "相似推薦",
                                        "color": "#ffffff",
                                        "align": "center",
                                        "size": "xs",
                                        "offsetTop": "4px"
                                    }
                                ],
                                "position": "absolute",
                                "cornerRadius": "20px",
                                "offsetTop": "18px",
                                "backgroundColor": "#ff334bCC",
                                "offsetStart": "18px",
                                "height": "25px",
                                "width": "75px"
                            }
                        ],
                        "paddingAll": "0px"
                    }
                },
                {
                    "type": "bubble",
                    "size": "giga",
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "image",
                                "url": picture_2,
                                "size": "full",
                                "aspectRatio": "2:3",
                                "gravity": "top",
                                "aspectMode": "cover"
                            },
                            {
                                "type": "image",
                                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/flexsnapshot/clip/clip15.png",
                                "size": "full",
                                "aspectMode": "cover",
                                "aspectRatio": "2:3",
                                "gravity": "top",
                                "position": "absolute"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": name_2,
                                                "size": "xl",
                                                "color": "#ffffff",
                                                "weight": "bold",
                                                "wrap": True
                                            }
                                        ],
                                        "offsetTop": "16px"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "size": "sm",
                                                "color": "#ffffff",
                                                "wrap": True,
                                                "text": "n"+number_2,
                                                "align": "end",
                                                "weight": "bold",
                                                "offsetTop": "5px"
                                            },
                                            {
                                                "type": "icon",
                                                "url": "https://i.imgur.com/uLAimaY.png",
                                                "size": "xxl",
                                                "offsetTop": "12px"
                                            }
                                        ],
                                        "offsetTop": "8px",
                                        "paddingBottom": "2px"
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
                                                        "text": Action_but,
                                                        "color": "#ffffff",
                                                        "flex": 0,
                                                        "offsetBottom": "3px"
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
                                            "uri": site_2
                                        }
                                    }
                                ],
                                "position": "absolute",
                                "offsetBottom": "0px",
                                "offsetStart": "0px",
                                "offsetEnd": "0px",
                                "backgroundColor": "#494949BB",
                                "paddingAll": "20px",
                                "paddingTop": "0px"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "相似推薦",
                                        "color": "#ffffff",
                                        "align": "center",
                                        "size": "xs",
                                        "offsetTop": "4px"
                                    }
                                ],
                                "position": "absolute",
                                "cornerRadius": "20px",
                                "offsetTop": "18px",
                                "backgroundColor": "#ff334bCC",
                                "offsetStart": "18px",
                                "height": "25px",
                                "width": "75px"
                            }
                        ],
                        "paddingAll": "0px"
                    }
                },
                {
                    "type": "bubble",
                    "size": "giga",
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "image",
                                "url": picture_3,
                                "size": "full",
                                "aspectRatio": "2:3",
                                "gravity": "top",
                                "aspectMode": "cover"
                            },
                            {
                                "type": "image",
                                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/flexsnapshot/clip/clip15.png",
                                "size": "full",
                                "aspectMode": "cover",
                                "aspectRatio": "2:3",
                                "gravity": "top",
                                "position": "absolute"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": name_3,
                                                "size": "xl",
                                                "color": "#ffffff",
                                                "weight": "bold",
                                                "wrap": True
                                            }
                                        ],
                                        "offsetTop": "16px"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "size": "sm",
                                                "color": "#ffffff",
                                                "wrap": True,
                                                "text": "n"+number_3,
                                                "align": "end",
                                                "weight": "bold",
                                                "offsetTop": "5px"
                                            },
                                            {
                                                "type": "icon",
                                                "url": "https://i.imgur.com/uLAimaY.png",
                                                "size": "xxl",
                                                "offsetTop": "12px"
                                            }
                                        ],
                                        "offsetTop": "8px",
                                        "paddingBottom": "2px"
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
                                                        "text": Action_but,
                                                        "color": "#ffffff",
                                                        "flex": 0,
                                                        "offsetBottom": "3px"
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
                                            "uri": site_3
                                        }
                                    }
                                ],
                                "position": "absolute",
                                "offsetBottom": "0px",
                                "offsetStart": "0px",
                                "offsetEnd": "0px",
                                "backgroundColor": "#494949BB",
                                "paddingAll": "20px",
                                "paddingTop": "0px"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "相似推薦",
                                        "color": "#ffffff",
                                        "align": "center",
                                        "size": "xs",
                                        "offsetTop": "4px"
                                    }
                                ],
                                "position": "absolute",
                                "cornerRadius": "20px",
                                "offsetTop": "18px",
                                "backgroundColor": "#ff334bCC",
                                "offsetStart": "18px",
                                "height": "25px",
                                "width": "75px"
                            }
                        ],
                        "paddingAll": "0px"
                    }
                },
                {
                    "type": "bubble",
                    "size": "giga",
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "image",
                                "url": picture_4,
                                "size": "full",
                                "aspectRatio": "2:3",
                                "gravity": "top",
                                "aspectMode": "cover"
                            },
                            {
                                "type": "image",
                                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/flexsnapshot/clip/clip15.png",
                                "size": "full",
                                "aspectMode": "cover",
                                "aspectRatio": "2:3",
                                "gravity": "top",
                                "position": "absolute"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": name_4,
                                                "size": "xl",
                                                "color": "#ffffff",
                                                "weight": "bold",
                                                "wrap": True
                                            }
                                        ],
                                        "offsetTop": "16px"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "size": "sm",
                                                "color": "#ffffff",
                                                "wrap": True,
                                                "text": "n"+number_4,
                                                "align": "end",
                                                "weight": "bold",
                                                "offsetTop": "5px"
                                            },
                                            {
                                                "type": "icon",
                                                "url": "https://i.imgur.com/uLAimaY.png",
                                                "size": "xxl",
                                                "offsetTop": "12px"
                                            }
                                        ],
                                        "offsetTop": "8px",
                                        "paddingBottom": "2px"
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
                                                        "text": Action_but,
                                                        "color": "#ffffff",
                                                        "flex": 0,
                                                        "offsetBottom": "3px"
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
                                            "uri": site_4
                                        }
                                    }
                                ],
                                "position": "absolute",
                                "offsetBottom": "0px",
                                "offsetStart": "0px",
                                "offsetEnd": "0px",
                                "backgroundColor": "#494949BB",
                                "paddingAll": "20px",
                                "paddingTop": "0px"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "相似推薦",
                                        "color": "#ffffff",
                                        "align": "center",
                                        "size": "xs",
                                        "offsetTop": "4px"
                                    }
                                ],
                                "position": "absolute",
                                "cornerRadius": "20px",
                                "offsetTop": "18px",
                                "backgroundColor": "#ff334bCC",
                                "offsetStart": "18px",
                                "height": "25px",
                                "width": "75px"
                            }
                        ],
                        "paddingAll": "0px"
                    }
                },
                {
                    "type": "bubble",
                    "size": "giga",
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "image",
                                "url": picture_5,
                                "size": "full",
                                "aspectRatio": "2:3",
                                "gravity": "top",
                                "aspectMode": "cover"
                            },
                            {
                                "type": "image",
                                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/flexsnapshot/clip/clip15.png",
                                "size": "full",
                                "aspectMode": "cover",
                                "aspectRatio": "2:3",
                                "gravity": "top",
                                "position": "absolute"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": name_5,
                                                "size": "xl",
                                                "color": "#ffffff",
                                                "weight": "bold",
                                                "wrap": True
                                            }
                                        ],
                                        "offsetTop": "16px"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "size": "sm",
                                                "color": "#ffffff",
                                                "wrap": True,
                                                "text": "n"+number_5,
                                                "align": "end",
                                                "weight": "bold",
                                                "offsetTop": "5px"
                                            },
                                            {
                                                "type": "icon",
                                                "url": "https://i.imgur.com/uLAimaY.png",
                                                "size": "xxl",
                                                "offsetTop": "12px"
                                            }
                                        ],
                                        "offsetTop": "8px",
                                        "paddingBottom": "2px"
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
                                                        "text": Action_but,
                                                        "color": "#ffffff",
                                                        "flex": 0,
                                                        "offsetBottom": "3px"
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
                                            "uri": site_5
                                        }
                                    }
                                ],
                                "position": "absolute",
                                "offsetBottom": "0px",
                                "offsetStart": "0px",
                                "offsetEnd": "0px",
                                "backgroundColor": "#494949BB",
                                "paddingAll": "20px",
                                "paddingTop": "0px"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "相似推薦",
                                        "color": "#ffffff",
                                        "align": "center",
                                        "size": "xs",
                                        "offsetTop": "4px"
                                    }
                                ],
                                "position": "absolute",
                                "cornerRadius": "20px",
                                "offsetTop": "18px",
                                "backgroundColor": "#ff334bCC",
                                "offsetStart": "18px",
                                "height": "25px",
                                "width": "75px"
                            }
                        ],
                        "paddingAll": "0px"
                    }
                }
            ]
        }
    )
    return flex_message


# w網發車
def Hentai_Path_W(
                Action_but,
                URL,
                PicURL,
                Title,
                Num
    ):
    flex_message = FlexSendMessage(
        alt_text = 'w網現正發車中~~',
#        quick_reply=QuickClick(),
        contents = {
            "type": "carousel",
            "contents": [
                {
                    "type": "bubble",
                    "size": "giga",
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "image",
                                "url": PicURL,
                                "size": "full",
                                "aspectRatio": "2:3",
                                "aspectMode": "cover"
                            },
                            {
                                "type": "image",
                                "url": "https://i.imgur.com/1nKb4qO.png",
                                "position": "absolute",
                                "size": "full",
                                "offsetTop": "0px",
                                "offsetBottom": "0px",
                                "offsetStart": "0px",
                                "offsetEnd": "0px",
                                "aspectRatio": "2:3",
                                "aspectMode": "cover"
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
                                                "text": Title,
                                                "size": "xl",
                                                "color": "#1C4C58",
                                                "weight": "bold",
                                                "wrap": True
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": 'w'+Num,
                                                "color": "#1C4C58aa",
                                                "size": "sm",
                                                "flex": 0,
                                                "align": "end"
                                            }
                                        ],
                                        "spacing": "lg",
                                        "offsetTop": "10px"
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
                                                        "text": Action_but,
                                                        "color": "#1C4C58",
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
                                        "borderColor": "#1C4C58",
                                        "margin": "xxl",
                                        "height": "40px",
                                        "action": {
                                            "type": "uri",
                                            "label": "action",
                                            "uri": URL
                                        }
                                    }
                                ],
                                "position": "absolute",
                                "offsetBottom": "0px",
                                "offsetStart": "0px",
                                "offsetEnd": "0px",
                                "backgroundColor": "#eeeeeebb",
                                "paddingAll": "20px",
                                "paddingTop": "18px"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "wnacg.org",
                                        "color": "#ffffff",
                                        "align": "center",
                                        "size": "xs",
                                        "offsetTop": "4px"
                                    }
                                ],
                                "position": "absolute",
                                "cornerRadius": "20px",
                                "offsetTop": "18px",
                                "backgroundColor": "#1C4C58cc",
                                "offsetStart": "18px",
                                "height": "25px",
                                "width": "85px",
                                "action": {
                                    "type": "uri",
                                    "label": "action",
                                    "uri": "http://wnacg.org/albums.html"
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


# 抽卡
def Capsule_Gotcha(
        card_rarity_0,
        card_rarity_1,
        card_rarity_2,
        card_rarity_3,
        card_rarity_4,
        card_rarity_5,
        card_rarity_6,
        card_rarity_7,
        card_rarity_8,
        card_rarity_9,
        COLOUR_position_0,
        COLOUR_position_1,
        COLOUR_position_2,
        COLOUR_position_3,
        COLOUR_position_4,
        COLOUR_position_5,
        COLOUR_position_6,
        COLOUR_position_7,
        COLOUR_position_8,
        COLOUR_position_9,
        chara_name_0,
        chara_name_1,
        chara_name_2,
        chara_name_3,
        chara_name_4,
        chara_name_5,
        chara_name_6,
        chara_name_7,
        chara_name_8,
        chara_name_9,
        chara_picURL_0,
        chara_picURL_1,
        chara_picURL_2,
        chara_picURL_3,
        chara_picURL_4,
        chara_picURL_5,
        chara_picURL_6,
        chara_picURL_7,
        chara_picURL_8,
        chara_picURL_9,
        COL,
        GOL,
        SLI,
        COL_Probability
    ):
    flex_message = FlexSendMessage(
        alt_text = '母珠石呷飽飽',
#        quick_reply=QuickClick(),
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
                                "url": "https://i.imgur.com/hfa4tSd.jpg",
                                "size": "full",
                                "aspectRatio": "1528:860"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "box",
                                        "layout": "horizontal",
                                        "contents": [
                                            {
                                                "type": "image",
                                                "url": card_rarity_0,
                                                "size": "xs",
                                                "offsetStart": "15px",
                                                "align": "start",
                                                "offsetTop": "20px"
                                            },
                                            {
                                                "type": "image",
                                                "url": card_rarity_1,
                                                "size": "xs",
                                                "offsetStart": "7px",
                                                "align": "start",
                                                "offsetTop": "17px"
                                            },
                                            {
                                                "type": "image",
                                                "url": card_rarity_2,
                                                "size": "xs",
                                                "offsetStart": "-1px",
                                                "align": "start",
                                                "offsetTop": "20px"
                                            },
                                            {
                                                "type": "image",
                                                "url": card_rarity_3,
                                                "size": "xs",
                                                "offsetStart": "-9px",
                                                "align": "start",
                                                "offsetTop": "17px"
                                            },
                                            {
                                                "type": "image",
                                                "url": card_rarity_4,
                                                "size": "xs",
                                                "offsetStart": "-16px",
                                                "align": "start",
                                                "offsetTop": "20px"
                                            },
                                            {
                                                "type": "image",
                                                "url": "https://i.imgur.com/FmSZ2Ms.png",
                                                "size": "md",
                                                "offsetStart": COLOUR_position_0+"px",
                                                "align": "start",
                                                "offsetTop": "1px",
                                                "position": "absolute"
                                            },
                                            {
                                                "type": "image",
                                                "url": "https://i.imgur.com/FmSZ2Ms.png",
                                                "size": "md",
                                                "offsetStart": COLOUR_position_1+"px",
                                                "align": "start",
                                                "offsetTop": "-2px",
                                                "position": "absolute"
                                            },
                                            {
                                                "type": "image",
                                                "url": "https://i.imgur.com/FmSZ2Ms.png",
                                                "size": "md",
                                                "offsetStart": COLOUR_position_2+"px",
                                                "align": "start",
                                                "offsetTop": "1px",
                                                "position": "absolute"
                                            },
                                            {
                                                "type": "image",
                                                "url": "https://i.imgur.com/FmSZ2Ms.png",
                                                "size": "md",
                                                "offsetStart": COLOUR_position_3+"px",
                                                "align": "start",
                                                "offsetTop": "-2px",
                                                "position": "absolute"
                                            },
                                            {
                                                "type": "image",
                                                "url": "https://i.imgur.com/FmSZ2Ms.png",
                                                "size": "md",
                                                "offsetStart": COLOUR_position_4+"px",
                                                "align": "start",
                                                "offsetTop": "1px",
                                                "position": "absolute"
                                            }
                                        ],
                                        "width": "300px",
                                        "height": "90px"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "horizontal",
                                        "contents": [
                                            {
                                                "type": "image",
                                                "url": card_rarity_5,
                                                "size": "xs",
                                                "offsetStart": "15px",
                                                "align": "start"
                                            },
                                            {
                                                "type": "image",
                                                "url": card_rarity_6,
                                                "size": "xs",
                                                "offsetStart": "7px",
                                                "align": "start",
                                                "offsetTop": "3px"
                                            },
                                            {
                                                "type": "image",
                                                "url": card_rarity_7,
                                                "size": "xs",
                                                "offsetStart": "-1px",
                                                "align": "start",
                                                "offsetTop": "5px"
                                            },
                                            {
                                                "type": "image",
                                                "url": card_rarity_8,
                                                "size": "xs",
                                                "offsetStart": "-9px",
                                                "align": "start",
                                                "offsetTop": "3px"
                                            },
                                            {
                                                "type": "image",
                                                "url": card_rarity_9,
                                                "size": "xs",
                                                "offsetStart": "-16px",
                                                "align": "start",
                                                "offsetTop": "4px"
                                            },
                                            {
                                                "type": "image",
                                                "url": "https://i.imgur.com/FmSZ2Ms.png",
                                                "size": "md",
                                                "offsetStart": COLOUR_position_5+"px",
                                                "align": "start",
                                                "offsetTop": "-19px",
                                                "position": "absolute"
                                            },
                                            {
                                                "type": "image",
                                                "url": "https://i.imgur.com/FmSZ2Ms.png",
                                                "size": "md",
                                                "offsetStart": COLOUR_position_6+"px",
                                                "align": "start",
                                                "offsetTop": "-16px",
                                                "position": "absolute"
                                            },
                                            {
                                                "type": "image",
                                                "url": "https://i.imgur.com/FmSZ2Ms.png",
                                                "size": "md",
                                                "offsetStart": COLOUR_position_7+"px",
                                                "align": "start",
                                                "offsetTop": "-14px",
                                                "position": "absolute"
                                            },
                                            {
                                                "type": "image",
                                                "url": "https://i.imgur.com/FmSZ2Ms.png",
                                                "size": "md",
                                                "offsetStart": COLOUR_position_8+"px",
                                                "align": "start",
                                                "offsetTop": "-16px",
                                                "position": "absolute"
                                            },
                                            {
                                                "type": "image",
                                                "url": "https://i.imgur.com/FmSZ2Ms.png",
                                                "size": "md",
                                                "offsetStart": COLOUR_position_9+"px",
                                                "align": "start",
                                                "offsetTop": "-15px",
                                                "position": "absolute"
                                            }
                                        ],
                                        "width": "300px",
                                        "height": "90px"
                                    }
                                ],
                                "position": "absolute"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "image",
                                        "url": "https://i.imgur.com/T5cTl6w.jpg",
                                        "size": "full",
                                        "aspectRatio": "1528:860"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "box",
                                                "layout": "horizontal",
                                                "contents": [
                                                    {
                                                        "type": "image",
                                                        "url": chara_picURL_0,
                                                        "size": "xxs",
                                                        "action": {
                                                            "type": "message",
                                                            "label": "action",
                                                            "text": chara_name_0
                                                        },
                                                        "gravity": "center",
                                                        "align": "end"
                                                    },
                                                    {
                                                        "type": "image",
                                                        "url": chara_picURL_1,
                                                        "size": "xxs",
                                                        "action": {
                                                            "type": "message",
                                                            "label": "action",
                                                            "text": chara_name_1
                                                        },
                                                        "gravity": "center"
                                                    },
                                                    {
                                                        "type": "image",
                                                        "url": chara_picURL_2,
                                                        "size": "xxs",
                                                        "action": {
                                                            "type": "message",
                                                            "label": "action",
                                                            "text": chara_name_2
                                                        },
                                                        "gravity": "center",
                                                        "align": "start"
                                                    },
                                                    {
                                                        "type": "image",
                                                        "url": chara_picURL_3,
                                                        "size": "xxs",
                                                        "action": {
                                                            "type": "message",
                                                            "label": "action",
                                                            "text": chara_name_3
                                                        },
                                                        "gravity": "center",
                                                        "align": "start",
                                                        "offsetStart": "-8px"
                                                    },
                                                    {
                                                        "type": "image",
                                                        "url": chara_picURL_4,
                                                        "size": "xxs",
                                                        "action": {
                                                            "type": "message",
                                                            "label": "action",
                                                            "text": chara_name_4
                                                        },
                                                        "gravity": "center",
                                                        "align": "start",
                                                        "offsetStart": "-16px"
                                                    }
                                                ],
                                                "width": "300px",
                                                "height": "95px",
                                                "offsetStart": "8px"
                                            },
                                            {
                                                "type": "box",
                                                "layout": "horizontal",
                                                "contents": [
                                                    {
                                                        "type": "image",
                                                        "url": chara_picURL_5,
                                                        "size": "xxs",
                                                        "action": {
                                                            "type": "message",
                                                            "label": "action",
                                                            "text": chara_name_5
                                                        },
                                                        "gravity": "top",
                                                        "align": "end"
                                                    },
                                                    {
                                                        "type": "image",
                                                        "url": chara_picURL_6,
                                                        "size": "xxs",
                                                        "action": {
                                                            "type": "message",
                                                            "label": "action",
                                                            "text": chara_name_6
                                                        },
                                                        "gravity": "top"
                                                    },
                                                    {
                                                        "type": "image",
                                                        "url": chara_picURL_7,
                                                        "size": "xxs",
                                                        "action": {
                                                            "type": "message",
                                                            "label": "action",
                                                            "text": chara_name_7
                                                        },
                                                        "gravity": "top",
                                                        "align": "start"
                                                    },
                                                    {
                                                        "type": "image",
                                                        "url": chara_picURL_8,
                                                        "size": "xxs",
                                                        "action": {
                                                            "type": "message",
                                                            "label": "action",
                                                            "text": chara_name_8
                                                        },
                                                        "gravity": "top",
                                                        "align": "start",
                                                        "offsetStart": "-8px"
                                                    },
                                                    {
                                                        "type": "image",
                                                        "url": chara_picURL_9,
                                                        "size": "xxs",
                                                        "action": {
                                                            "type": "message",
                                                            "label": "action",
                                                            "text": chara_name_9
                                                        },
                                                        "gravity": "top",
                                                        "align": "start",
                                                        "offsetStart": "-16px"
                                                    }
                                                ],
                                                "width": "300px",
                                                "height": "90px",
                                                "offsetStart": "8px"
                                            }
                                        ],
                                        "position": "absolute"
                                    }
                                ],
                                "paddingAll": "0px"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "image",
                                        "url": "https://imgur.com/67ULtT9.png",
                                        "aspectMode": "cover",
                                        "position": "absolute",
                                        "size": "full",
                                        "offsetBottom": "-15px"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "horizontal",
                                        "contents": [
                                            {
                                                "type": "box",
                                                "layout": "horizontal",
                                                "contents": [
                                                    {
                                                        "type": "text",
                                                        "text": "白金轉蛋 (機率"+str(COL_Probability/10)+"%十抽)",
                                                        "gravity": "bottom",
                                                        "align": "center",
                                                        "weight": "bold",
                                                        "size": "lg",
                                                        "color": "#999018"
                                                    }
                                                ],
                                                "paddingTop": "20px",
                                                "paddingBottom": "20px"
                                            }
                                        ],
                                        "backgroundColor": "#ffffffcc"
                                    },
                                    {
                                        "type": "separator"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "horizontal",
                                        "contents": [
                                            {
                                                "type": "box",
                                                "layout": "horizontal",
                                                "contents": [
                                                    {
                                                        "type": "image",
                                                        "url": "https://i.imgur.com/u94s9So.png"
                                                    },
                                                    {
                                                        "type": "text",
                                                        "text": "x"+str(COL),
                                                        "gravity": "center",
                                                        "align": "start",
                                                        "offsetStart": "3px"
                                                    }
                                                ],
                                                "paddingAll": "20px"
                                            },
                                            {
                                                "type": "box",
                                                "layout": "horizontal",
                                                "contents": [
                                                    {
                                                        "type": "image",
                                                        "url": "https://imgur.com/pHfHyhV.png",
                                                        "size": "xxs"
                                                    },
                                                    {
                                                        "type": "text",
                                                        "text": "x"+str(GOL),
                                                        "gravity": "center",
                                                        "align": "start",
                                                        "offsetStart": "3px"
                                                    }
                                                ],
                                                "paddingAll": "20px"
                                            },
                                            {
                                                "type": "box",
                                                "layout": "horizontal",
                                                "contents": [
                                                    {
                                                        "type": "image",
                                                        "url": "https://imgur.com/D9mJZp3.png",
                                                        "size": "xxs"
                                                    },
                                                    {
                                                        "type": "text",
                                                        "text": "x"+str(SLI),
                                                        "gravity": "center",
                                                        "align": "start",
                                                        "offsetStart": "3px"
                                                    }
                                                ],
                                                "paddingAll": "20px"
                                            }
                                        ],
                                        "backgroundColor": "#ffffffcc"
                                    },
                                    {
                                        "type": "separator"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "horizontal",
                                        "contents": [
                                            {
                                                "type": "box",
                                                "layout": "horizontal",
                                                "contents": [
                                                    {
                                                        "type": "image",
                                                        "url": "https://i.Imgur.com/NJ36MhA.png",
                                                        "size": "xxs",
                                                        "align": "end",
                                                        "offsetEnd": "3px"
                                                    },
                                                    {
                                                        "type": "text",
                                                        "text": "x"+str(COL*50+GOL*10+SLI*1),
                                                        "gravity": "center",
                                                        "align": "start",
                                                        "offsetStart": "3px"
                                                    }
                                                ],
                                                "paddingTop": "20px",
                                                "paddingBottom": "20px"
                                            }
                                        ],
                                        "backgroundColor": "#ffffffcc"
                                    }
                                ]
                            }
                        ],
                        "paddingAll": "0px"
                    }
                }
            ]
        }
    )
    return flex_message