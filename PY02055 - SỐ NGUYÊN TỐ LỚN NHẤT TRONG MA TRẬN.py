from math import *
import sys

def nt(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    n, m = map(int, input().split())
    a = []
    res = []
    max_val = -1
    for i in range(n):
        row = list(map(int, input().split()))
        a.append(row)
    check = False
    for i in range(n):
        for j in range(m):
            if nt(a[i][j]) and max_val < a[i][j]:
                max_val = a[i][j]
                check = True
    if check == False:
        print("NOT FOUND")
    else:
        print(max_val)
        for i in range(n):
            for j in range(m):
                if a[i][j] == max_val:
                    print(f"Vi tri [{i}][{j}]")
    