#三重クォート文字列/複数行
"""
line one
line two
line three
"""

#文字列のインデックス
from msilib import FCICreate


author ="kafka"
author[0]
author[1]
author[2]
author[3]
author[4]
#例外
author[5]

#マイナスインデックス/後ろから指定
author ="kafka"
author[-1]
author[-2]
author[-3]

#文字列はイミュータブル
ff = "F.Fitzgerald"
ff = "F.Scott Fitzgerald"
ff

#文字列の足し算
"cat"+"in"+"hat"
"cat"+" in"+" the"+" hat"
#文字列のかけ算
"Sayer" * 3

#大文字小文字変換
"we hold these truths...".upper()
"SO IT GOES.".lower()
#最初だけ大文字
"four score and...".capitalize()

#書式化{}に文字代入
"こんにちは、{}".format("ウィリアム・フォークナー")
#変数
name = "ウィリアム・フォークナー"
"こんにちは、{}".format("name")
#{}複数使用可能
author = "ウィリアム・フォークナー"
year_born = "1897"
"{}は{}年に生まれました。".format(author, year_born)

#他者入力の場合も有効
what = input("何が:")
when = input("いつ:")
where = input("どこで:")
do = input("どうした:")

r = "{}は{}に{}で{}。".format(what,when,where,do)
print(r)

#分割/splitの引数にどの文字で分割したいかの文字列を渡す。
"水たまりを飛び越えたんだ。３メートルもあったんだぜ！".split("。")

#結合/すべての文字列の間に新しい文字列を追加
first_three = "abc"
result = "+".join(first_three)
result
#結合/リスト
words = ["The","fox","jumped","over","the","fence","."]
one = "".join(words)
one
#結合/リスト2
words = ["The", "fox", "jumped", "over", "the", "fence", "."]
one = " ".join(words)
one

#空白除去
s = "    The   "
s = s.strip()
s

#置換
equ = "all advise ao awesome"
equ = equ.replace("a","@")
print(equ)

#文字が最初に現れる位置を探す
"animals".index("m")
#含まれていない文字の場合は例外
"animals".index("z")
#含まれていない文字の場合は例外処理を書く
try:
  "animals".index("z")
except:
  print("Not found.")

#包含/指定した文字列を含んでいるか確認
"Cat" in "Cat in the hat."
"Bat" in "Cat in the hat"
"Potter" not in "Harry"

#エスケープ文字/特定の文字の前に記号を書くこと
#例外
"彼女は "そうだね" といった"
#クオート文字の前で\
"彼女は \"そうだね\" といった"
#ダブルの場合はシングルでもOK
"彼女は 'そうだね' といった"
#逆
'彼女は "そうだね" といった'

#改行 \n
print("line1\nline2\nline3")

#スライス/指定したインデックスまでの値を取り出す
fict = ["トルストイ","カミュ","オーウェル","ハクスリー","オースティン"]
fict[0:3]

#スライス/文字列"
ivan = "死の代わりに一つの光があった。"
ivan[0:6]
ivan[6:16]

#スライス/0から始める場合は省略可
ivan = "死の代わりに一つの光があった。"
ivan[:6]

#スライス/最後の要素まで含める場合省略可
ivan = "死の代わりに一つの光があった。"
ivan[6:]

#スライス/全文コピー
ivan = "死の代わりに一つの光があった。"
ivan[:]
