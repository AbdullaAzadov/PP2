f = open("week6/dir_file/0.txt", "r").read()

cnt = 1
for i in f:
    if i == "\n":
        cnt+= 1

print(cnt)