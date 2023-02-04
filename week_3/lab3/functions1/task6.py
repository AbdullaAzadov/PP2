def reversed_sentence(list):
    list.reverse()
    for i in list:
        print(i, end=' ')

list = input().split()
reversed_sentence(list)