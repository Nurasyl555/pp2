import os
paths = r"C:\Users\noutstorekz\Desktop\githowto\repositories\work\lab6\lecture"
for i in range(26):
    name_file = chr(65 + i)
    x = os.path.join(paths, name_file)
    os.mkdir(x)