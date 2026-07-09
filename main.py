import urllib.request
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, site):
        self.site = site
    def scraper(self):
        r = urllib.request.urlopen(self.site)
        html = r.read()
        parser = "html.parser"
        sp = BeautifulSoup(html, parser)
        ext = []
        count = 0
        for tag in sp.find_all("a"):
            url = tag.get("href")
            if url is None:
                continue
            if "html" in url and url[15:17] == "20":
                count += 1
                ext.append(f"\n {count}.| {url} <-|")
        return ext

while True:
    news = input("Input website url-link: ")
    if news[0:8] != "https://":
        print("Error url link or it's not a safety!")
    else:
        my_file = open('news','w')
        my_file.writelines(Scraper(news).scraper())
        my_file.close()