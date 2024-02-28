import re

txt = "The rain in Spain"

#Возвращает совпадение для каждого символа, содержащего пробел:

x = re.findall("\s", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
