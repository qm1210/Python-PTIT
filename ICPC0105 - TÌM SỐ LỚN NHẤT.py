from math import *
import sys
from itertools import combinations
import re
from functools import cmp_to_key

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t -= 1
        s = input()
        numbers = re.findall(r'\d+', s)
        numbers = list(map(int, numbers))
        print(max(numbers))
