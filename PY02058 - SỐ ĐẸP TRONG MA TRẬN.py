from math import *
import sys

if __name__ == '__main__':
    n, m = map(int, input().split())
    a = []
    check = False
    for i in range(n):
        row = list(map(int, input().split()))
        a.append(row)
    min_value, max_value = 10001, -1
    for i in range(n):
        for j in range(m):
            if a[i][j] > max_value:
                max_value = a[i][j]
            if a[i][j] < min_value:
                min_value = a[i][j]
    tmp = max_value - min_value
    for i in range(n):
        for j in range(m):
            if a[i][j] == tmp and check == False:
                check = True
                print(tmp)
            if a[i][j] == tmp:
                print(f"Vi tri [{i}][{j}]")
    if check == False:
        print("NOT FOUND")
