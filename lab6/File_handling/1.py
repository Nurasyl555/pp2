import os
paths = r"C:\Users\noutstorekz\Desktop\githowto\repositories\work\lab6\lecture"
list_path = os.listdir(paths)
#print(os.listdir(paths))
# directory
for i in list_path:
    if os.path.isdir(os.path.join(paths, i)):
        print(i)
# file
print("file")
for i in list_path:
    if os.path.isfile(os.path.join(paths, i)):
        print(i)