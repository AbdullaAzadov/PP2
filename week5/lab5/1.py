import re

txt = input()
find = r'ab*'
a = re.search(find, txt)

print(a)