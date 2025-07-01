from math import *

t = (int)(input())
for test in range(t, 0, -1):
    cnt = 0
    n, x, m = map(float, input().split())
    while 1:
        n += n * (x / 100)
        cnt += 1
        if n >= m:
            print(cnt)
            break
