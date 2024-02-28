import re
txt = "The rain in Spain"
#Найдите все строчные символы в алфавитном порядке между "a" и "m".:
x = re.findall("[a-z]", txt)
print(x)