def OuncesToGrams(grams):
    ounces = 28.3495231 * grams
    return ounces

grams = float(input("How many grams do you need ?: "))
print("It will be", OuncesToGrams(grams), "ounces")