#1
#四角形
class Rectangle():
    def __init__(self, width, length):
        self.width = width
        self.length = length
    def calculate_perimeter(self):
        return self.width * 2 + self.length * 2

#正方形
class Square():
    def __init__(self,s1):
        self.s1 = s1
    def calculate_perimeter(self):
        return self.s1 * 4

rectangle = Rectangle(10,20)
print(rectangle.calculate_perimeter())
square = Square(30)
print(square.calculate_perimeter())

#2
class Square():
    def __init__(self,s1):
        self.s1 = s1
    def calculate_perimeter(self):
        return self.s1 * 4
    def change_size(self, new_size):
        self.s1 += new_size

square = Square(20)
print(square.s1)
square.change_size(5)
print(square.s1)

#3
class Shape():
    def what_am_i(self):
        print("I am a shape.")

class Rectangle(Shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length
    def calculate_perimeter(self):
        return self.width * 2 + self.length * 2

#正方形
class Square(Shape):
    def __init__(self,s1):
        self.s1 = s1
    def calculate_perimeter(self):
        return self.s1 * 4

a_rectangle = Rectangle(20, 50)
a_square = Square(29)

a_rectangle.what_am_i()
a_square.what_am_i()

#4


class Rider():
    def __init__(self, name):
        self.name = name
class Horse():
    def __init__(self, name, rider):
        self.name = name
        self.rider = rider

the_rider = Rider("Sally")
harry_the_horse = Horse("Harry", the_rider)

print("The name of Horse is {}".format(harry_the_horse.name))
print("The name of Rider is {}".format(harry_the_horse.rider.name))