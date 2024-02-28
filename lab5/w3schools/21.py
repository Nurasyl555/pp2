import re
#Возвращает совпадение, при котором строка НЕ содержит никаких символов word 
txt = "The rain in Spain"
x = re.findall("\W", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")