from math import *
import sys
from itertools import *
import re
from functools import cmp_to_key

if __name__ == '__main__':
    s = input()
    perms = list(permutations(s))
    for x in perms:
        print("".join(x))


