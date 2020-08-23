
# 運算終端插件

#============================================================
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *
#============================================================

#============================================================
# quick reply 快速選取套件
def QuickClick_Log (event):
    if(event.source.type != "group" or event.type == "follow"):
        quick_reply = QuickReply (
            items=[
                QuickReplyButton(
                    action=MessageAction(
                        label="公連角色", 
                        text="#求圖",
                    )
                ),
                QuickReplyButton(
                    action=MessageAction(
                        label="公連動畫", 
                        text="#動畫 公連",
                    )
                ),
                QuickReplyButton(
                    action=MessageAction(
                        label="公主祭十抽", 
                        text="#抽 公主祭",
                    )
                ),
                QuickReplyButton(
                    action=MessageAction(
                        label="N網隨機本本", 
                        text="n0",
                    )
                )
            ]
        )
        return quick_reply
    else:
        return 
# 抽卡系統的quick reply
def QuickClick_Capsule ():
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
                    label="我崩潰給我100%彩卡", 
                    text="#抽 大雜燴 自訂100%",
                )
            )
        ]
    )
    return quick_reply