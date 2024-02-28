import re
txt = "hello planet"
#Любой символ (кроме символа новой строки)
x = re.findall("he..o", txt)
print(x)