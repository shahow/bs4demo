from bs4 import BeautifulSoup
import requests
import re

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
    for ia in innera:
        print("------------------------------")
        print(ia.get('src'))
    #print(detailweb.text)  # 取得所有 a 標籤