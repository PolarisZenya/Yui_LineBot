#============================================================
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *
#============================================================
from FlexMessage import *
from Quick_Reply import *
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
def ImageMessageURL (pic_url):
    message = ImageSendMessage(original_content_url = pic_url,preview_image_url = pic_url) 
    return message

def VideoMessageURL (vid_url):
    message = VideoSendMessage(original_content_url= vid_url+".mp4",preview_image_url= vid_url+".jpg")
    return message

def TextMess (text_mess):
    message = TextSendMessage(text = text_mess)
    return message

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
    elif '刀劍' in input_message and ('第三季' in input_message or '愛麗絲' in input_message or  'Alicization' in input_message):
        return Anime_Return_abc(
            'https://ani.gamer.com.tw/animeVideo.php?sn=10849',
            'https://www.bilibili.com/bangumi/media/md130412',
            'https://abema.tv/video/title/25-102',
            '刀劍神域 Alicization',
            'https://i.imgur.com/xj57J8N.jpg',
            'https://i.imgur.com/kyNw323.jpg',
            'https://i.imgur.com/pTXo6wf.jpg'
        )
    elif '刀劍' in input_message and ('第二季' in input_message  or  '幽靈子彈' in input_message or 'Phantom Bullet' in input_message):
        return Anime_Return_ac(
            'https://ani.gamer.com.tw/animeVideo.php?sn=903',
            'https://abema.tv/video/title/25-31rtb-j-u-pk',
            '刀劍神域Phantom Bullet',
            'https://i.imgur.com/BqbaDh4.jpg',
            'https://i.imgur.com/mcmCLLL.jpg'
        )
    elif '刀劍' in input_message:
        return Anime_Return_abc(
            'https://ani.gamer.com.tw/animeVideo.php?sn=926',
            'https://www.bilibili.com/bangumi/media/md24755609',
            'https://abema.tv/video/title/25-1nzan-whrxe',
            '刀劍神域SwordArtOnline',
            'https://i.imgur.com/yxOdYQ2.jpg',
            'https://i.imgur.com/Fwz01xQ.png',
            'https://i.imgur.com/avHcju5.jpg'
        )
    elif '魔女之旅' in input_message:
        return Anime_Return_abc(
            'https://ani.gamer.com.tw/animeVideo.php?sn=18427',
            'https://www.bilibili.com/bangumi/media/md28229881',
            'https://abema.tv/video/title/174-18',
            '魔女の旅々',
            'https://i.imgur.com/CTN6KHK.jpg',
            'https://i.imgur.com/pLHyvB3.png',
            'https://i.imgur.com/zj50nOb.jpg'
        )

