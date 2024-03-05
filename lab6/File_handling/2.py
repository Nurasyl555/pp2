import os
paths = r"C:\Users\noutstorekz\Desktop\githowto\repositories\work\lab6\lecture"
# os.R_OK для проверки чтения,
print(os.access(paths, os.R_OK))
#os.W_OK для записи
print(os.access(paths, os.W_OK))
#os.X_OK для исполнения
print(os.access(paths, os.X_OK))