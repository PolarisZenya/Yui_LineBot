#============================================================
from FlexMessage import *
import urllib.request as req
import bs4
#============================================================
def getData(Action_but,url,user_input):
    timer = 0
    timer_b = 0
    site=[0]*5
    name=[0]*5
    picture=[0]*5
    number_N=[0]*5
    request = req.Request(url, headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
    soup = bs4.BeautifulSoup(data, "html.parser")
    if "» nhentai: hentai doujinshi and manga" in soup.title.string :
        Re_bef = soup.find_all("span", class_="before")
        Re_aft = soup.find_all("span", class_="after")
        for before in Re_bef:
            bef = before.string
            if(timer_b==2):
                timer_b=0
                break
        for after in Re_aft:
            aft = after.string
            if(timer_b==2):
                timer_b=0
                break
        Title = bef + aft
        
        #Title=str(soup.title.string).split("» nhentai: hentai doujinshi and manga")[0]
        PicURL = soup.find("meta", itemprop="image")
### 
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
            return Hentai_Path(
                Action_but,
                url,
                PicURL["content"],
                Title,
                user_input,
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
            return Hentai_Path_1(
                Action_but,
                url,
                PicURL["content"],
                Title,
                user_input
            )
    elif "- 列表 - 紳士漫畫-專註分享漢化本子|邪惡漫畫" in soup.title.string :
        print(str(soup.title.string).split("- 列表 - 紳士漫畫-專註分享漢化本子|邪惡漫畫")[0])
#url = "http://wnacg.org/photos-slide-aid-100000.html"