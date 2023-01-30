x = "awesome" # x is global variable

def myfunc():
  print("Python is " + x)

myfunc()

def myfunc2():
    y = 'good'
    print("Python is " + y) # y is a local var

myfunc2()    

