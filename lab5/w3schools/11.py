import re
txt = "the rain in Spain falls mainly in the plain"
##Проверьте, содержит ли строка либо "falls", либо "stays".:
x = re.findall("falls|stays", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
