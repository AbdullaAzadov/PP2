def FtoC(F):
    C = (5/9) * (F-32)
    return C

F = float(input('How many farrenheit: '))
print("It will be", round(FtoC(F), 1), "in celsius")