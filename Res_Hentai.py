#============================================================
from FlexMessage import *
import urllib.request as req
import bs4
#============================================================
def getData(Action_but,url,user_input):
    timer = 0
    max_value = 3
    site=[0]*max_value
    name=[0]*max_value
    picture=[0]*max_value
    number_N=[0]*max_value
    request = req.Request(url, headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
    soup = bs4.BeautifulSoup(data, "html.parser")
    if "» nhentai: hentai doujinshi and manga" in soup.title.string :
        Title=str(soup.title.string).split("» nhentai: hentai doujinshi and manga")[0]
        PicURL = soup.find("meta", itemprop="image")
###
        URL = soup.find_all("div",class_='gallery')
        for gallery in URL:
            site[timer]=str("https://nhentai.net"+gallery.a["href"])
            name[timer]=str(gallery.a.div.string)
            picture[timer]=str(gallery.a.img["data-src"].replace("thumb","cover"))
            number_N[timer]=str(site[timer].split("/")[4])
            timer += 1
            if(timer==max_value):
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
        )
    elif "- 列表 - 紳士漫畫-專註分享漢化本子|邪惡漫畫" in soup.title.string :
        print(str(soup.title.string).split("- 列表 - 紳士漫畫-專註分享漢化本子|邪惡漫畫")[0])
#url = "http://wnacg.org/photos-slide-aid-100000.html"