def generator(n):
    value = 0
    while value <= n:
        yield value
        value += 2
n = int(input())
for value in generator(n):
    print(value)