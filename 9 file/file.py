#複数のフォルダを引数として受け取り、フォルダパスを組み立て可能
import os
#Users/bob/st.txt
os.path.join("Users","bob","st,txt")

#書き込み
st = open("st.txt","w")
st.write("Hi room Python")
#ファイル閉じる
st.close()
#日本語
st = open("st.txt","w", encoding="utf-8")
st.write("Pyhtonからこんにちは！")
st.close()

#自動閉じ
with open("st.txt","w") as f:
  f.write("Hi from Python!")

#読み込み
with open("st.txt","r") as f:
  print(f.read())
with open("st.txt","r", encoding="utf-8") as f:
  print(f.read())

#読み込み後にリストに入れる
my_list = []

with open("st.txt","r") as f:
  my_list.append(f.read())

print(my_list)

#csv書き込み
import csv

with open("st.csv","w", newline="") as f:
  w = csv.writer(f, delimiter=",")
  w.writerow(["one", "two", "three", "four", "five"])
  w.writerow(["five","six", "seven", "eight", "nine"])

#csv読み込み
import csv

with open("st.csv","r") as f:
  r = csv.reader(f,delimiter=",")
  for row in r:
    print(",".join(row))
