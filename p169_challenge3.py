class Shape:
    def what_am_i(self):
        print("I am a shape")

class Rectangle(Shape):
    def __init__(self, w, l):
        self.width = w
        self.len = l
    
    def calculate_perimeter(self):
        return self.width * 2 + self.len * 2

class Square(Shape):
    def __init__(self, w):
        self.width = w
    
    def calculate_perimeter(self):
        return self.width * 4

    def change_size(self, w):
        self.width += w  

r =  Rectangle(10, 20)
print(r.calculate_perimeter())

s = Square(10)
print(s.calculate_perimeter())

s.change_size(5)
print(s.calculate_perimeter())

s.change_size(-10)
print(s.calculate_perimeter())

sh=Shape()
sh.what_am_i()

r.what_am_i()
s.what_am_i()