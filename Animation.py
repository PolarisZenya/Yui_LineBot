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
    if input_message == '#動畫':
        return TextSendMessage(text ='不不不!!你搞錯了\n假設你要看re0動畫\n輸入: #動畫 re0\n即可~~')
    elif '工作細胞' in input_message:
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
            'https://i.imgur.com/kxEmnj3.jpg'
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
            'https://www.bilibili.com/bangumi/media/md28229233',
            'https://abema.tv/video/title/25-148',
            'Re:Zero 第二季',
            'https://i.imgur.com/dy5SWPI.jpg',
            'https://i.imgur.com/TJ53X4g.jpg',
            'https://i.imgur.com/am5ZzK5.jpg'
            
        )
    elif 're0' in input_message or 'Re0' in input_message or 'Re:0' in input_message:
        return Anime_Return_abc(
            'https://ani.gamer.com.tw/animeVideo.php?sn=14440',
            'https://www.bilibili.com/bangumi/media/md3461',
            'https://abema.tv/video/title/25-139',
            'Re:Zero 第一季',
            'https://i.imgur.com/fVkLdJV.jpg',
            'https://i.imgur.com/MawwrYS.jpg',
            'https://i.imgur.com/qSI1tmA.jpg'
        )
    elif '輝夜' in input_message and '第二季' in input_message:
        return Anime_Return_abc(
            'https://ani.gamer.com.tw/animeVideo.php?sn=15298',
            'https://www.bilibili.com/bangumi/media/md28228367',
            'https://abema.tv/video/title/26-96',
            '輝夜姬想讓人告白 第二季',
            'https://i.imgur.com/ZS7xDXG.jpg',
            'https://i.imgur.com/jTrXiqn.jpg',
            'https://i.imgur.com/oHO6Axn.jpg'
        )
    elif '輝夜' in input_message:
        return Anime_Return_abc(
            'https://ani.gamer.com.tw/animeVideo.php?sn=11431',
            'https://www.bilibili.com/bangumi/media/md5267730',
            'https://abema.tv/video/title/26-66',
            '輝夜姬想讓人告白 第一季',
            'https://i.imgur.com/4Ntx0Rw.jpg',
            'https://i.imgur.com/oiyKEI8.jpg',
            'https://i.imgur.com/XalMrNf.jpg'
        )
    elif '刀劍神域' in input_message and ('第三季' in input_message or '愛麗絲' in input_message or  'Alicization' in input_message):
        return Anime_Return_abc(
            'https://ani.gamer.com.tw/animeVideo.php?sn=10849',
            'https://www.bilibili.com/bangumi/media/md130412',
            'https://abema.tv/video/title/25-102',
            '刀劍神域 Alicization',
            'https://i.imgur.com/xj57J8N.jpg',
            'https://i.imgur.com/LraIlZB.jpg',
            'https://i.imgur.com/pTXo6wf.jpg'
        )
    elif '刀劍神域' in input_message and ('第二季' in input_message  or  '幽靈子彈' in input_message or 'Phantom Bullet' in input_message):
        return Anime_Return_ac(
            'https://ani.gamer.com.tw/animeVideo.php?sn=903',
            'https://abema.tv/video/title/25-31rtb-j-u-pk',
            '刀劍神域Phantom Bullet',
            'https://i.imgur.com/BqbaDh4.jpg',
            'https://i.imgur.com/mcmCLLL.jpg'
        )
    elif '刀劍神域' in input_message:
        return Anime_Return_abc(
            'https://ani.gamer.com.tw/animeVideo.php?sn=926',
            'https://www.bilibili.com/bangumi/media/md24755609',
            'https://abema.tv/video/title/25-1nzan-whrxe',
            '刀劍神域SwordArtOnline',
            'https://i.imgur.com/yxOdYQ2.jpg',
            'https://i.imgur.com/Fwz01xQ.png',
            'https://i.imgur.com/avHcju5.jpg'
        )