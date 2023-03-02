import re

def camelTo_snake(camelCase):
    snake_case = re.sub(r'(.)([A-Z])', r'\1_\2', camelCase)
    return snake_case.lower()
txt = input()
print(camelTo_snake(txt))