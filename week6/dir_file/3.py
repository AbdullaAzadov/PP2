import os

dir = "C:\pp2"

if os.path.isdir(dir):
    if os.path.exists("week6"):
        print("week6 is acces")
    if os.path.exists("tmp.txt"):
        print('file "tmp.txt" is exist')