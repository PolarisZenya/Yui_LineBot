#============================================================
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *
#============================================================
from FlexMessage import *
import urllib.request as req
#============================================================
def getData(url,user_input):
    try:
        request = req.Request(url, headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
        })
        with req.urlopen(request) as response:
            data = response.read().decode("utf-8")
    #    print(data)
        import bs4
        soup = bs4.BeautifulSoup(data, "html.parser")
        if "» nhentai: hentai doujinshi and manga" in soup.title.string :
            Title=str(soup.title.string).split("» nhentai: hentai doujinshi and manga")[0]
            PicURL = soup.find("meta", itemprop="image")
            PicURL = str(PicURL).replace('<meta content="','')
            PicURL = PicURL.replace('" itemprop="image"/>','')
            return Hentai_Path(PicURL,Title,user_input)
        elif "- 列表 - 紳士漫畫-專註分享漢化本子|邪惡漫畫" in soup.title.string :
            print(str(soup.title.string).split("- 列表 - 紳士漫畫-專註分享漢化本子|邪惡漫畫")[0])
    except:
        TextSendMessage(text = '查無這本車，請重新再試 若仍有此問題請聯絡作者')
#    print(soup.title.string)

#    titles = soup.find("div", class_="shareBox")
#    print(titles)

#url = "http://wnacg.org/photos-slide-aid-100000.html"
