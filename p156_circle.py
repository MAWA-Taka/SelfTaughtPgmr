import math
class Circle:
    def __init__(self, r):
        self.radius = r
    
    def calc_area(self):
        return self.radius ** 2 * math.pi

c = Circle(10)
print(c.radius)
print(c.calc_area())
