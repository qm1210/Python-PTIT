from math import *

if __name__ == '__main__':
    n, k = map(int, input().split())
    res = []
    cnt = 0
    for i in range(10 ** (k - 1), 10 ** k):
        ucln = gcd(i, n)
        if ucln == 1:
            res.append(i)
    for i in range(0, len(res), 10):
        print(" ".join(map(str, res[i : i + 10])))