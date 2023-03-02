def g(a):
    while a >= 0:
        yield a
        a-= 1

num = int(input())
for i in g(num):
    print(i)