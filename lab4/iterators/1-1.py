def generator(n):
    value = 1
    while value <= n:
        yield value**2
        value += 1
n = int(input())
for value in generator(n):
    print(value)