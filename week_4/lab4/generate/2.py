def g(n):
    for i in range(n+1):
        yield i

num = int(input())
for i in g(num):
    print(i)