#============================================================
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *
from FlexMessage import *
#============================================================

def Anime_Link(i,input_message):
    if 're0' in input_message or 'Re:從零開始的異世界生活' in input_message or '雷姆' in input_message or 'Re0' in input_message or 'Re:0' in input_message:
        message = '☆Re:從零開始的異世界生活☆ 動畫連結\n\nb站(港澳台專用)：\nhttps://www.bilibili.com/bangumi/media/md3461 \n\n巴哈(港澳台專用)\n第一季：\nhttps://ani.gamer.com.tw/animeVideo.php?sn=14440 \n第二季：\nhttps://ani.gamer.com.tw/animeVideo.php?sn=16344 \n\nAbema生肉(需使用VPN)\n第一季：\nhttps://abema.tv/video/title/25-139 \n第二季：\nhttps://abema.tv/video/title/25-148'
    elif '輝夜姬' in input_message or  '輝夜' in input_message or '輝夜姬想讓人告白～天才們的戀愛頭腦戰～'  in input_message or  '輝夜姬想讓人告白' in input_message or  '天才們的戀愛頭腦戰動畫' in input_message:
        message = '☆輝夜姬想讓人告白～天才們的戀愛頭腦戰～☆ 動畫連結\n\nb站(港澳台專用)：\nhttps://www.bilibili.com/bangumi/media/md5267730 \n\n巴哈(港澳台專用)\n第一季：\nhttps://ani.gamer.com.tw/animeVideo.php?sn=11431 \n第二季：\nhttps://ani.gamer.com.tw/animeVideo.php?sn=15298 \n\nAbema生肉(需使用VPN)\n第一季：\nhttps://abema.tv/video/title/26-66 \n第二季：\nhttps://abema.tv/video/title/26-96 '

#====================================
    elif '作品' in input_message:    
        message = '不不不!!你搞錯了\n假設你要看re0動畫\n輸入: #動畫 re0\n即可~~'
    return message
#====================================
def Anime_Preview(i,input_message):
    if '輝夜' in input_message:
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
        return Anime_Return_abc(
            'https://ani.gamer.com.tw/animeVideo.php?sn=10210',
            'https://www.bilibili.com/bangumi/media/md102392',
            'https://abema.tv/video/title/26-53',
            '工作細胞',
            'https://i.imgur.com/kPBFaz2.jpg',
            'https://i.imgur.com/d3oRiU7.jpg',
            'https://i.imgur.com/LbQJcj9.jpg'
        )
    elif '鬼滅' in input_message:
        return Anime_Return_abc(
            'https://ani.gamer.com.tw/animeVideo.php?sn=12083',
            'https://www.bilibili.com/bangumi/media/md25832466',
            'https://abema.tv/video/title/26-75',
            '鬼滅之刃',
            'https://i.imgur.com/Dk1Q6WI.jpg',
            'https://i.imgur.com/xGQLQ6c.jpg',
            'https://i.imgur.com/11plqZW.jpg'
        )
    elif '公連' in input_message or '公主連結' in input_message:
        return Anime_Return_bc(
            'https://www.bilibili.com/bangumi/play/ss33095',
            'https://abema.tv/video/title/512-2',
            '超異域公主連結',
            'https://i.imgur.com/dqDTLAH.jpg',
            'https://i.imgur.com/B9lRrbU.jpg'
        )
    elif ('re0' in input_message or 'Re0' in input_message or 'Re:0' in input_message) and '第二季' in input_message:
        return Anime_Return_abc(
            'https://ani.gamer.com.tw/animeVideo.php?sn=16344',
            'https://www.bilibili.com/bangumi/media/md3461',
            'https://abema.tv/video/title/25-148',
            'Re:Zero 第二季',
            'https://i.imgur.com/dy5SWPI.jpg',
            'https://i.imgur.com/am5ZzK5.jpg',
            'https://i.imgur.com/TJ53X4g.jpg'
        )