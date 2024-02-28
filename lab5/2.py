import re
txt = open("row.txt", "r", encoding="UTF-8")
txt1 = txt.read()
text = "Tomb raiderabbb"
x = re.findall("ab{2,3}", text)
y = re.findall("ab{2,3}", txt1)
print(x)
print(y)