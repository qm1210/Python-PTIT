from math import *
from sys import *
from itertools import *
from functools import cmp_to_key
from datetime import *
import re
import sys

def check(s1):
    s2 = s1[::-1]
    for i in range(1, len(s1)):
        if abs(ord(s1[i]) - ord(s1[i - 1])) != abs(ord(s2[i]) - ord(s2[i - 1])):
            return False
    return True

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t -= 1
        s1 = input()
        if check(s1):
            print("YES")
        else:
            print("NO")
