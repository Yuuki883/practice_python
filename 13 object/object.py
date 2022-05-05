#オブジェクト指向の４大要素

#カプセル化
#1複数のメソッドと変数をまとめること
class Rectangle:
  def __init__(self,w,l):
    self.width = w
    self.len = l

  def area(self):
    return self.width * self.len


#2データをクラス内に隠蔽して外から見えないようにすること。メソッドを通じて操作
class Data:
    def __init__(self):
        self.num = [1, 2, 3, 4, 5]
    def change_data(self, index, n):
        self.num[index] = n

data_one = Data()
data_one.num[0] = 100
print(data_one.num)

data_two = Data()
data_two.change_data(0, 100)
print(data_two.num)

#client(クラスの外側からオブジェクトを操作するコード)からアクセスして欲しくない場合には名前の前に_をつける
class PublicPrivateExample:
    def __init__(self):
        self.public = "safe"
        self._unsafe = "unsafe"

    def public_method(self):
        # clients can use this
        pass

    def _unsafe_method(self):
        # clients shouldn't use this
        pass

#2抽象化

#3ポリモーフィズム/同じインターフェースでありながらデータ型に合わせて異なる動作をする機能
print("Hello, world!")
print(200)
print(200.1)
type("Hello world")
type(200)
type(200.1)

#4継承/
class Shape():
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def print_size(self):
        print("""{} by {}""".format(self.width,self.len))

class Square(Shape):
    pass

a_square = Square(20,20)
a_square.print_size()

class Shape():
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def print_size(self):
        print("""{} by {}
              """.format(self.width,
                          self.len))

class Square(Shape):
    def area(self):
        return self.width * self.len

a_square = Square(20, 20)
print(a_square.area())

#オーバーライド/子クラスが親クラスのメソッドを別の実装で書き換える
class Shape():
    def __init__(self, w, l):
        self.width = w
        self.len = l
    def print_size(self):
        print("{} by {}".format(self.width,self.len))
class Square(Shape):
    def area(self):
        return self.width * self.len
    def print_size(self):
        print("I am {} by {} ".format(self.width,self.len))

a_square = Square(20, 20)
a_square.print_size()

#コンポジション/has-a関係、別クラスのオブジェクトを変数として持つ
class Horse:
  def __init__(self,name,owner):
    self.name = name
    self.owner = owner

class Rider:
  def __init__(self,r_name):
    self.r_name = r_name

n = Rider("Yuki")
h_name = Horse("スーホー",n)
print(h_name.owner.r_name)
print("The name of Horse is {}".format(h_name.name))
print("The name of Rider is {}".format(h_name.owner.r_name))


