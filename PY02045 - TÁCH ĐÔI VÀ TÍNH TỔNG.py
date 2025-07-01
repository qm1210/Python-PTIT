from math import *

if __name__ == '__main__':
    s = input()
    l = len(s)
    while l > 1:
        left = s[:l//2]
        right = s[l//2:]
        total = int(left) + int(right)
        s = str(total)
        l = len(s)
        print(s)
