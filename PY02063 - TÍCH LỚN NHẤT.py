from math import *

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    m1 = a[-1] * a[-2]
    m2 = a[-1] * a[-2] * a[-3]
    m3 = a[0] * a[1]
    m4 = a[0] * a[1] * a[-1]
    max_val = max(m1, m2, m3, m4)
    print(max_val)