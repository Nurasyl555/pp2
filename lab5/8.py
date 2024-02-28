import re

text = "WhenYouPlayTheGameOfThrones,YouWinOrYouDie"
result = re.split(r'(?<=[a-z])(?=[A-Z])', text)
print(result)