import re

txt = "The rain in Spain"

#Проверьте, присутствует ли "ain" в начале СЛОВА:

x = re.findall(r"ain\b", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
