#if文

x = 2
if x == 2:
  print("数値は2です")
  if x % 2 == 0:
    print("数値は偶数です")
    if x % 2 != 0:
      print("数値は奇数です")

home = "タイ"
if home == "日本":
  print("Hello,Japan!")
elif home == "タイ":
  print("Hello Thailand!")
elif home == "インド":
  print("Hello india")
elif home == "中国":
  print("Hello china")
else:
  print("Hello world")

home = "Thailand"
if home == "Japan":
    print("Hello, Japan!")
elif home == "Thailand":
    print("Hello, Thailand!")
elif home == "India":
    print("Hello, India!")
elif home == "China":
    print("Hello, China!")
else:
    print("Hello, World!")

home = "Mars"
if home == "America":
    print("Hello, America!")
elif home == "Canada":
    print("Hello, Canada!")
elif home == "Thailand":
    print("Hello, Thailand!")
elif home == "Mexico":
    print("Hello, Mexico!")
else:
    print("Hello, World!")

    x = 100
if x == 10:
    print("10!")
elif x == 20:
    print("20!")
else:
    print("I don’t know!")


if x == 100:
    print("x is 100!")


if x % 2 == 0:
    print("x is even!")
else:
    print("x is odd!")

print("hello") and print(12345) and print(hello)

x = 3
if x < 10:
  print("10未満")
else:
  print("10以上")

x = 3
if x <= 10:
  print("10未満")
elif x > 10 and x <= 25:
  print("10以上25未満")
else:
  print("25以上")

age = 27
if age == 18:
  print("大学生")
elif age == 23:
  print("社会人")
else:
  print("社畜")

age = 130
retirement = age - 65

if retirement < 10:
    print("You get to retire soon.")
else:
    print("You have a long time until you can retire!")

#関数内からグローバル変数に書き込み
x = 100

def f():
  global x
  x += 1
  print(x)

f()

#例外処理=予想されるエラーを回避するための処理
a = input("50")
b = input("10")
a = int(a)
b = int(b)
print(a/b)


a = 50
b = 10
print(a/b)
