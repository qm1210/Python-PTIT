from math import *
import sys

if __name__ == '__main__':
    n, m = map(int, input().split())
    a = []
    res = []
    max_val = -1
    min_val = 10001
    for i in range(n):
        row = list(map(int, input().split()))
        a.append(row)
    check = False
    for i in range(n):
        for j in range(m):
            if max_val < a[i][j]:
                max_val = a[i][j]
            if min_val > a[i][j]:
                min_val = a[i][j]
    tmp = max_val - min_val
    for i in range(n):
        for j in range(m):
            if a[i][j] == tmp and check == False:
                print(tmp)
                check = True
            if a[i][j] == tmp:
                print(f"Vi tri [{i}][{j}]")
    if check == False:
        print("NOT FOUND")
    