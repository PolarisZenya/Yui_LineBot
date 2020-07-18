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
    anime_value = {
        '#動畫' or '作品' : TextSendMessage(text ='不不不!!你搞錯了\n假設你要看re0動畫\n輸入: #動畫 re0\n即可~~'),
        '工作細胞' in input_message : Anime_Return_abc(
                        'https://ani.gamer.com.tw/animeVideo.php?sn=10210',
                        'https://www.bilibili.com/bangumi/media/md102392',
                        'https://abema.tv/video/title/26-53',
                        '工作細胞',
                        'https://i.imgur.com/kPBFaz2.jpg',
                        'https://i.imgur.com/d3oRiU7.jpg',
                        'https://i.imgur.com/LbQJcj9.jpg'
                    )
    }
    return anime_value[input_message]