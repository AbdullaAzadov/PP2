import os
dir = "C:/pp2/week6/dir_file/"

if os.path.isfile(dir + "deleteMe.txt"):
    os.remove(dir + "deleteMe.txt")
else:
    # to create file again
    open(dir + "deleteMe.txt", "w")