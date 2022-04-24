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

#pop=リストの末尾から要素削除
colors = ["blue","green","yellow"]
colors
item = colors.pop()
item
colors

#リスト結合
colors1 = ["red","green","yellow"]
colors2 = ["orange","green","yellow"]
colors1 + colors2

#in＝リストに含まれている要素を確認
colors = ["blue","green","yellow"]
"green" in colors

#in＝リストに含まれていない要素を確認
colors = ["blue", "green", "yellow"]
"black" not in colors

#コンテナ内の要素数確認
len(colors)

#3種類の色当て
colors = ["purple","orange","green"]
guess = input("何色でしょう(入力してください):")

if guess in colors:
  print("当たり!")
else:
  print("ハズレ!また挑戦してね。")

#タプル=一度作ると内容を変更できない.変更してほしくない値で使用
my_tuple = tuple()
my_tuple
my_tuple = ()
my_tuple

#タプルにオブジェクトを追加する場合
rndm = ("M. jackson",1958,True)
rndm

#要素が一つの場合は,必要
#コレはタプルです
('self_taught',)

#コレはタプルではなく数値演算に使うカッコ
(9)+1

#コレはタプルではなく数値演算に使うカッコ
(9)+1

#要素変更不可
dys = ("M. jackson", 1958, True)
dys[1] = "Handomaids Tale"

#要素を取り出す場合にはインデックス
dys = ("M. jackson", 1958, True)
dys[0]

#要素の確認はin、入っていないことの確認はnotin
dys = ("M. jackson", 1958, True)
"M. jackson" in dys

dys = ("M. jackson", 1958, True)
"Handomaids Tale" not in dys

#辞書
my_dict = dict()
my_dict

my_dict = {}
my_dict

#キーバリューペア
fruits = {"Apple": "Red",
          "Banana": "Yellow"}
fruits

facts = dict()
#バリューを追加
facts["code"] = "fun"
#キーで参照
facts["code"]

#バリューを追加
facts["Bill"] = "Gates"
#キーで参照
facts["Bill"]

#バリューを追加
facts["founded"] = 1776
#キーで参照
facts["founded"]

#辞書のキーを確認。入っていないものを確認。バリューの確認は不可
bill = {"Bill Gates": "charitable"}
"Bill Gates" in bill
"Bill Doors" not in bill

#dell=キーバリュー削除
books = {"Dracula": "Stoker",
         "1984": "Orwell",
         "The Trial": "Kefka"}

del books["The Trial"]
books

songs = {"1": "fun",
         "2": "blue",
         "3": "me",
         "4": "floor",
         "5": "live",
         }

n = input("数字を入力してください")
if n in songs:
  song = songs[n]
  print(song)
else:
  print("見つかりません。")

#コンテナにコンテナを格納
lists = []


rap = ["カニエウエスト","ジェイZ","エミネム"]
rock = ["ビートルズ","ボブディラン"]
djs = ["ティエスと","ゼッズデッド"]

lists.append(rap)
lists.append(rock)
lists.append(djs)

print(lists)
rap = lists[0]
print(rap)

rap = lists[0]
rap.append("ケンドリックラマー")
print(rap)
print(lists)

#リストの要素にタプル
locations = []
la = (34.0052,177.2434)
chicago = (42.111, 87.6398)

locations.append(la)
locations.append(chicago)

print(locations)

#タプルの要素にリスト
eights = ["edgar","charles"]
nines = ["hemingway","orwel"]

author = (eights,nines)
print(author)

#リスト,タプルの要素に辞書
bday = {"hemingway": "7.21.1899",
        "fitzgerald": "9.24.1896"}

my_list = [bday]
print(my_list)
my_tuple = (bday,)
print(my_tuple)

#辞書のバリューとしてリスト、タプル、辞書を格納可能
ny = {
  "座標": (40.7128, 74.0059),
  
  "セレブ": [
    "ウッディ",
    "ジェイ",
    "ケヴィン",
  ],
  
  "事実": {
    "州": "ニューヨーク",
    "国": "アメリカ",
    }
  }
ny["セレブ"].append("マイク")
print(ny["セレブ"])
