#============================================================
from FlexMessage import *
import urllib.request as req
import bs4
#============================================================
from Animation import *
#============================================================
def getData_N(Action_but,num,event):
    timer = 0
    timer_b = 0
    site=[0]*5
    name=[0]*5
    picture=[0]*5
    number_N=[0]*5
    request = req.Request("https://nhentai.net/g/"+str(num), headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
    soup = bs4.BeautifulSoup(data, "html.parser")
    if "» nhentai: hentai doujinshi and manga" in soup.title.string :
        Re_bef = soup.find_all("span", class_="before")
        Re_pty = soup.find_all("span", class_="pretty")
        
        for before in Re_bef:
            bef = before.string
            if(timer_b==2):
                timer_b=0
                break
        for pretty in Re_pty:
            pty = pretty.string
            if(timer_b==2):
                timer_b=0
                break

        try:
            Title = bef + pty
        except:
            Title = pty
        PicURL = soup.find("meta", itemprop="image")

        try:
            URL = soup.find_all("div",class_='gallery')
            for gallery in URL:
                site[timer]=str("https://nhentai.net"+gallery.a["href"])
                name[timer]=str(gallery.a.div.string)
                picture[timer]=str(gallery.a.img["data-src"].replace("thumb","cover"))
                number_N[timer]=str(site[timer].split("/")[4])
                timer += 1
                if(timer==5):
                    timer = 0
                    break
            return Hentai_Path_N(
                event,
                Action_but,
                "https://nhentai.net/g/"+str(num),
                PicURL["content"],
                Title,
                num,
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
            return Hentai_Path_N_except(
                event,
                Action_but,
                "https://nhentai.net/g/"+str(num),
                PicURL["content"],
                Title,
                num
            )

def getData_W(Action_but,num,event):
    url = "http://wnacg.org/photos-index-aid-"+num+".html"
    url_ret = "http://wnacg.org/photos-slide-aid-"+num+".html"
    pic = [0]*3
    request = req.Request(url, headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
    soup = bs4.BeautifulSoup(data, "html.parser")
    title = soup.title.string
    title = title.replace('- 紳士漫畫-專註分享漢化本子|邪惡漫畫','')
    i = 0
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

def getData_18C(Action_but,num,event):
    url = "https://18comic.vip/photo/"+str(num)
    request = req.Request(url, headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
    soup = bs4.BeautifulSoup(data, "html.parser")
    title = soup.title.string
    title = title.replace("|H漫內頁瀏覽 Comics - 禁漫天堂","")
    Res_pic = "https://cdn-msp.18comic.org/media/photos/"+str(num)+"/00001.jpg"
    recommand = soup.find_all("div", class_ ="well well-sm")
    recom_num = [0]*5
    recom_title = [0]*5
    for i in range (0,5):
        recom_item = recommand[i].a['href'].split("/")
        recom_num[i] = recom_item[2]
        recom_title[i] = recom_item[3]
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
    except:
        return Hentai_Path_18C_except(
            event,
            Action_but,
            url,
            title,
            num,
            Res_pic
        )