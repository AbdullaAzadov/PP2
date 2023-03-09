dir = "C:/pp2/week6/dir_file/alph"

for i in range(65, 91):
    open(dir + "/{}.txt".format(chr(i)), 'w')