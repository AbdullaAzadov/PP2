def squares(a, b):
    for i in range(a, b+1):
        yield i**2

a = int(input())
b = int(input())

if a <= b:
    for i in squares(a, b):
        print(i)
else:
    for i in squares(b, a):
        print(i)
        
