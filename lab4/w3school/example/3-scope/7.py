x = 3000
print(x)
def myfunc():
    global x
    x = 200
    print(x)
myfunc()
print(x)