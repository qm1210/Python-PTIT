from math import *
from sys import *
from itertools import *
import re
from functools import cmp_to_key
from datetime import *

if __name__ == '__main__':
    t = int(input())
    current = ""
    mp = {}
    data = []
    while t > 0:
        t -= 1
        s = input()
        data.append(s)
        for line in data:
            if line == "":
                current = ""
                continue
            if current == "":
                current = line
                mp[current] = 0
            else:
                mp[current] += 1
    for x in mp:
        print(x, mp[x], sep=": ")