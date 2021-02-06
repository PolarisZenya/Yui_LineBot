
# 運算終端插件

#============================================================
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *
#============================================================

# quick reply 快速選取套件
def QuickClick_Log (event):
    #那個event.type是為了follow event所設置
    if(event.source.type != "group" or event.type == "follow"):
        quick_reply = QuickReply (
            items=[
                QuickReplyButton(
                    image_url='https://i.imgur.com/D4q9mgi.jpg',
                    action=MessageAction(
                        label="公連角色", 
                        text="#求圖",
                    )
                ),
                QuickReplyButton(
                    image_url='https://i.imgur.com/4YSb0vJ.jpg',
                    action=MessageAction(
                        label="公連動畫", 
                        text="#動畫 公連",
                    )
                ),
                QuickReplyButton(
                    image_url='https://i.imgur.com/RWCDXFk.jpg',
                    action=MessageAction(
                        label="公主祭十抽", 
                        text="#抽 公主祭",
                    )
                ),
                QuickReplyButton(
                    image_url='https://i.imgur.com/3Rh5gp6.jpg',
                    action=MessageAction(
                        label="作者巴哈", 
                        text="#問題回報",
                    )
                ),
                QuickReplyButton(
                    image_url='https://i.imgur.com/UnnR15e.jpg',
                    action=MessageAction(
                        label="私訊作者大大", 
                        text="#許願",
                    )
                ),
                QuickReplyButton(
                    image_url='https://i.imgur.com/dyGIpOL.jpg',
                    action=MessageAction(
                        label="更改優衣回覆", 
                        text="#權限",
                    )
                ),
                QuickReplyButton(
                    image_url='https://i.imgur.com/Jm3RYa6.jpg',
                    action=MessageAction(
                        label="N網隨機本本", 
                        text="n0",
                    )
                ),
                QuickReplyButton(
                    image_url='https://i.imgur.com/c8McovH.jpg',
                    action=MessageAction(
                        label="W網隨機本本", 
                        text="w0",
                    )
                ),
                QuickReplyButton(
                    image_url='https://i.imgur.com/t0sAiNh.png',
                    action=MessageAction(
                        label="18comic隨機本本", 
                        text="18c0",
                    )
                )
            ]
        )
        return quick_reply
    else:
        return 
# 抽卡系統的quick reply
def QuickClick_Capsule (event):
    if(event.source.type != "group"):
        quick_reply = QuickReply (
            items=[
                QuickReplyButton(
                    action=MessageAction(
                        label="常駐池", 
                        text="#抽 常駐",
                    )
                ),
                QuickReplyButton(
                    action=MessageAction(
                        label="公主祭", 
                        text="#抽 公主祭",
                    )
                ),
                QuickReplyButton(
                    action=MessageAction(
                        label="泳裝池", 
                        text="#抽 泳裝",
                    )
                ),
                QuickReplyButton(
                    action=MessageAction(
                        label="新年池", 
                        text="#抽 新年",
                    )
                ),
                QuickReplyButton(
                    action=MessageAction(
                        label="情人節", 
                        text="#抽 情人節",
                    )
                ),
                QuickReplyButton(
                    action=MessageAction(
                        label="萬聖節", 
                        text="#抽 萬聖節",
                    )
                ),
                QuickReplyButton(
                    action=MessageAction(
                        label="聖誕節", 
                        text="#抽 聖誕節",
                    )
                ),
                QuickReplyButton(
                    action=MessageAction(
                        label="奇幻夢境", 
                        text="#抽 夢境",
                    )
                ),
                QuickReplyButton(
                    action=MessageAction(
                        label="偶大", 
                        text="#抽 偶像大師",
                    )
                ),
                QuickReplyButton(
                    action=MessageAction(
                        label="天使池", 
                        text="#抽 天使",
                    )
                ),
                QuickReplyButton(
                    action=MessageAction(
                        label="Re:0池", 
                        text="#抽 re0",
                    )
                ),
                QuickReplyButton(
                    action=MessageAction(
                        label="我崩潰給我100%彩卡", 
                        text="#抽 大雜燴 自訂100%",
                    )
                )
            ]
        )
        return quick_reply

def QuickClick_Res_Hentai (event):
    if(event.source.type != "group"):
        quick_reply = QuickReply (
            items=[
                QuickReplyButton(
                    image_url='https://i.imgur.com/Jm3RYa6.jpg',
                    action=MessageAction(
                        label="更多N網隨機本本", 
                        text="n0",
                    )
                ),
                QuickReplyButton(
                    image_url='https://i.imgur.com/c8McovH.jpg',
                    action=MessageAction(
                        label="更多W網隨機本本", 
                        text="w0",
                    )
                ),
                QuickReplyButton(
                    image_url='https://i.imgur.com/t0sAiNh.png',
                    action=MessageAction(
                        label="更多18comic隨機本本", 
                        text="18c0",
                    )
                )
            ]
        )
        return quick_reply