import time, math

num = float(input())
ms = int(input())

time.sleep(ms / 1000)
print("Square root of {} after {} miliseconds is {}".format(num, ms, math.sqrt(num)))