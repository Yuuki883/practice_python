#クラスオブジェクト
class Square:
  pass

print(Square)

class Rectangle():
    def __init__(self, w, l):
      #インスタンス変数
        self.width = w
        self.length = l

    def print_size(self):
        print("""{} by {}""".format(self.width,self.length))

my_rectangle = Rectangle(10, 24)
my_rectangle.print_size()

class Rectangle():
  #クラス変数/__init__メソッドの外で行う
    recs = []

    def __init__(self, w, l):
        self.width = w
        self.len = l
        self.recs.append((self.width,self.len))

    def print_size(self):
        print("""{} by {}
              """.format(self.width,self.len))

#Rectangleクラスのオブジェクト、recsに追加
r1 = Rectangle(10, 24)
r2 = Rectangle(20, 40)
r3 = Rectangle(100, 200)

print(Rectangle.recs)

#特殊メソッド
class Lion:
  def __init__(self,name):
    self.name = name
  def __repr__(self):
    return self.name

lion = Lion("Dilbert")
print(lion)

class AlwaysPositive:
    def __init__(self, number):
        self.n = number
    def __add__(self, other):
        return abs(self.n + other.n)

x = AlwaysPositive(-20)
y = AlwaysPositive(10)

print(x + y)

#is
class Person:
    def __init__(self):
        self.name = 'Bob'

bob = Person()
same_bob = bob
print(bob is same_bob)
print(bob.name)
print(same_bob.name)

another_bob = Person()
print(bob is another_bob)
print(bob.name is another_bob.name)
print(another_bob)
print(bob)
