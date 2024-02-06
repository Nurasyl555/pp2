class Shape:
    def __init__(self, length):
        self.length = length
    def area(self):
        return 0 
class Square(Shape):
    def __init__(self, length):
        super().__init__(length)
    def area(self):
        return self.length * self.length 
x = Square(50)
k = x.area()
print(k)