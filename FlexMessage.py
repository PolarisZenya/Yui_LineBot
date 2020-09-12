#============================================================
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *
# linebbot_std made node json in python
#============================================================
from Quick_Reply import *
#============================================================
def Log(event):
    flex_message = FlexSendMessage(
        alt_text = "使用教學指令",
        quick_reply=QuickClick_Log(event),
        contents = {
            "type": "carousel",
            "contents": [
                {
                    "type": "bubble",
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "contents": [
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "#log功能集",
                                        "weight": "bold",
                                        "size": "xl",
                                        "color": "#2F8D5B"
                                    },
                                    {
                                        "type": "separator",
                                        "margin": "sm"
                                    }
                                ],
                                "offsetBottom": "10px"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "角色圖、梗圖...！",
                                        "weight": "bold",
                                        "size": "lg"
                                    },
                                    {
                                        "type": "text",
                                        "text": "角色圖庫多達1500+張(含繪師p站或推特)\n支援個角色名、綽號...等(但不支援錯字)\n像凱留可輸入：黑貓、接頭霸王、945...\n若沒想法又想看圖(可於主選單快速輸入)\n可輸入指令：#隨機 或是 #求圖",
                                        "color": "#A3A3A3",
                                        "size": "sm",
                                        "wrap": True
                                    },
                                    {
                                        "type": "separator",
                                        "margin": "sm"
                                    }
                                ],
                                "offsetBottom": "10px"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "橫跨歐非大陸的轉蛋機(新)",
                                        "weight": "bold",
                                        "size": "lg",
                                        "color": "#B70003"
                                    },
                                    {
                                        "type": "text",
                                        "color": "#A3A3A3",
                                        "size": "sm",
                                        "wrap": True,
                                        "text": "抽！就是抽爆！！管你歐洲天龍人還非洲酋長，更新加入的轉蛋機沉浸式體驗，可選擇卡池與機率，卡池更新至日服卡池\n指令：#抽 + 轉蛋池 + 自訂 + 機率(2.5%)\n例如輸入：#抽 公主祭、#抽 泳裝 加倍\n#抽 偶大 自訂 100%、#抽 大雜燴"
                                    },
                                    {
                                        "type": "separator",
                                        "margin": "sm"
                                    }
                                ],
                                "offsetBottom": "10px"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "動畫超連結指令(開發中)",
                                        "weight": "bold",
                                        "size": "lg"
                                    },
                                    {
                                        "type": "text",
                                        "color": "#A3A3A3",
                                        "size": "sm",
                                        "wrap": True,
                                        "text": "(未來可能會移除的測試性功能)\n目前提供以下3種正版通路\n巴哈姆特動漫瘋、bilibili、Abema\n輸入：#動畫 公連、#動畫 輝夜 第二季"
                                    }
                                ],
                                "offsetBottom": "10px"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "color": "#999B02bb",
                                        "size": "sm",
                                        "text": "特別感謝布丁機器人的生父-罕罕",
                                        "align": "center"
                                    }
                                ],
                                "position": "absolute",
                                "offsetBottom": "10px",
                                "paddingStart": "30px"
                            }
                        ]
                    }
                },
                {
                    "type": "bubble",
                    "hero": {
                        "type": "image",
                        "size": "full",
                        "aspectRatio": "20:13",
                        "aspectMode": "cover",
                        "url": "https://i.imgur.com/4RthLFT.png"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "contents": [
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "大量的隨機性",
                                        "weight": "bold",
                                        "size": "lg"
                                    },
                                    {
                                        "type": "text",
                                        "color": "#A3A3A3",
                                        "size": "sm",
                                        "wrap": True,
                                        "text": "強化了舊版的隨機功能，95%以上的行為都具隨機性，更大幅度降低罐頭文的出現率，並於此次更新加入更多隨機元素與降低彩蛋出現機率，希望各位大大玩得開心\n"
                                    },
                                    {
                                        "type": "separator",
                                        "margin": "sm"
                                    }
                                ],
                                "offsetBottom": "5px"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "聊天機器人(新 限非群組)",
                                        "weight": "bold",
                                        "size": "lg",
                                        "color": "#B70003"
                                    },
                                    {
                                        "type": "text",
                                        "color": "#A3A3A3",
                                        "size": "sm",
                                        "wrap": True,
                                        "text": "在單人聊天頻道加入聊天功能(算尬聊吧)\n目前聊天內容不算豐富約莫200種回覆與幾種狀態而已(可於後面的私作者功能提供加入優衣對話，我還會慢慢加入進去)"
                                    }
                                ],
                                "offsetBottom": "5px"
                            }
                        ]
                    }
                },
                {
                    "type": "bubble",
                    "hero": {
                        "type": "image",
                        "size": "full",
                        "aspectRatio": "20:13",
                        "aspectMode": "cover",
                        "url": "https://i.imgur.com/ToC8mDP.png"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "contents": [
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "私訊作者與許願(新 限非群組)",
                                        "weight": "bold",
                                        "size": "lg",
                                        "color": "#B70003"
                                    },
                                    {
                                        "type": "text",
                                        "color": "#A3A3A3",
                                        "size": "sm",
                                        "wrap": True,
                                        "text": "礙於我對於優衣實在還不太認識，如果想要優衣於聊天系統中回覆更奇特的詞或更多互動場景，又或者是對作者許願新功能(肝都爆光，實在沒點子了...)\n於單人聊天頻道可輸入：#許願、#建議\n(過程完全隱密，不過我沒辦法回覆你很抱歉，不過你們的每一封訊息我都會讀，Line機器人個別回覆的機制要$$...)"
                                    }
                                ],
                                "offsetBottom": "5px"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "color": "#B70003",
                                        "size": "sm",
                                        "text": "-傳過多無意義垃圾私訊會入黑單-",
                                        "align": "center"
                                    },
                                    {
                                        "type": "text",
                                        "color": "#999B02bb",
                                        "size": "sm",
                                        "text": "-notify功能不會加入，無法回覆-",
                                        "align": "center"
                                    }
                                ],
                                "offsetTop": "15px"
                            }
                        ]
                    }
                },
                {
                    "type": "bubble",
                    "hero": {
                        "type": "image",
                        "size": "full",
                        "aspectRatio": "20:13",
                        "aspectMode": "cover",
                        "url": "https://i.imgur.com/cAxJIOA.png"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "contents": [
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "優衣暫不提供情報...",
                                        "weight": "bold",
                                        "size": "lg"
                                    },
                                    {
                                        "type": "text",
                                        "color": "#A3A3A3",
                                        "size": "sm",
                                        "wrap": True,
                                        "text": "情報方面還是推薦各位使用前輩們開發的布丁、可可蘿機器人 (十分實用~~~)"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "horizontal",
                                        "contents": [
                                            {
                                                "type": "image",
                                                "url": "https://i.imgur.com/wdy7Sv2.png",
                                                "size": "sm",
                                                "action": {
                                                    "type": "uri",
                                                    "label": "action",
                                                    "uri": "https://forum.gamer.com.tw/C.php?bsn=30861&snA=13556"
                                                }
                                            },
                                            {
                                                "type": "image",
                                                "url": "https://i.imgur.com/33OaH0u.png",
                                                "size": "sm",
                                                "action": {
                                                    "type": "uri",
                                                    "label": "action",
                                                    "uri": "https://forum.gamer.com.tw/C.php?bsn=30861&snA=12791"
                                                }
                                            }
                                        ],
                                        "paddingTop": "5px",
                                        "paddingBottom": "5px"
                                    }
                                ],
                                "offsetBottom": "5px"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "separator",
                                        "margin": "sm"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "順便推廣個自家臉書社團",
                                                "weight": "bold",
                                                "size": "lg"
                                            }
                                        ],
                                        "paddingTop": "10px"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "color": "#A3A3A3",
                                                "size": "sm",
                                                "wrap": True,
                                                "align": "center",
                                                "text": "我...一個不起眼的小管管"
                                            },
                                            {
                                                "type": "text",
                                                "color": "#5C88DA",
                                                "size": "sm",
                                                "text": "超異域公主連結✩Re:Dive交流區",
                                                "weight": "bold",
                                                "align": "center",
                                                "action": {
                                                    "type": "uri",
                                                    "label": "action",
                                                    "uri": "https://www.facebook.com/groups/2090300834327237"
                                                }
                                            }
                                        ],
                                        "paddingTop": "10px"
                                    }
                                ],
                                "offsetBottom": "5px"
                            }
                        ]
                    }
                },
                {
                    "type": "bubble",
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "contents": [
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "老司機飆起來！！",
                                        "weight": "bold",
                                        "size": "xl",
                                        "color": "#2F8D5B"
                                    },
                                    {
                                        "type": "separator",
                                        "margin": "sm"
                                    }
                                ],
                                "offsetBottom": "10px"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "這才是人家創機器人的初心",
                                        "weight": "bold",
                                        "size": "lg"
                                    },
                                    {
                                        "type": "text",
                                        "text": "沒錯，你沒看錯！！(機動激動)\n冒著前幾個機器人都被Line封鎖的風險",
                                        "color": "#A3A3A3",
                                        "size": "sm",
                                        "wrap": True
                                    },
                                    {
                                        "type": "text",
                                        "text": "我就發車、發色圖，拿我怎樣！(沒",
                                        "color": "#A3A3A3",
                                        "size": "sm",
                                        "wrap": True,
                                        "weight": "bold"
                                    },
                                    {
                                        "type": "separator",
                                        "margin": "sm"
                                    }
                                ],
                                "offsetBottom": "10px"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "快速發車器",
                                        "weight": "bold",
                                        "size": "lg"
                                    },
                                    {
                                        "type": "text",
                                        "color": "#A3A3A3",
                                        "size": "sm",
                                        "wrap": True,
                                        "text": "目前支援n網&w網，e&ex網(開發中)\n有新設新版的防呆偵錯功能，不用擔心會傳404 not found的連結(sry了真步bot)\n使用很簡單，直接輸入想要網站加上車號\n亦可於英文字後加入0會發送隨機本本\n例：n320580，w102180，n0，w0\n車子將於1秒內抵達官邸"
                                    },
                                    {
                                        "type": "separator",
                                        "margin": "sm"
                                    }
                                ],
                                "offsetBottom": "10px"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "版本更新 v.2020.09.12",
                                        "weight": "bold",
                                        "size": "lg"
                                    },
                                    {
                                        "type": "text",
                                        "color": "#A3A3A3",
                                        "size": "sm",
                                        "wrap": True,
                                        "text": "#加入了快速回覆選項\n#加入了轉蛋系統\n#所有遊戲連動與活動角色均加入圖庫\n#大幅度降低了所有彩蛋的出現機率\n#w網發車功能美術修改至如n網，速度+\n#修復了一些會導致機器人崩壞的bug"
                                    }
                                ],
                                "offsetBottom": "10px"
                            }
                        ]
                    }
                }
            ]
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
def Hentai_Path_N_except(Action_but,
                URL,
                PicURL,
                Title,
                Num
    ):
    flex_message = FlexSendMessage(
        alt_text = ('n網現正發車中~~'),
#        quick_reply=QuickClick(),
        contents = {
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
    )
    return flex_message

def Hentai_Path_N(Action_but,
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


# 新版w網發車
def Hentai_Path_W(
    Action_but,
    url,
    Title,
    num,
    PicURL_0,
    PicURL_1
):
    flex_message = FlexSendMessage(
        alt_text = 'w網現正發車中~~',
#        quick_reply=QuickClick(),
        contents = {
            "type": "bubble",
            "size": "giga",
            "body": {
                "type": "box",
                "layout": "vertical",
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
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "image",
                                                "url": PicURL_0,
                                                "size": "4xl",
                                                "aspectRatio": "2:3",
                                                "aspectMode": "cover",
                                                "gravity": "top",
                                                "align": "start"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "image",
                                                "url": PicURL_1,
                                                "size": "4xl",
                                                "aspectRatio": "2:3",
                                                "aspectMode": "cover",
                                                "gravity": "top",
                                                "align": "start"
                                            }
                                        ],
                                        "paddingStart": "10px"
                                    }
                                ],
                                "backgroundColor": "#1C4C58cc",
                                "paddingTop": "10px",
                                "paddingStart": "10px",
                                "paddingEnd": "10px",
                                "paddingBottom": "5px"
                            }
                        ]
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
                                        "text": "w"+num,
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
                                "borderWidth": "3px",
                                "cornerRadius": "4px",
                                "spacing": "sm",
                                "borderColor": "#1C4C58",
                                "margin": "xxl",
                                "height": "40px",
                                "action": {
                                    "type": "uri",
                                    "label": "action",
                                    "uri": url
                                }
                            }
                        ],
                        "position": "relative",
                        "offsetBottom": "0px",
                        "offsetStart": "0px",
                        "offsetEnd": "0px",
                        "backgroundColor": "#eeeeeedd",
                        "paddingAll": "20px",
                        "paddingTop": "18px",
                        "borderColor": "#1C4C58cc",
                        "borderWidth": "3px"
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
                "paddingAll": "0px",
                "backgroundColor": "#91AAA9"
            }
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
        COL_Probability,
        NAME,
        event
    ):
    flex_message = FlexSendMessage(
        alt_text = '母珠石呷飽飽',
        quick_reply = QuickClick_Capsule(event),
        contents = {
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
                                "url": "https://i.imgur.com/67ULtT9.png",
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
                                                "text": NAME + " (機率"+str(COL_Probability/10)+"%十抽)",
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
                                                "url": "https://i.imgur.com/pHfHyhV.png",
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
                                                "url": "https://i.imgur.com/D9mJZp3.png",
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
    )
    return flex_message
