#1
from operator import imod


class Apple():
    def __init__(self, color, weight, stem_length, circumference):
        self.color = color
        self.weight = weight
        self.stem_length = stem_length
        self.circumference = circumference

c = Apple("blue",10,15,100)
print(c.weight)

#2
import math

class Circle():
  def __init__(self, radius):
    self.radius = radius
  def calculate_area(self):
    return self.radius ** 2 * math.pi

a_circle = Circle(6)
print(a_circle.calculate_area())

#3
class Triangle():
  def __init__(self,bottom,height):
    self.bottom = bottom
    self.height = height
  def triangle_area(self):
    return self.bottom * self.height / 2

a_triangle = Triangle(15,10)
print(a_triangle.triangle_area())

#4
class Hexagon():
    def __init__(self, s1, s2, s3, s4, s5, s6):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.s4 = s4
        self.s5 = s5
        self.s6 = s6

    def calculate_perimeter(self):
        return self.s1 + self.s2 + self.s3 + self.s4 + self.s5 + self.s6

a_hexagon = Hexagon(1, 2, 3, 4, 5, 6)
print(a_hexagon.calculate_perimeter())