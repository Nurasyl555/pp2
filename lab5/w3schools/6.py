import re

txt = "hello planet"

#Проверьте, заканчивается ли строка на 'планета

x = re.findall("planet$", txt)
if x:
  print("Yes, the string ends with 'planet'")
else:
  print("No match")
