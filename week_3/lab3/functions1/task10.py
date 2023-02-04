def unique(list):
    u = []
    for i in list:
        if i not in u:
            u.append(i)
    return u

list = input().split()
print(unique(list))