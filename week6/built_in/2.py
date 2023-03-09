txt = input()

u = 0
l = 0

for i in range[len(txt)]:
    if txt[i].isupper():
        u+= 1
    if txt[i].islower():
        l+= 1

print("Uppercase letters:", u)
print("Lowercase letters:", l)