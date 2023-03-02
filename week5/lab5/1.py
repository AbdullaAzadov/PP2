import re

txt = input()
find = 'ab*'
a = re.search(find, txt)

print(a)