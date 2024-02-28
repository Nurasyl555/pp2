import re
text = 'GHHSS ds aaab fffdddaab'
x = re.findall("a.*b", text)
print(x)