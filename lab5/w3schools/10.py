import re
#{} Точно указанное количество вхождений
txt = "hello planet"
x = re.findall("he.{2}o", txt)
