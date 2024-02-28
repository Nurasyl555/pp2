import re
text = "When_you_play_the_game_of_thrones,_you_win_or_you_die"
x = re.sub(r"_[a-z]", lambda y: y.group(0)[1].upper(), text)
print(x)