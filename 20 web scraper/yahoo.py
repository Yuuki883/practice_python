#sudo pip install beautifulsoup4==4.4.1ではエラーになるので4.10.0に変更
import requests
from bs4 import BeautifulSoup
import re

# ヤフーニュースのトップページ情報を取得する
URL = "https://www.yahoo.co.jp/"
rest = requests.get(URL)

# BeautifulSoupにヤフーニュースのページ内容を読み込ませる
soup = BeautifulSoup(rest.text, "html.parser")

# ヤフーニュースの見出しとURLの情報を取得して出力する
data_list = soup.find_all(href=re.compile("news.yahoo.co.jp/pickup"))
for data in data_list:
    print(data.span.string)
    print(data.attrs["href"])