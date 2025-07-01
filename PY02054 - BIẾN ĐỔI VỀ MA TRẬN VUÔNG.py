from math import *
import sys

if __name__ == '__main__':
    n, m = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        row = list(map(int, input().split()))
        a.append(row)
    if n > m:
        l = n - m
        cnt = 0
        for i in range(n):
            row = a[i]
            if cnt < l and (i + 1) % 2 == 1:
                cnt += 1
                continue
            b.append(row)
        for i in range(m):
            print(*b[i])
    elif m > n:
        l = m - n
        for i in range(n):
            cnt = 0
            row = []
            for j in range(m):
                if cnt < l and (j + 1) % 2 == 0:
                    cnt += 1
                    continue
                row.append(a[i][j])
            b.append(row)
        for i in range(n):
            print(*b[i])
    else:
        for i in range(n):
            print(*a[i])
