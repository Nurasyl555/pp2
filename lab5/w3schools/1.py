import re
txt = "The rain in Spain"
x = re.search("^The.Spaon$", txt)
if x:
  print("YES! We have a match!")
else:
  print("No match")
print(type(x))
print(type(True))