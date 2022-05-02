#条件文

from ast import Try

#if-else文
home = "アメリカ"
if home == "アメリカ":
    print("Hello, アメリカ!")
else:
  print("Hello, World!")

#複数のif文
x = 2
if x == 2:
  print("数値は2です")
  if x % 2 == 0:
    print("数値は偶数です")
    if x % 2 != 0:
      print("数値は奇数です")

#ネスト
x = 10
y = 11

if x == 10:
    if y == 11:
      print(x + y)

#elif文
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

#ifelse混合
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

#最後だけtrue
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

#ifelse混合2
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