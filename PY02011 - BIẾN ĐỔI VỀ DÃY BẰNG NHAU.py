from math import *

if __name__ == '__main__':
    n = int(input())
    res = []
    a = list(map(int, input().split()))
    for i in range(n):
        cnt = 0
        for j in range(n):
            cnt += abs(a[i] - a[j])
        res.append(cnt)
    min_val = min(res)
    i = res.index(min_val)
    print(min_val, a[i], sep=' ')

