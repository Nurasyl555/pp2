import re

txt = "The rain in Spain"

#Возвращает совпадение для каждого символа без цифр:

x = re.findall("\D", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
