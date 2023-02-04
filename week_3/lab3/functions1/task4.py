def is_prime(number):
    for i in range(2, int((number)**0.5) + 1):
        if number % i == 0:
            return False

    return number > 1

list = input('Enter some integers: ').split()
result = []

for number in list:
    if is_prime(int(number)) == True:
        result.append(int(number))

print(result)        