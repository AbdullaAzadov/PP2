def Histogram(list):
    for number in list:
        for i in range(0, int(number)):
            print('*', end='')
        print('')    

list = input().split()
Histogram(list)            