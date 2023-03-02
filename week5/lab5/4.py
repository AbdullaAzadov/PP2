import re

txt = input()
find = '[A-Z][a-z]+'
a = re.findall(find, txt)

print(a)