# import math
class Hexagon:
    def __init__(self, r):
        self.radius = r
    
    def calculate_perimete(self):
        return self.radius * 6

h = Hexagon(10)
print(h.calculate_perimete())
