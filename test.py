#爬蟲測試檔案(n網)

import urllib.request as req
import bs4
def getData(url):
    timer = 0
    timer_b =0
    max_value = 3
    site=[0]*max_value
    name=[0]*max_value
    picture=[0]*max_value
    number_n=[0]*max_value
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
        print("-------------------------")
        Title = bef + aft
        print(Title)
        PicURL = soup.find("meta", itemprop="image")
        print(PicURL["content"])
        print("-------------------------")
        URL = soup.find_all("div",class_='gallery')
        for gallery in URL:
            site[timer]=str("https://nhentai.net"+gallery.a["href"])
            name[timer]=str(gallery.a.div.string)
            picture[timer]=str(gallery.a.img["data-src"].replace("thumb","cover"))
            number_n[timer]=str(site[timer].split("/")[4])
            print(site[timer])
            print(name[timer])
            print(picture[timer])
            print(number_n[timer])
            print("-------------------------")
            timer += 1
            if(timer==max_value):
                timer = 0
                break

#getData('https://nhentai.net/g/300000')



#爬蟲測試檔案(imgur)