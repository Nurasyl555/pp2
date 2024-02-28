import re 
txt = "hello planet"
x = re.findall("he.*", txt)
print(x)