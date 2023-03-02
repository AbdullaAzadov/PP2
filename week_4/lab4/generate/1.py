def square(n):
    for i in range(n+1):
        yield i**2

num = int(input())
for i in square(num):
    print(i)