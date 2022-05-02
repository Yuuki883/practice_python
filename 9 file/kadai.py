#1
with open("st.txt","r", encoding="utf-8") as f:
  print(f.read())

#2
guess = input("何色が好き？(入力してください):")
with open("st.txt","w", encoding="utf-8") as st
st.write(guess)
st.close()

#3
import csv

movies = [["Top Gun", "Risky Business", "Minority Report"], ["Titanic", "The Revenant", "Inception"], ["Training Day", "Man on Fire", "Flight"]]
with open("movies.csv", "w") as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=",")
    for movie_list in movies:
        spamwriter.writerow(movie_list)

#4
import csv

movies = [["のだめカンタービレ","ミッドナイトイーグル","ハリーポッター"], ["エヴァンゲリオン","燃えよ剣","鬼滅の刃"], ["ジョーカー","銀英伝","閃光のハサウェイ"]]
with open("movies2.csv", "w", encoding="utf-8") as moviefile:
  a = csv.writer(moviefile, delimiter=",")
  for list in movies:
    a.writerow(list)