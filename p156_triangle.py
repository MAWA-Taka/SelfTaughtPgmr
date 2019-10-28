# import math
class Triangle:
    def __init__(self, b, h):
        self.base = b
        self.height = h
    
    def calc_area(self):
        return self.base * self.height / 2

t = Triangle(20, 10)
print(t.base)
print(t.height)
print(t.calc_area())
