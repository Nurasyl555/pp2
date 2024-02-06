class Person:
    def __init__(self):
        self.string = None
    def getString(self):
        self.string = input()
    def printString(self):
        print(self.string.upper())
d = Person()
d.getString()
d.printString()