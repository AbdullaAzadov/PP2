# sets
thisset = set(("apple", 'banana', "cherry"))
print(thisset)

print('')
# chechking element
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)

print('')
# adding a new element to set

thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)
print('')

# deleting an element

thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset) 

print('')
# pop deletes random element

thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)