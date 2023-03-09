import os

dir = "C:\pp2"

if os.access(dir, os.F_OK):
    print("Path is found")
if os.access(dir, os.R_OK):
    print("Path is readable")
if os.access(dir, os.W_OK):
    print("Path is writable")
