import re
import json
txt = open("row.txt", "r", encoding="UTF-8")
txt1 = txt.read()
text2 = "Grand theft autob"
#x = re.findall(r"ab*", text2)
y = re.findall("ab*", txt1)
print(y)