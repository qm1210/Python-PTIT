from math import *

if __name__ == '__main__':
    n = int(input())
    cnt = 0
    a = list(map(int, input().split()))
    for i in range(0, len(a) - 1):
        if a[i] != a[i + 1]:
            cnt += 1
    print(cnt)