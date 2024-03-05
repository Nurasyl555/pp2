import os
paths = r"C:\Users\noutstorekz\Desktop\githowto\repositories\work\lab6\lecture\OS import\12.py"
try:
    if os.path.exists(paths):
        x , y = os.path.split(paths)
        print("path - ")
        print(x)
        print(y)
except:
    print("неверный путь")