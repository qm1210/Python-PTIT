from math import *
from sys import *
from itertools import *
import re
from functools import cmp_to_key
from datetime import *

if __name__ == '__main__':
    f = open('CONTACT.in', 'r')
    a = f.read().splitlines()
    se = set()
    for x in a:
        se.add(x.strip().lower())
    arr = sorted(list(se)) 
    for x in arr:
        print(x)