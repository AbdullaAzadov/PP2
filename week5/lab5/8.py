import re

txt = input()
find = '[A-Z][^A-Z]*'

a = re.findall(find, txt)

print(a)