from itertools import permutations 

def perm(string):
    p = permutations(string)
    for i in p:
        print(''.join(i))


string = input("Type a string: ")
perm(string)
