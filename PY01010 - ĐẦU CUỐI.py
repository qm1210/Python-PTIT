from math import *

t = int(input())
while t > 0:
    t -= 1
    s = str(input())
    first = int(s[:2])
    last = int(s) % 100
    if first == last:
        print("YES")
    else:
        print("NO")
    