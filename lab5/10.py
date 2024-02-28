import re

text = "WhenYouPlayTheGameOfThrones,YouWinOrYouDie"
result = re.sub(r'(?<=[a-z])(?=[A-Z])', r'_' , text)
print(result)