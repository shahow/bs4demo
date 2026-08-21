from bs4 import BeautifulSoup
import requests
import re
import gdown

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/139.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "zh-TW,zh;q=0.9,en;q=0.8",
}


url = 'https://www.weiqi.org.tw/Weiqi/Home/Index2'
web = requests.get(url, headers=headers)   
soup = BeautifulSoup(web.text, "html.parser")  # 轉換成標籤樹           
allb=soup.find_all('a',href=re.compile(r"^\/Weiqi\/Race\/RaceDetail"))  # 取得所有 a 標籤
for a in allb:
    detailweb = requests.get("https://www.weiqi.org.tw"+a["href"], headers=headers)   
    detailsoup = BeautifulSoup(detailweb.text, "html.parser") 
    #print(detailweb.text)
    innera = detailsoup.find_all('iframe')
    h2=detailsoup.find('h2',class_="title")
    filename = h2.text.replace('/','')
    print(h2.text)
    for ia in innera:
        print("------------------------------")
        print(ia.get('src'))
        gdown.download(ia.get('src'), r"D:\races\{0}.pdf".format(filename), quiet=False)
    #print(detailweb.text)  # 取得所有 a 標籤