def Manga_Reply(input_message,i):
    value_i = [
        "https://i.imgur.com/6PM2XXF.png","https://i.imgur.com/ow4jBAI.png","https://i.imgur.com/ftYK35I.png","https://i.imgur.com/okPm6Ah.png",
        "https://i.imgur.com/vBrIw6D.png","https://i.imgur.com/IROtp3U.png","https://i.imgur.com/0YIRaEl.png","https://i.imgur.com/MqWbJcr.png",
        "https://i.imgur.com/mJd0seZ.png","https://i.imgur.com/Ri97JdE.png","https://i.imgur.com/9jrsP2Z.png","https://i.imgur.com/NhqS7c5.png",
        "https://i.imgur.com/bv40ZtG.png","https://i.imgur.com/Gq1jDwr.png","https://i.imgur.com/tTv8Fey.png","https://i.imgur.com/OthX2cL.png",
        "https://i.imgur.com/9AWRLyZ.png","https://i.imgur.com/2SeFzJ4.png","https://i.imgur.com/wdEnu7V.png","https://i.imgur.com/iDGS0Fc.png",
        "https://i.imgur.com/0NgE16W.png","https://i.imgur.com/VVzPkHA.png","https://i.imgur.com/O4BBMug.png","https://i.imgur.com/aiyDODv.png",
        "https://i.imgur.com/AOjW6mj.png","https://i.imgur.com/hFlEhsQ.png","https://i.imgur.com/m6sMMo5.png","https://i.imgur.com/O0prldN.png",
        "https://i.imgur.com/gAwONny.png","https://i.imgur.com/E5rw3rs.png","https://i.imgur.com/UODkcB8.png","https://i.imgur.com/SvSH2pf.png", # 32
        "https://i.imgur.com/INkkWN8.png","https://i.imgur.com/2IsCgjO.png","https://i.imgur.com/rxbXIAo.png","https://i.imgur.com/tGgLSLZ.png",
        "https://i.imgur.com/Jv3cdHg.png","https://i.imgur.com/LG29Yvu.png","https://i.imgur.com/Q85C47Z.png","https://i.imgur.com/oRi7MeR.png",
        "https://i.imgur.com/GxE2wic.png","https://i.imgur.com/FXBb90A.png","https://i.imgur.com/enmanMM.png","https://i.imgur.com/PYCR89Z.png",
        "https://i.imgur.com/ZN88884.png","https://i.imgur.com/jfAQ4Fz.png","https://i.imgur.com/91Z4jqx.png","https://i.imgur.com/c7rFguu.png",
        "https://i.imgur.com/HiiTwb4.png","https://i.imgur.com/IPEwP7c.png","https://i.imgur.com/1kyhD1o.png","https://i.imgur.com/TAOnGTC.png",
        "https://i.imgur.com/E73zGIA.png","https://i.imgur.com/SJhLu1r.png","https://i.imgur.com/FVlUIOF.png","https://i.imgur.com/3PcsbCB.png",
        "https://i.imgur.com/aGUSmCl.png","https://i.imgur.com/k2X9iRu.png","https://i.imgur.com/kOwsu5C.png","https://i.imgur.com/ik9iBoF.png",
        "https://i.imgur.com/7tjhlEb.png","https://i.imgur.com/ZFeu3KK.png","https://i.imgur.com/24FJiPf.png","https://i.imgur.com/optHyMD.png", # 64
        "https://i.imgur.com/3eK8RnZ.png","https://i.imgur.com/S8Kbgxt.png","https://i.imgur.com/zy5Ly4G.png","https://i.imgur.com/HJ8ruAs.png",
        "https://i.imgur.com/FwLKnR5.png","https://i.imgur.com/1f8owmJ.png","https://i.imgur.com/qAtQHEM.png","https://i.imgur.com/0ovG7rv.png",
        "https://i.imgur.com/H82DAUp.png","https://i.imgur.com/o8HRvYr.png","https://i.imgur.com/KdRmRH2.png","https://i.imgur.com/XdgB37m.png",
        "https://i.imgur.com/mgUakB4.png","https://i.imgur.com/X6DobFl.png","https://i.imgur.com/q29GBPf.png","https://i.imgur.com/2I8Gwjl.png",
        "https://i.imgur.com/uxqPjTC.png","https://i.imgur.com/CZk2Zxm.png","https://i.imgur.com/cvmFsLZ.png","https://i.imgur.com/AVURmQT.png",
        "https://i.imgur.com/MYsFwWt.png","https://i.imgur.com/3CVJMM2.png","https://i.imgur.com/tekiWQL.png","https://i.imgur.com/kytSjbo.png",
        "https://i.imgur.com/Yh1VJ0q.png","https://i.imgur.com/xQ1hfkf.png","https://i.imgur.com/Ys5j65p.png","https://i.imgur.com/nuUrKSx.png",
        "https://i.imgur.com/qCFnJcy.png","https://i.imgur.com/OIttIkq.png","https://i.imgur.com/guKzYCs.png","https://i.imgur.com/d8DOwr3.png", # 96
        "https://i.imgur.com/5zR8Yce.png","https://i.imgur.com/rdyg3QY.png","https://i.imgur.com/53HphlM.png","https://i.imgur.com/O8xPjMc.png",
        "https://i.imgur.com/wlWqevO.png","https://i.imgur.com/nMtoulr.png","https://i.imgur.com/pGfXpur.png","https://i.imgur.com/8fpyD8A.png",
        "https://i.imgur.com/jUUitAY.png","https://i.imgur.com/DzTNofO.png","https://i.imgur.com/Uf53CGz.png","https://i.imgur.com/B7LHiRH.png",
        "https://i.imgur.com/OD1lcFo.png","https://i.imgur.com/QVAQ088.png","https://i.imgur.com/bWWiCYe.png","https://i.imgur.com/sEqXkGQ.png",
        "https://i.imgur.com/lU7lUaT.png","https://i.imgur.com/Mo4cqsV.png","https://i.imgur.com/ffraXgA.png","https://i.imgur.com/7Ctuy3l.png",
        "https://i.imgur.com/88lP2aS.png","https://i.imgur.com/sS5Nd3V.png","https://i.imgur.com/n91Qj8d.png","https://i.imgur.com/jTuaK5N.png",
        "https://i.imgur.com/7UHsyFi.png","https://i.imgur.com/UL1P7ob.png","https://i.imgur.com/i92SP7Z.png","https://i.imgur.com/A7vQJfe.png",
        "https://i.imgur.com/02bepW0.png","https://i.imgur.com/C9zAu0W.png","https://i.imgur.com/tVruSzu.png","https://i.imgur.com/mskHG4A.png", # 128
        "https://i.imgur.com/7e1Edl0.png","https://i.imgur.com/aS0Hef1.png","https://i.imgur.com/eIKBFkq.png","https://i.imgur.com/pdVCtoE.png",
        "https://i.imgur.com/mwHI3ig.png","https://i.imgur.com/YuNbuRL.png","https://i.imgur.com/4tnqK6N.png","https://i.imgur.com/4gIHRrU.png",
        "https://i.imgur.com/YL1Y7bx.png","https://i.imgur.com/iSFNrTK.png","https://i.imgur.com/9GInsAm.png","https://i.imgur.com/grqtPbk.png",
        "https://i.imgur.com/UQ7zXfO.png","https://i.imgur.com/Q5qmThW.png","https://i.imgur.com/jQneyVU.png","https://i.imgur.com/kE45FEf.png",
        "https://i.imgur.com/x0DAjjQ.png","https://i.imgur.com/2BSZXFt.png","https://i.imgur.com/GmAARfd.png","https://i.imgur.com/AAbJQl4.png",
        "https://i.imgur.com/EvZ1kq1.png","https://i.imgur.com/1t47dve.png","https://i.imgur.com/HFgahaG.png","https://i.imgur.com/WxW98Xj.png",
        "https://i.imgur.com/W7vfJQA.png","https://i.imgur.com/cBkw6dO.png","https://i.imgur.com/STg1Q5i.png","https://i.imgur.com/AOhTkxQ.png", 
        "https://i.imgur.com/P7UV6vx.png","https://i.imgur.com/RRZJq4Y.png","https://i.imgur.com/KfYtEcy.png","https://i.imgur.com/ZOIj6Gy.png", # 160
        "https://i.imgur.com/1cj6Ptq.png","https://i.imgur.com/CSOE7SB.png","https://i.imgur.com/nNI00Ir.png","https://i.imgur.com/jmAWCyt.png",
        "https://i.imgur.com/vsxnP42.png","https://i.imgur.com/jU2oivP.png","https://i.imgur.com/eDBEcdt.png","https://i.imgur.com/GT3fCGk.png",
        "https://i.imgur.com/h64dtdP.png","https://i.imgur.com/eps7O8P.png","https://i.imgur.com/8uIqCXI.png","https://i.imgur.com/C3ZNd81.png",
        "https://i.imgur.com/61YvhyA.png","https://i.imgur.com/mAbxcoX.png","https://i.imgur.com/yXYtF2L.png","https://i.imgur.com/YtWVCKX.png",
        "https://i.imgur.com/n2LoxAg.png","https://i.imgur.com/GvExU6N.png","https://i.imgur.com/JxbdiLk.png","https://i.imgur.com/5jq69C2.png",
        "https://i.imgur.com/uMi9T8G.png","https://i.imgur.com/i6TWRWl.png","https://i.imgur.com/gxtna9k.png","https://i.imgur.com/5lTlKnw.png",
        "https://i.imgur.com/mANu7Di.png","https://i.imgur.com/oDovvDU.png","https://i.imgur.com/L0uGbmd.png","https://i.imgur.com/8vDQzbI.png",
        "https://i.imgur.com/pBRGUQq.png","https://i.imgur.com/eBm3FyP.png","https://i.imgur.com/K5Sup6A.png","https://i.imgur.com/nvkarUS.png", # 192
        "https://i.imgur.com/gjITkW8.png","https://i.imgur.com/1Pjg2zF.png","https://i.imgur.com/TN2Ktrs.png","https://i.imgur.com/n9RzcGa.png",
        "https://i.imgur.com/SPSG2zf.png","https://i.imgur.com/7zpqtQR.png","https://i.imgur.com/LPX9zdA.png","https://i.imgur.com/AEAGJp1.png",
        "https://i.imgur.com/JlsAmMW.png","https://i.imgur.com/7qgddSZ.png","https://i.imgur.com/Y04jqIx.png","https://i.imgur.com/5lAXNaI.png",
        "https://i.imgur.com/6EHIFnC.png","https://i.imgur.com/VJ7VuhS.png","https://i.imgur.com/PbHxMOi.png","https://i.imgur.com/zYDy6fW.png",
        "https://i.imgur.com/GpgaZXI.png","https://i.imgur.com/Ht0080H.png","https://i.imgur.com/WUVZYDf.png","https://i.imgur.com/7aU1qHO.png",
        "https://i.imgur.com/72ovrHN.png","https://i.imgur.com/eFo4XCv.png","https://i.imgur.com/tlptVxA.png","https://i.imgur.com/gOoeCVH.png",
        "https://i.imgur.com/r2hrqjn.png","https://i.imgur.com/q7fgWMH.png","https://i.imgur.com/wQLbUbc.png","https://i.imgur.com/UpBkqa9.png",
        "https://i.imgur.com/O3lb89t.png","https://i.imgur.com/7Ymn8MY.png","https://i.imgur.com/gvx1eGF.png","https://i.imgur.com/Hsah08O.png", # 224
        "https://i.imgur.com/dpWXViQ.png","https://i.imgur.com/vIrrET0.png","https://i.imgur.com/cWY5dQD.png","https://i.imgur.com/3Fm1KoU.png",
        "https://i.imgur.com/ZBZHyyR.png","https://i.imgur.com/kAyOfVl.png","https://i.imgur.com/e2h0L9F.png","https://i.imgur.com/veqnPUm.png",
        "https://i.imgur.com/yxIrV5d.png","https://i.imgur.com/dBlLiKQ.png","https://i.imgur.com/RKjId9Z.png","https://i.imgur.com/cp5GWIj.png",
        "https://i.imgur.com/43NPtGT.png","https://i.imgur.com/TjjXcRZ.png","https://i.imgur.com/9jtfagd.png","https://i.imgur.com/U5SB2tb.png",
        "https://i.imgur.com/ViBQAe3.png",
    ]
    if input_message == '#漫畫' or input_message == '#漫畫 隨機': 
        return value_i [i% len(value_i)]
    elif len(input_message) <= 7: 
        num =''.join([x for x in input_message if x.isdigit()])
        return value_i [eval(num)-1]