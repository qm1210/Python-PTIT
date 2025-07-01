from math import *

if __name__ == '__main__':
    n = int(input())
    a = list(map(float, input().split()))
    a.sort()
    min = a[0]
    max = a[-1]
    b = []
    for i in range(len(a)):
        if a[i] != min and a[i] != max:
            b.append(a[i])
    avg = sum(b) / len(b)
    print("%.2f" % avg)