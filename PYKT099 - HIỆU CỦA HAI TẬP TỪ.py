from math import *
from sys import *
from itertools import *
import re
from functools import cmp_to_key
from datetime import *

if __name__ == '__main__':
    f = open('DATA1.in', 'r')
    s = f.read()
    a = s.split()
    for i in range(len(a)):
        a[i] = a[i].lower()
    se1 = set(a)
    f = open('DATA2.in', 'r')
    s = f.read()
    a = s.split()
    for i in range(len(a)):
        a[i] = a[i].lower()
    se2 = set(a)
    res1 = list(se1 - se2)
    res2 = list(se2 - se1)
    res1.sort()
    res2.sort()
    print(*res1)
    print(*res2)