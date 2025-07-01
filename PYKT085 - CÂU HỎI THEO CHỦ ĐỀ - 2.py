from math import *
from collections import *
import re
import sys

if __name__ == '__main__':
    t = int(input())
    data = []
    current = ""
    mp = {}
    while t > 0:
        t -= 1
        data.append(input())
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
            