def generator(a, b):
    value = a
    while value <= b:
        yield value**2
        value += 1
a = int(input())
b = int(input())
for value in generator(a, b):
    print(value)