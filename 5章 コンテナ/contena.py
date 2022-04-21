#メソッド

# 大文字にする
from random import random

"Hello".upper()
#置換
"Hello".replace("o","@")

#リスト
fruit = list()
fruit = []

fruit = ["Apple","Orange","Pear"]
fruit

#リスト追加
fruit = ["Apple","Orange","Pear"]
fruit.append("Banana")
fruit.append("Peach")
fruit

#リスト追加2
random = []
random.append("True")
random.append(100)
random.append(1.1)
random.append("Hello")
random

#インデックス・・コンテナ内の要素の位置。最初は0から始まる
fruit = ["Apple","Orange","Pear"]
fruit[0]
fruit[1]
fruit[2]

#存在しないインデックス値を指定した場合、例外発生
colors = ["blue","green","yellow"]
colors[4]

#リストの位置や要素を入れ替え可能
colors = ["blue","green","yellow"]
colors
colors[2] = "red"
colors