from math import *

def check(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    n, m = map(int, input().split())
    a = []
    for i in range(n):
        row = list(map(int, input().split()))
        a.append(row)
    for i in range(n):
        for j in range(m):
            if check(a[i][j]):
                a[i][j] = 1
            else:
                a[i][j] = 0
    for row in a:
        print(" ".join(map(str, row)))
