from math import *

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t -= 1
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        a.sort()
        b.sort()
        check = 1
        for i in range(len(a)):
            if a[i] > b[i]:
                check = 0
                break
        if check == 1:
            print("YES")
        else:
            print("NO")