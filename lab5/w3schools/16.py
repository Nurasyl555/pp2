import re

txt = "The rain in Spain"

#Проверьте, содержит ли строка какие-либо цифры (числа от 0 до 9)

x = re.findall("\d", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
