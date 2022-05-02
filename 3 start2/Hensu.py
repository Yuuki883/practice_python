#出力
from re import X
from tkinter import Y


print("python")
print("こんにちわ")

print("""
      これはとてもとても長い
      複数行のコードです
      aaaaaaaaaaaaaa。""")

print\
  (""""
   これはとてもとても長い
      複数行のコードです""")

#定数
2 + 2
2 - 2
4 / 2
2 * 2

#変数
b = 10000
b
#変数変更
x = 1000
x
x = 200
x

x = 1000
y = 1000
z = x + y
z
a = x - y
a

#インクリメント,デクリメント
x = 1000
x = x + 1000
x

x = 1000
x += 1000
x

x = 1000
x -= 1000
x

#変数ルール/スペースは含められない/文字、数値、アンダースコア記号の三種類を含められる/１文字目に数字は✖︎、_はok/pythonキーワードはNG
hi = "hello,world!"
my_float = 2.2
my_boolean = True

#構文
#エラー例
my_string="hello world.
SyntaxError: unterminated string literal (detected at line 1)
#SyntaxError=構文エラー

#ZeroDivisionError
10/0
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    10/0
ZeroDivisionError: division by zero
#ZeroDivisionError=例外が発生

#算術演算子

#累乗
2**3
#余剰
14 % 4
#割り算、切り捨て
13//8
#割り算(除算)
13 / 8
#かけ算
2 * 10
#ひき算
10 - 5
#足し算
10 + 10

#比較演算子

# > 左辺が右辺より大きい
100 > 10

# < 左辺が右辺より小さい
100 < 10

# >= 左辺が右辺以上
3 >= 2

# <= 左辺が右辺以下
1 <= 2

# == 左辺と右辺が同じ
2 == 2

# != 左辺と右辺が異なる
1 != 2

#論理演算子

#and かつ 左右の式がtrueの場合はtrue
1 == 1 and 2 == 2
1 == 2 and 2 == 2

#or あるいは 左右の式のどちらかがtrueの場合はtrue
1 == 2 or 2 == 2

#not 否定 式の評価逆転
not 1 == 1
not 1 == 2