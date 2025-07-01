from math import *
import sys

def tn(n):
    s = str(n)
    if len(s) < 2:
        return False
    if s != s[::-1]:
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
            if tn(a[i][j]) and max_val < a[i][j]:
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
    