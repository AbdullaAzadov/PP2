def solve(numheads, numlegs):
    # formula - 2r + (numheads - r) * 4 = numlegs
    # formula - c = numheads - r
    rabbits = ((numheads*4) - numlegs)/2
    chicken = numheads - rabbits
    return rabbits, chicken

numheads = int(input("How many heads: "))
numlegs = int(input("How many legs: "))

r, c = solve(numheads, numlegs)

if r < 0 or c < 0:
    print("Wrong input")
    exit()

print(r, "rabbits and", c, "chickens")