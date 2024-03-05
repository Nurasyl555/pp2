import math, time
def root_time(square, the_time):
    time.sleep(the_time/1000)
    return math.sqrt(square)
numbers = int(input())
the_time = int(input())
print(f"Square root of {numbers} after {the_time} miliseconds is {root_time(numbers, the_time)}")
