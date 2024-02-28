import re
text = "When You-Play The.Game,OfThrones,YouWinOrYouDie"
x = re.sub(r"[ -.,]", ":", text)

print(x)