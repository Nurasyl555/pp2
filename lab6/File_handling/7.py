import shutil
paths = r"C:\Users\noutstorekz\Desktop\githowto\repositories\work\lab6\lecture\fff.txt"
try:
    shutil.copyfile(paths, r"C:\Users\noutstorekz\Desktop\githowto\repositories\work\lab6\demo.txt")
except:
    print("Ошибка")
    