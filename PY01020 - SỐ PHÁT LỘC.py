from math import *

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t -= 1
        n = int(input())
        if n % 100 == 86:
            print("YES")
        else:
            print("NO")