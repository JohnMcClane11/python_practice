class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def rectArea(self):
        return self.a * self.b
class Square:
    def __init__(self, c):
        self.c = c
    def sqrArea(self):
        return self.c ** 2
class Circle:
    def __init__(self, r, Pi = 3.14):
        self.r = r
        self.Pi = Pi
    def circArea(self):
        return self.Pi * self.r ** 2
