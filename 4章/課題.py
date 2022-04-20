#1
def test(x):
  return x**2

print (test(4))

#2
def print_string(string):
  print(string)

print_string("Testing: 1, 2, 3.")

#3
def test(a,b,c,x=10,j=20):
  return a + b + c + x + j

result = test(5,10,15)
print(result)

#4
def test1(x):
  return x / 2

def test2(x):
  return y * 4

y = test1(4)
z = test2(y)

print(z)

#5
def test(string):
  try:
    return float(string)
  except ValueError:
    print("Could not convert the string to a float.")

c = test("aaa")
print(c)

#6
def test(x):
  """
  x２乗の結果を出力
  :param x: int,
  :return: x２乗
  """
  return x**2
print(test(4))


def print_string(string):
  """
  文字列を出力
  :param string: str,
  """
  print(string)
print_string("Testing: 1, 2, 3.")

def test(a, b, c, x=10, j=20):
  """
  3つの必須引数と2つのオプション引数の合計を出力
  :param a: int,
  :param b: int,
  :param c: int,
  :param x: int,
  :param j: int,
  :return: a,b,c,x,jの合計
  """
  return a + b + c + x + j

result = test(5, 10, 15)
print(result)


def test1(x):
  """
  x÷2の結果を出力
  :param x: int,
  :return: x÷2
  """
  return x / 2

def test2(x):
  """
  x×4の結果を出力
  :param x: int,
  :return: x×4
  """
  return y * 4

y = test1(4)
z = test2(y)

print(z)

def test(string):
  """
  文字列をfloat型に変換して出力
  :param string: str,
  :return: 文字列をfloat型に変換
  """
  try:
    return float(string)
  except ValueError:
    print("Could not convert the string to a float.")

c = test("aaa")
print(c)

