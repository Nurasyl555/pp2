# 1
print(10 + 5)
# 2
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)

# returns True because z is the same object as x

print(x is y)

# returns False because x is not the same object as y, even if they have the same content

print(x == y)

# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y
# 3
print((6 + 3) - (6 + 3))
# 4
print(100 + 5 * 3)
# 5
print(5 + 4 - 7 + 3)