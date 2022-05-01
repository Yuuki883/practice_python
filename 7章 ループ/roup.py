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
