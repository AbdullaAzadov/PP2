# tuple
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

# changing elements 
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

print("")

# unpacking elements
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)