#============================================================
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *
from FlexMessage import *
#============================================================

def Anime_Link(i,input_message):
    if '工作細胞' in input_message:
        message = '☆工作細胞☆ 動畫連結\n\nb站：\nhttps://www.bilibili.com/bangumi/media/md102392 \n\n巴哈(港澳台專用)：\n\nhttps://ani.gamer.com.tw/animeVideo.php?sn=10210 \n\nAbema生肉(需使用VPN)：\nhttps://abema.tv/video/title/26-53'
    elif '鬼滅' in input_message:
        message = '☆鬼滅之刃☆ 動畫連結\n\nb站(僅限台灣)：\nhttps://www.bilibili.com/bangumi/media/md25832466 \n\n巴哈(港澳台專用)：\n\nhttps://ani.gamer.com.tw/animeVideo.php?sn=12083 \n\nAbema生肉(需使用VPN)：\nhttps://abema.tv/video/title/26-75'
    elif '公主連結' in input_message or '公連' in input_message :
        message = '☆公主連結☆ 動畫連結\n\nb站(港澳台專用)：\nhttps://www.bilibili.com/bangumi/play/ss33095 \n\nAbema生肉(需使用VPN)：\nhttps://abema.tv/video/title/512-2'
    elif 're0' in input_message or 'Re:從零開始的異世界生活' in input_message or '雷姆' in input_message or 'Re0' in input_message or 'Re:0' in input_message:
        message = '☆Re:從零開始的異世界生活☆ 動畫連結\n\nb站(港澳台專用)：\nhttps://www.bilibili.com/bangumi/media/md3461 \n\n巴哈(港澳台專用)\n第一季：\nhttps://ani.gamer.com.tw/animeVideo.php?sn=14440 \n第二季：\nhttps://ani.gamer.com.tw/animeVideo.php?sn=16344 \n\nAbema生肉(需使用VPN)\n第一季：\nhttps://abema.tv/video/title/25-139 \n第二季：\nhttps://abema.tv/video/title/25-148'
    elif '輝夜姬' in input_message or  '輝夜' in input_message or '輝夜姬想讓人告白～天才們的戀愛頭腦戰～'  in input_message or  '輝夜姬想讓人告白' in input_message or  '天才們的戀愛頭腦戰動畫' in input_message:
        message = '☆輝夜姬想讓人告白～天才們的戀愛頭腦戰～☆ 動畫連結\n\nb站(港澳台專用)：\nhttps://www.bilibili.com/bangumi/media/md5267730 \n\n巴哈(港澳台專用)\n第一季：\nhttps://ani.gamer.com.tw/animeVideo.php?sn=11431 \n第二季：\nhttps://ani.gamer.com.tw/animeVideo.php?sn=15298 \n\nAbema生肉(需使用VPN)\n第一季：\nhttps://abema.tv/video/title/26-66 \n第二季：\nhttps://abema.tv/video/title/26-96 '

#====================================
    elif '作品' in input_message:    
        message = '不不不!!你搞錯了\n假設你要看re0動畫\n輸入: #動畫 re0\n即可~~'
    return message
#====================================
def Anime_Preview(i,input_message):
    if '工作細胞' in input_message:
        message = ImageSendMessage(original_content_url = "https://i.imgur.com/d3oRiU7.jpg",preview_image_url = "https://i.imgur.com/d3oRiU7.jpg")
    elif '鬼滅' in input_message:
        if(i%3==1):
            message = ImageSendMessage(original_content_url = "https://i.imgur.com/11plqZW.jpg",preview_image_url = "https://i.imgur.com/11plqZW.jpg")
        elif(i%3==2):
            message = ImageSendMessage(original_content_url = "https://i.imgur.com/eKSycQi.jpg",preview_image_url = "https://i.imgur.com/eKSycQi.jpg")
        elif(i%3==0):
            message = ImageSendMessage(original_content_url = "https://i.imgur.com/xGQLQ6c.jpg",preview_image_url = "https://i.imgur.com/xGQLQ6c.jpg")
    elif '公主連結' in input_message or '公連' in input_message :
        if(i%7==1):
            message = ImageSendMessage(original_content_url = "https://i.imgur.com/IulcU1a.jpg",preview_image_url = "https://i.imgur.com/IulcU1a.jpg")
        elif(i%7==2):
            message = ImageSendMessage(original_content_url = "https://i.imgur.com/CksvDjN.jpg",preview_image_url = "https://i.imgur.com/CksvDjN.jpg")
        elif(i%7==3):
            message = ImageSendMessage(original_content_url = "https://i.imgur.com/FLSUOjR.jpg",preview_image_url = "https://i.imgur.com/FLSUOjR.jpg")
        elif(i%7==4):
            message = ImageSendMessage(original_content_url = "https://i.imgur.com/FYblE8E.jpg",preview_image_url = "https://i.imgur.com/FYblE8E.jpg")
        elif(i%7==5):
            message = ImageSendMessage(original_content_url = "https://i.imgur.com/gxMQkHy.jpg",preview_image_url = "https://i.imgur.com/gxMQkHy.jpg")
        elif(i%7==6):
            message = ImageSendMessage(original_content_url = "https://i.imgur.com/sBYyPxS.jpg",preview_image_url = "https://i.imgur.com/sBYyPxS.jpg")
        elif(i%7==0):
            message = ImageSendMessage(original_content_url = "https://i.imgur.com/dqDTLAH.jpg",preview_image_url = "https://i.imgur.com/dqDTLAH.jpg")
    elif 're0' in input_message or 'Re:從零開始的異世界生活' in input_message or '雷姆' in input_message or 'Re0' in input_message or 'Re:0' in input_message:
        if(i%4==1):
            message = ImageSendMessage(original_content_url = "https://i.imgur.com/dy5SWPI.jpg",preview_image_url = "https://i.imgur.com/dy5SWPI.jpg")
        elif(i%4==2):
            message = ImageSendMessage(original_content_url = "https://i.imgur.com/fVkLdJV.jpg",preview_image_url = "https://i.imgur.com/fVkLdJV.jpg")
        elif(i%4==3):
            message = ImageSendMessage(original_content_url = "https://i.imgur.com/rQVZCGT.jpg",preview_image_url = "https://i.imgur.com/rQVZCGT.jpg")
        elif(i%4==0):
            message = ImageSendMessage(original_content_url = "https://i.imgur.com/WSzx0X4.jpg",preview_image_url = "https://i.imgur.com/WSzx0X4.jpg")
    elif '輝夜' in input_message:
        if(i%3==1):
            message = ImageSendMessage(original_content_url = "https://i.imgur.com/ZS7xDXG.jpg",preview_image_url = "https://i.imgur.com/ZS7xDXG.jpg")
        elif(i%3==2):
            message = ImageSendMessage(original_content_url = "https://i.imgur.com/4Ntx0Rw.jpg",preview_image_url = "https://i.imgur.com/4Ntx0Rw.jpg")
        elif(i%3==0):
            message = ImageSendMessage(original_content_url = "https://i.imgur.com/oiyKEI8.jpg",preview_image_url = "https://i.imgur.com/oiyKEI8.jpg")
#===================================
    return message
#===================================


def Anime_View(input_message):
    if '工作細胞' in input_message:
        return Anime_Return(
            'https://ani.gamer.com.tw/animeVideo.php?sn=10210',
            'https://www.bilibili.com/bangumi/media/md102392',
            'https://abema.tv/video/title/26-53',
            '工作細胞',
            'https://imgur.com/kPBFaz2',
            'https://i.imgur.com/d3oRiU7.jpg',
            'https://imgur.com/LbQJcj9'
        )