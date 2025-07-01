from math import *

if __name__ == '__main__':
    n = int(input())
    cnt = 0
    a = list(map(int, input().split()))
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if a[i] > a[j]:
                cnt += 1
    print(cnt)