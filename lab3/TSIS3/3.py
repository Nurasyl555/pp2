class Shape:
    def __init__(self, length):
        self.length = length
    def area(self):
        return 0 
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__(length)
        self.width = width
    def area(self):
        return self.width * self.length
x = Rectangle(50, 30)
audan = x.area()
print(audan)