from FlexMessage import *
import urllib.request as req
import bs4

def getData_18C(num):
    url = "https://18comic.vip/photo/"+str(num)
    request = req.Request(url, headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
    soup = bs4.BeautifulSoup(data, "html.parser")
    #print(soup)
#抓title
    title = soup.title.string
    title = title.replace("|H漫內頁瀏覽 Comics - 禁漫天堂","")
#抓main
    Res_pic = "https://cdn-msp.18comic.org/media/photos/"+str(num)+"/00001.jpg"
    print(url)
    print(title)
    print(num)
    print(Res_pic)
    print("-----------------------------------")
#抓recommand
    recommand = soup.find_all("div", class_ ="well well-sm")
#推薦序存值
    recom_num = [0]*5
    recom_title = [0]*5

    for i in range (0,5):
        recom_item = recommand[i].a['href'].split("/")
        recom_num[i] = recom_item[2]
        recom_title[i] = recom_item[3]
        #pic = "https://cdn-msp.18comic.org/media/albums/"+recom_item[2]+"_3x4.jpg"
        #url = "https://18comic.vip/photo/"+recom_item[2]
        print(recom_title[i])
        print(recom_num[i])
        print("-----------------------------------")

getData_18C(217726)
