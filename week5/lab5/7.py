import re

def snake_toCamel(snake_case):
    list = re.split('_', snake_case)
    camelCase = ''
    for i in list:
        if i != list[0]:
            i = i[0].upper() + i[1:]
        camelCase+= i
    return camelCase
txt = input()
print(snake_toCamel(txt))