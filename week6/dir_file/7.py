dir = "C:/pp2/week6/dir_file/"

copy = open(dir + "copy.txt", 'r').read()
paste = open(dir + "paste.txt", 'w').write(copy)