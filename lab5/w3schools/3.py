import re
txt = "That wiil be 59 dollors"
#Найдите все цифровые символы:
x = re.findall("\d", txt)
print(x)