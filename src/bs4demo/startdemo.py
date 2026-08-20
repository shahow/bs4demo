from bs4 import BeautifulSoup
import requests

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/139.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "zh-TW,zh;q=0.9,en;q=0.8",
}

def save_page(url, file_path):
    response = requests.get(url, headers=headers)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(response.text)

url = 'https://shahow.github.io/bs4demo/'
web = requests.get(url, headers=headers)   
soup = BeautifulSoup(web.text, "html.parser")  # 轉換成標籤樹
title = soup.title                             # 取得 title
print(title)  
body = soup.body                             # 取得 body
print(body.text)  
print("-----------------------------")
print(soup.h2.text)  # 取得第一個 h2 標籤的文字

h2=soup.find('a',href="#top")  # 取得所有 h2 標籤
print(h2.text)  # 取得第一個 h2 標籤的文字
div=soup.find_all('div')  # 取得所有 div 標籤
print("-----------------------------")
#for d in div:
#    print(d.text)  # 取得每個 div 標籤的文字

print(soup.find('div', class_="hero-art"))