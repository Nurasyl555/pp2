import re

txt = "The rain in Spain"

#Возвращает совпадение, при котором строка содержит любые символы слова (символы от a до Z, цифры от 0 до 9 и символ подчеркивания _).

x = re.findall("\w", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")