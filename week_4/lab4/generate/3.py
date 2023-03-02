def g(a):
    for i in range(a):
        if i % 3 == 0 and i % 4 == 0:
            yield i

num = int(input())
for i in g(num):
    print(i)