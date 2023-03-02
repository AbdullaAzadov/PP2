import re

txt = input()
find = r'ab{2}|b{3}'
a = re.search(find, txt)

print(a)