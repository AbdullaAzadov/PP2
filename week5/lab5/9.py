import re

txt = input()
find = r"(\w)([A-Z])"
replace = r"\1 \2"

a = re.sub(find, replace, txt)
print(a)