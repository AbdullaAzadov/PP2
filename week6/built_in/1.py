list = [1, "2", 3, '4', 5.5]

res = float(list[0])
for i in range(1, len(list)):
    res*= float(list[i])

print(res)