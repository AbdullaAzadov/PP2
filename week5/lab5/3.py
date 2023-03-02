import re

txt = input()
find = '[a-z]+_[a-z]+'
a = re.findall(find, txt)

print(a)