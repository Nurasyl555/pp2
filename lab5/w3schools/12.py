import re

txt = "The rain in Spain"

#Проверьте, присутствует ли "ain", но не в начале слова:

x = re.findall(r"\Bain", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
