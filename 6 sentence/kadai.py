#1文字を１文字ずつ出力
kamyu = "カミュ"
print(kamyu[0])
print(kamyu[1])
print(kamyu[2])

#2文字列入力関数
moji1 = input("")
moji2 = input("")
Bun = "私は{}を書いて{}に送った!".format(moji1, moji2)
print(Bun)

#3先頭のみ大文字
v = "aldous Huxley was born in 1894.".title()
print(v)

#4
matome = "どこで? 誰が？ いつ？".split("?")
print(matome)

#5
matome = ["The","fox","jumped","over","the","fence","."]
matome = " ".join(matome)
matome = matome[: -2] + "."
print(matome)

#6
moji = "A screaming comes across the sky.".replace("s", "$")
print(moji)

#7
moji = "Hemingway".index("m")
print(moji)

#8
serifu = "君は'君だ'と言った,'嘘だ'"
print(serifu)

#9
a = "three"+"three"+"three"
b = "three"*3
print(a)
print(b)

#10
bun = "４月の晴れた寒い日で、時計がどれも13時を打っていた。"
bun2 = bun[:10]
print(bun2)
