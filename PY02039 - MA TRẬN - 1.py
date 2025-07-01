from functools import cmp_to_key
from math import *

if __name__ == '__main__':
    n = int(input())
    a = []
    for i in range(n):
        row = list(map(int, input().split()))
        a.append(row)
    k = int(input())
    sumTren = 0
    sumDuoi = 0
    for i in range(n):
        for j in range(n):
            if j > i:
                sumTren += a[i][j]
            elif j < i:
                sumDuoi += a[i][j]
    sum = abs(sumTren - sumDuoi)
    check = 0
    if sum <= k:
        check = 1
    else:
        check = 0
    if check == 1:
        print("YES")
    else:
        print("NO")
    print(sum)

