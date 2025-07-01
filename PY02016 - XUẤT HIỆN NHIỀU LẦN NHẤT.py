from functools import cmp_to_key
from math import *
from collections import *

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t -= 1
        n = int(input())
        a = list(map(int, input().split()))
        freq = Counter(a)
        max_val = 0
        mark = -1
        check = False
        for num, val in freq.items():
            if val > n / 2:
                if num > max_val or (val == max_val and num < mark):
                    mark = num
                    max_val = val
                    check = True
        if check:
            print(mark)
        else:
            print("NO")