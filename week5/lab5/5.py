import re

txt = input()
find = 'a.*b$'
a = re.findall(find, txt)

print(a)