def filter_prime(numbers):
    for x in numbers:
        flag = True
        for i in range(2, int(x**0.5)+1):
            if x % i == 0:
                flag = False
        if flag:
            print(x, end=" ")
numbers = list(map(int, input().split()))
filter_prime(numbers)