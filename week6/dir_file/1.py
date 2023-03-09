import os

dir = "C:\pp2"

print("Only directories:")
for i in os.listdir(dir):
    if os.path.isdir(os.path.join(dir, i)):
        print(i, end=" ")
        
print("\n\nOnly files:")
for i in os.listdir(dir):
    if not os.path.isdir(os.path.join(dir, i)):
        print(i, end=" ")

print("\n\n All in direction:")
for i in os.listdir(dir):
    print(i, end=" ")

