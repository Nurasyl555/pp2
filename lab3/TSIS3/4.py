class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print(f"Coordinates: ({self.x}, {self.y})")
    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
    def dist(self, pp):
        print(((self.x-pp.x)**2 + (self.y - pp.y)**2)**0.5)
c1 = Point(0, 0)
c2 = Point(3, 4)
c1.show()
c2.show()
c1.dist(c2)

