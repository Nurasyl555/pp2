import re
txt = "hello planet"
#Проверьте, начинается ли строка с 'hello':
x = re.findall("^hello", txt)
if x:
    print("Yes, the string starts with 'hello'")
else:
  print("No match")