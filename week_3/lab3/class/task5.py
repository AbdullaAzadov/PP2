def isPrime(num):
    for i in range(2, int(num ** 0.5)+1):
        if num % i == 0:
            return False
    if num != 1 and num != 0:
        return True
    

list = [i for i in range(100)]
filtered_list = filter(isPrime, list)
for num in filtered_list:
    print(num, end=' ')