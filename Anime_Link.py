#這個檔案的作用是：建立功能列表

#===============這些是LINE提供的功能套組，先用import叫出來=============
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *
#===============LINEAPI=============================================

#以下是本檔案的內容本文

#1.建立旋轉木馬訊息，名為function_list(未來可以叫出此函數來使用)
#function_list的括號內是設定此函數呼叫時需要給函數的參數有哪些

def Anime_Link(input_message):
    if '工作細胞' input_message:
        message = '☆工作細胞☆ 動畫連結\n\nb站：\nhttps://www.bilibili.com/bangumi/media/md102392 \n\n巴哈(港澳台專用)：\n\nhttps://ani.gamer.com.tw/animeVideo.php?sn=10210 \n\nAbema生肉(需使用VPN)：\nhttps://abema.tv/video/title/26-53'
        return message

def Anime_Preview(input_message):
    if '工作細胞' input_message:
        message = ImageSendMessage(original_content_url = "https://i.imgur.com/d3oRiU7.jpg",preview_image_url = "https://i.imgur.com/d3oRiU7.jpg")
        return message