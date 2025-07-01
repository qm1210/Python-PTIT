from math import *
import sys
from itertools import combinations
import re
from functools import cmp_to_key

if __name__ == '__main__':
    t = int(input())
    c = ""
    while t > 0:
        t -= 1
        d, m = map(int, input().split())
        if m == 1:
            if d >= 1 and d <= 19:
                c = "Ma Ket"
            else:
                c = "Bao Binh"
        elif m == 2:
            if d >= 1 and d <= 18:
                c = "Bao Binh"
            else:
                c = "Song Ngu"
        elif m == 3:
            if d >= 1 and d <= 20:
                c = "Song Ngu"
            else:
                c = "Bach Duong"
        elif m == 4:
            if d >= 1 and d <= 19:
                c = "Bach Duong"
            else:
                c = "Kim Nguu"
        elif m == 5:
            if d >= 1 and d <= 20:
                c = "Kim Nguu"
            else:
                c = "Song Tu"
        elif m == 6:
            if d >= 1 and d <= 20:
                c = "Song Tu"
            else:
                c = "Cu Giai"
        elif m == 7:
            if d >= 1 and d <= 22:
                c = "Cu Giai"
            else:
                c = "Su Tu"
        elif m == 8:
            if d >= 1 and d <= 22:
                c = "Su Tu"
            else:
                c = "Xu Nu"
        elif m == 9:
            if d >= 1 and d <= 22:
                c = "Xu Nu"
            else:
                c = "Thien Binh"
        elif m == 10:
            if d >= 1 and d <= 22:
                c = "Thien Binh"
            else:
                c = "Thien Yet"
        elif m == 11:
            if d >= 1 and d <= 22:
                c = "Thien Yet"
            else:
                c = "Nhan Ma"
        elif m == 12:
            if d >= 1 and d <= 21:
                c = "Nhan Ma"
            else:
                c = "Ma Ket"
        print(c)
