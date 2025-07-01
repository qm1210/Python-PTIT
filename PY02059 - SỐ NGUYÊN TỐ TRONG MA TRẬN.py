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
    check = False
    for i in range(n):
        row = list(map(int, input().split()))
        a.append(row)
    max_val = 0
    for i in range(n):
        for j in range(m):
            if nt(a[i][j]) and a[i][j] > max_val:
                max_val = a[i][j]
    for i in range(n):
        for j in range(m):
            if a[i][j] == max_val and check == False:
                print(max_val)
                check = True
            if a[i][j] == max_val:
                print(f"Vi tri [{i}][{j}]")
    if check == False:
        print("NOT FOUND")

