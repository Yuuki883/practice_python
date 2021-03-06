#def [関数名]([引数]):
    #[関数定義]

#
def f(x):
    return x * 2

#関数の戻り値を変数に保存
result = f(2)
print(result)

#
def f(x):
    return x + 1

z = f(4)

if z == 5:
    print("z is 5")
else:
    print("z is not 5")


def f(x):
    return 1 + 1


result = f()

if z == 5:
    print("z is 5")
else:
    print("z is not 5")

# 複数の関数の場合


def f(x, y, z):
    return x + y + z


result = f(1, 2, 3)
print(result)

# 文字列の長さ
len("Monty")
len("python")

# 整数を文字列に変換
str(100)

# 文字列を整数に変換
int("1")
int(20.54)
# 以下は不可
int("prince")

# 浮動小数点数オブジェクトを返す
float(100)
float("16.4")

# input関数.文字列を引数として受け取る
age = input("Enter your age:")

int_age = int(age)
if int_age < 21:
    print("You are young!")
else:
    print("wow, you are old!")

# 関数の再利用


def even_old(x):
    if x % 2 == 0:
        print("偶数")
    else:
        print("奇数")


even_old(2)
even_old(3)

# 関数の再利用2


def even_odd():
    n = input("type a number:")
    n = int(n)
    if n % == 0:
        print("n is even.")
    else:
        print("n is odd.")


even_odd()
even_odd()

# 必須引数とオプション引数


def f(x=2):
    return x ** x
print(f())
print(f(3))

# 必須引数とオプション引数
def f(x=2):
    return x ** x
print(f())
print(f(3))

def add_it(x,y=10):
  return x + y

result = add_it(2)
print(result)

#スコープ・・変数を定義するとその変数を読み書きできる範囲
#関数やクラスの外で定義された変数はグローバルスコープに定義される。グローバルスコープの変数はグローバル変数と呼ぶ。
# どの範囲のプログラムからでも読み込み可能
x = 1
y = 2
z = 3

def f(v=4):
  print(x)
  print(y)
  print(z)
  print(v)

f()

#関数内で定義された変数はローカルスコープに定義される。ローカルスコープの変数はローカル変数と呼ぶ。
#関数内で定義した変数はその関数の内部からのみ読み書き可能
def f():
  x = 1
  y = 2
  z = 3
  print(x)
  print(y)
  print(z)

f()

#エラー発生
def f():
  x = 1
  y = 2
  z = 3

print(x)
print(y)
print(z)

if x > 100:
  print("x is > 100")

#関数内からグローバル変数に書き込み
x = 100

def f():
  global x
  x += 1
  print(x)

f()

#例外処理=予想されるエラーを回避するための処理
#try=例外発生の可能性のあるエラー
#except=例外が発生した場合に実行するコード
a = input("type a number:")
b = input("type another:")
a = int(a)
b = int(b)
try:
    print(a / b)
except ZeroDivisionError:
    print("b cannot be zero.")
#複数の場合
try:
    a = input("type a number:")
    b = input("type another:")
    a = int(a)
    b = int(b)
    print(a / b)
except (ZeroDivisionError, ValueError):
    print("Invalid input.")

#ドキュメンテーション文字列/関数の内容について記載
def add(x, y):
  """
  Returns x+y
  :param x: int.
  :param y: int.
  :return: int sum of x and y.
  """
  return x+y

#出力したい値を直接関数に渡す
print(100)

