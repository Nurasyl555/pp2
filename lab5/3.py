import re
text = "abf_gd gjd_fgkd"
x = re.findall(r"[a-z]+_[a-z]+", text)
print(x)