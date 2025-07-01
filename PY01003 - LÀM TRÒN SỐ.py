from math import *

t = int(input())
while t > 0:
    t -= 1
    n = list(input())
    for i in range(len(n) - 1, 0, -1):
        if int(n[i]) >= 5:
            tmp = int(n[i - 1]) + 1
            n[i - 1] = str(tmp)
        n[i] = '0'            
    kq = int(''.join(n))
    print(kq)