from math import *

if __name__ == '__main__':
    while True:
        t = int(input())
        if t == 0:
            break
        a = []
        while t > 0:
            t -= 1
            a.append(int(input()))
        min_val, max_val = min(a), max(a)
        if min_val == max_val:
            print("BANG NHAU")
        else:
            print(min_val, max_val, sep=" ")