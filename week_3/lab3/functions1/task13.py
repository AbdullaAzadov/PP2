import random

def guess(name):
    num = random.randint(1, 20)
    tried = 0
    input_num = 0
    while input_num != num:
        print("Take a guess.")
        input_num = int(input())
        tried+= 1
        
        if input_num < num:
            print("\nYour guess is too low.")
        elif input_num > num:
            print("\nYour guess is too high.")
    print("Good job, " + name + "! You guessed my number in " + str(tried) +" guesses!")                


print("Hello! What is your name?")
name = input()
print("\nWell, " + name + ", I am thinking of a number between 1 and 20.")
guess(name)

