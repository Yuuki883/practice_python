#for [変数名] in [イテラブル]:
    #[コードブロック]

name = "Ted"
for character in name:
  print (character)

#リスト
shows = ["Got","Narcos","Vice"]
for show in shows:
  print (show)


#tuple
coms = ("A.Development","Friends","Always Sunny")
for show in coms:
  print (show)

#辞書
people = {"G.Bluth II": "A.Development",
          "Barney": "HIMYM",
          "Dennis": "Always Sunny",
          }
for character in people:
  print (character)

#リスト更新
tv = ["GOT","Narcos","Vice"]
i = 0
for show in tv:
  """
  index指定
  """
  new = tv[i]
  new = new.upper()
  """
　リスト要素更新
  """
  tv[i] = new
  i += 1
print(tv)

#インデックス値を自動的に用意
tv = ["GOT","Narcos","Vice"]
for i, new in enumerate(tv):
  new = tv[i]
  new = new.upper()
  tv[i] = new

print(tv)

#ループでデータ加工
tv = ["GOT","Narcos","Vice"]
coms = ("A.Development","Friends","Always Sunny")
all_shows = []

for show in tv:
  show = show.upper()
  all_shows.append(show)

for show in coms:
  show = show.upper()
  all_shows.append(show)

print(all_shows)

#range 整数を順番に生成 range(開始値、終了値)
for i in range(1,11):
  print(i)

#while true評価の場合にはコードの実行を繰り返す
x = 10
while x > 0:
  print('{}'.format(x))
  x -= 1

print("Happy New Year!")

#無限ループ
while True:
  print("Hello,World!")

#break ループ終了文
for i in range(0,100):
  print(i)
  break

qs = ["what is your name?",
      "what is your fav. color?",
      "what is your quest?"]
n = 0
while True:
  print("Type  q to quit")
  a = input(qs[n])
  if a == "quit":
      break
  n = (n + 1) % 3

#continue　途中でループを止めて次の反復処理を開始
for i in range(1,6):
  if i == 3:
    continue
  print(i)

i = 1
while i <= 5:
  if i == 3:
      i += 1
      continue
  print(i)
  i += 1

#入れ子のループ
for i in range(1,3):
  print(i)
  for letter in ["a","b","c"]:
    print(letter)

list1 = [1,2,3,4]
list2 = [5,6,7,8]
added = []
for i in list1:
  for j in list2:
    added.append(i + j)

print(added)

#forの中にwhile
while input("y or n?") != "n":
  for i in range(1,6):
    print(i)