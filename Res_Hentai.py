
# 運算插件

#============================================================
from FlexMessage import *
import urllib.request as req
import bs4
#============================================================
from Animation import *
#============================================================
def getData_N(Action_but,num,event):
    """
        網頁爬蟲抓取資料存入並做出Flex Message

        目前功能為request上n網抓取資料 (w網未來考慮加入(w網js檔反爬蟲) 可能會利用selenium去抓

        並利用beautiful soup整理html.text代入FlexMessage組訊息
    """
    timer = 0
# b為取第二值用
    timer_b = 0
    site=[0]*5
    name=[0]*5
    picture=[0]*5
    number_N=[0]*5
# 使用者驗證，chrome升級後這裡驗證要重新去network/user-agent 抓 Chrome version
    request = req.Request("https://nhentai.net/g/"+str(num), headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
    soup = bs4.BeautifulSoup(data, "html.parser")
# 先做n網，w網js抓寫另一個def (此if可省略)
    if "» nhentai: hentai doujinshi and manga" in soup.title.string :
# bs4去整理request抓下之html，原如下
# <span class="before">[Gyuuhimochi] </span><span class="pretty">Furuhonya no Tenshi</span><span class="after"> (COMIC LO 2019-07) [Chinese] [一匙咖啡豆汉化组] [Digital]</span>
        Re_bef = soup.find_all("span", class_="before")
        Re_pty = soup.find_all("span", class_="pretty")
        try:
            # 取第二項<span class="">值
            for before in Re_bef:
                bef = before.string
                if(timer_b==2):
                    timer_b=0
                    break
            # 取第二項<span class="">值
            for pretty in Re_pty:
                pty = pretty.string
                if(timer_b==2):
                    timer_b=0
                    break
        except:
            bef = ""
            pty = pretty.string
        Title = bef + pty
        # 取出content值中的網址 <meta itemprop="image" content="https://t.nhentai.net/galleries/1454538/cover.png" /><meta    
        # 可看下面return使用 PicURL["content"]
        PicURL = soup.find("meta", itemprop="image")
###     用try except避防爬蟲找不到其他5個推薦的網站 而罷休的問題 (已解決)
        try:
            URL = soup.find_all("div",class_='gallery')
            # 老樣子去查 <div class="gallery" 之全部值(find_all)
            for gallery in URL:
                # 懶得處理直接全部強制轉換，用for&陣列去存全部整理過之result
                # site抓網址
                site[timer]=str("https://nhentai.net"+gallery.a["href"])
                # name抓每篇標題
                name[timer]=str(gallery.a.div.string)
                # picture抓預覽圖片，並且將連結中thumb取代為cover(畫質高一點點)
                picture[timer]=str(gallery.a.img["data-src"].replace("thumb","cover"))
                # number_N將原始網址site取出6位數(神的語言)
                number_N[timer]=str(site[timer].split("/")[4])
                # 這個無意義，只是當初和未來都好debug
                timer += 1
                if(timer==5):
                    timer = 0
                    break
            # 確定有5個推薦序去做 FlexMess
            return Hentai_Path_N(
                event,
                Action_but,
                "https://nhentai.net/g/"+str(num),
                PicURL["content"],
                Title,
                num,
                #recommand
                site[0],
                name[0],
                picture[0],
                number_N[0],
                site[1],
                name[1],
                picture[1],
                number_N[1],
                site[2],
                name[2],
                picture[2],
                number_N[2],
                site[3],
                name[3],
                picture[3],
                number_N[3],
                site[4],
                name[4],
                picture[4],
                number_N[4]
            )
        except:
            # 錯誤的話(無推薦序)call使用者input那個就好
            return Hentai_Path_N_except(
                event,
                Action_but,
                "https://nhentai.net/g/"+str(num),
                PicURL["content"],
                Title,
                num
            )


#爬蟲測試檔案(w網)
def getData_W(Action_but,num,event):
    url = "http://wnacg.org/photos-index-aid-"+num+".html"
    url_ret = "http://wnacg.org/photos-slide-aid-"+num+".html"
    pic = [0]*3
# google 升級後這裡驗證要重新去network/user-agent 抓 Chrome version
    request = req.Request(url, headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
    soup = bs4.BeautifulSoup(data, "html.parser")
#抓title
    title = soup.title.string
    title = title.replace('- 紳士漫畫-專註分享漢化本子|邪惡漫畫','')
    i = 0
#抓前3張圖片
    Res_pic = soup.find_all("div", class_="pic_box tb")
    for pic_box_tb in Res_pic:
        if(i<3):
            pic[i] = pic_box_tb
            i += 1
        else:
            break
    return Hentai_Path_W(
        event,
        Action_but,
        url_ret,
        title,
        num,
        "https:"+pic[0].a.img["data-original"],
        "https:"+pic[2].a.img["data-original"]
    )


#爬蟲檔案(18c)
def getData_18C(Action_but,num,event):
    url = "https://18comic.vip/photo/"+str(num)
    request = req.Request(url, headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
    soup = bs4.BeautifulSoup(data, "html.parser")
#抓title
    title = soup.title.string
    title = title.replace("|H漫內頁瀏覽 Comics - 禁漫天堂","")
#抓主要圖片
    Res_pic = "https://cdn-msp.18comic.org/media/photos/"+str(num)+"/00001.jpg"
#抓recommand
    recommand = soup.find_all("div", class_ ="well well-sm")
#推薦序存值
    recom_num = [0]*5
    recom_title = [0]*5
    for i in range (0,5):
        recom_item = recommand[i].a['href'].split("/")
        recom_num[i] = recom_item[2]
        recom_title[i] = recom_item[3]
#推薦序
    try:
        return Hentai_Path_18C(
            event,
            Action_but,
            url,
            title,
            num,
            Res_pic,
            recom_title[0],
            recom_num[0],
            recom_title[1],
            recom_num[1],
            recom_title[2],
            recom_num[2],
            recom_title[3],
            recom_num[3],
            recom_title[4],
            recom_num[4],
        )
#例外處理 只回傳單一車
    except:
        return Hentai_Path_18C_except(
            event,
            Action_but,
            url,
            title,
            num,
            Res_pic
        )