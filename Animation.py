#============================================================
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *
#============================================================
from FlexMessage import *
#============================================================
#   Anime_Return_abc(
#       url_baha,   巴哈連結-a
#       url_bili,   bili連結-b
#       url_abema,  Abema連結-c
#       anime_name, 
#       pic_baha,   巴哈預覽圖片-a
#       pic_bili,   bili預覽圖片-b
#       pic_abema   Abema預覽圖片-c
#    )
#============================================================
# 發送圖片訊息再簡化
def ImageMessageURL (pic_url):
    message = ImageSendMessage(original_content_url = pic_url,preview_image_url = pic_url)
    return message

# 動畫連結 import FlexMessage.py
def Anime_View(input_message):
    input_value = {
        '工作細胞' : Anime_Return_abc(
            'https://ani.gamer.com.tw/animeVideo.php?sn=10210',
            'https://www.bilibili.com/bangumi/media/md102392',
            'https://abema.tv/video/title/26-53',
            '工作細胞',
            'https://i.imgur.com/kPBFaz2.jpg',
            'https://i.imgur.com/d3oRiU7.jpg',
            'https://i.imgur.com/LbQJcj9.jpg'
        ),
        '鬼滅' or '鬼滅之刃' : Anime_Return_abc(
            'https://ani.gamer.com.tw/animeVideo.php?sn=12083',
            'https://www.bilibili.com/bangumi/media/md25832466',
            'https://abema.tv/video/title/26-75',
            '鬼滅之刃',
            'https://i.imgur.com/Dk1Q6WI.jpg',
            'https://i.imgur.com/xGQLQ6c.jpg',
            'https://i.imgur.com/kxEmnj3.jpg'
        ),
        '公連' or '公主連結' : Anime_Return_bc(
            'https://www.bilibili.com/bangumi/play/ss33095',
            'https://abema.tv/video/title/512-2',
            '超異域公主連結',
            'https://i.imgur.com/dqDTLAH.jpg',
            'https://i.imgur.com/B9lRrbU.jpg'
        ),
        're0' or 'Re0' or 'Re:0' : Anime_Return_abc(
            'https://ani.gamer.com.tw/animeVideo.php?sn=14440',
            'https://www.bilibili.com/bangumi/media/md3461',
            'https://abema.tv/video/title/25-139',
            'Re:Zero 第一季',
            'https://i.imgur.com/fVkLdJV.jpg',
            'https://i.imgur.com/rQVZCGT.jpg',
            'https://i.imgur.com/qSI1tmA.jpg'
        ),
        '輝夜' or '輝夜姬' : Anime_Return_abc(
            'https://ani.gamer.com.tw/animeVideo.php?sn=11431',
            'https://www.bilibili.com/bangumi/media/md5267730',
            'https://abema.tv/video/title/26-66',
            '輝夜姬想讓人告白 第一季',
            'https://i.imgur.com/4Ntx0Rw.jpg',
            'https://i.imgur.com/oiyKEI8.jpg',
            'https://i.imgur.com/XalMrNf.jpg'
        )
    }
    return input_value[input_message]

    
