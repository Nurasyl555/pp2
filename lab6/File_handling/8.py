import os
name_file = input("write file: ")
pathss = r"C:\Users\noutstorekz\Desktop\githowto\repositories\work\lab6"
paths = os.path.join(paths, name_file)
try:
    if os.path.exists(paths) and os.access(paths, os.X_OK):
        os.remove(paths)
except:
    print("mistake")