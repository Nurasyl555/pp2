class Kvad:
    def __init__(self, n):
        self.n = n
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a <= self.n:
            if self.a % 2 == 0:
                x = self.a**2
                self.a += 1
                return x
        else:
            raise StopIteration
h = Kvad(5)
myiter = iter(h)
for i in myiter:
    print(i)