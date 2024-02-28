import re

txt = "The rain in Spain"

#Проверьте, присутствует ли "ain", но не в конце слова:

x = re.findall(r"ain\B", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
