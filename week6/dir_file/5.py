import os

dir = "C:\pp2\week6\dir_file"

list = [True, 15, 35, 3.156, "djksahds"]

if not os.path.isfile(dir + "\list.txt"):
    file = open(dir + "\list.txt", "x")
    file.write((str(list)))
else:
    file = open(dir + "\list.txt", "w")
    file.write(str(list))