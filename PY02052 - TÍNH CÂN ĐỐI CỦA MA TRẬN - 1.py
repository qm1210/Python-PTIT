from math import *
import sys

if __name__ == '__main__':
    n = int(input())
    a = []
    for i in range(n):
        row = list(map(int, input().split()))
        a.append(row)
    k = int(input())
    sum_above, sum_below = 0, 0
    for i in range(n):
        for j in range(n):
            if j > i:
                sum_above += a[i][j]
            if j < i:
                sum_below += a[i][j]
    tmp = abs(sum_above - sum_below)
    if tmp <= k:
        print("YES")
    else:
        print("NO")
    print(tmp)