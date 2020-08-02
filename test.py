import urllib.request as req
def getData(url):
    request = req.Request(url, headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")

    import bs4
    root = bs4.BeautifulSoup(data, "html.parser")
    print(root.title.string)
#    titles = root.find("div", class_="shareBox")
#    print(titles)

url = "http://wnacg.org/photos-slide-aid-100000.html"
getData(url)