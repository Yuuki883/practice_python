#プログラミングパラダイム/プログラミングスタイル・手法のこと

#手続型プログラミング/連続した手続きをこなし、途中途中でステート（変数）をかえて答えを導く。
#データをグローバル変数として持ち、関数でそのデータを参照する
#複数の関数にまたがっtr同じデータを扱いたい場合に、グローバル変数によって管理していることでエラーが発生しやすくなる
from os import O_TEMPORARY


x = 20
y = 30
z = 8
xyz = x + y + z
xyz

rock = []
country = []

def collect_songs():
    song = "Enter a song."
    ask = "Type r or c. q to quit"

    while True:
        genre = input(ask)
        if genre == "q":
            break

        if genre == "r":
            rk = input(song)
            rock.append(rk)

        elif genre ==("c"):
            cy = input(song)
            country.append(cy)

        else:
            print("Invalid.")
    print(rock)
    print(country)

collect_songs()

#関数型プログラミング/グローバル関数に頼らず関数から関数へ変数を渡す

#副作用を起こす関数/関数のデータに依存して関数のデータを変更する
a = 0
def increment():
  global a
  a += 1
#副作用のない関数/関数街の変数を参照しない
def increment(a):
  return a + 1

#オブジェクト指向プログラミング/相互に作用するオブジェクトを定義するプログラミング
#class [クラス名]: クラス名は常に大文字
  #[スイート] 単純文またはメソッドを記載
class Orange:
  #__は特殊メソッド
  def __init__(self,w,c):
    self.weight = w
    self.color = c
    print("Created new Orange")
#オブジェクト作成,クラスのインスタンス化/[クラス名] ([引数])
orl = Orange(10,"dark orange")
print(orl)
#インスタンス変数の値を取得　/[オブジェクト名].[インスタンス名]
#インスタンス変数/オブジェクトに属する変数
print(orl.weight)
print(orl.color)
#インスタンス変数の値を変更/[オブジェクト名].[インスタンス名] = [新しい値]
orl1 = Orange(10,"dark orange")
orl1.weight = 100
orl1.color = "blue"

print(orl1.weight)
print(orl1.color)

#複数のオブジェクト作成
class Orange:
  def __init__(self,w,c):
    self.weight = w
    self.color = c
    print("Created new Orange")

orl1 = Orange(5,"red")
orl2 = Orange(10,"green")
orl3 = Orange(14,"blue")

#メソッド追加
class Orange:
    def __init__(self, w, c):
        """weights are in oz"""
        self.weight = w
        self.color = c
        self.mold = 0
        print("Created!")
    def rot(self, days, temp):
        """temp(温度)は摂氏"""
        self.mold = days * temp

orange = Orange(200, "orange")
print(orange.mold)
orange.rot(10, 37)
print(orange.mold)

#長方形計算
class Rectangle:
  def __init__(self,w,l):
    self.width = w
    self.len = l
  def area(self):
    return self.width * self.len
  def change_size(self,w,l):
    self.width = w
    self.len = l

rectangle = Rectangle(10,20)
print(rectangle.area())
rectangle.change_size(20,30)
print(rectangle.area())