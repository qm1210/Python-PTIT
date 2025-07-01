from math import *

def check(a):
    for i in range(1, len(a)):
        if a[i] != a[0]:
            return False
    return True

if __name__ == '__main__':
    while True:
        a = list(map(int, input().split()))
        if a == [0, 0, 0, 0]:
            break
        cnt = 0
        while len(set(a)) > 1:
            b = [abs(a[i] - a[i + 1]) for i in range(3)]
            b.append(abs(a[3] - a[0]))
            cnt += 1
            a = b
        print(cnt)
