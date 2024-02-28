import re
text = "He is the Kind in the North"
x = re.findall(r"[A-Z][a-z]+", text)
print(x)