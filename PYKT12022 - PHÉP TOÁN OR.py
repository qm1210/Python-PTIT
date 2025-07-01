from math import *
from sys import *
from itertools import *
import re
from functools import cmp_to_key
from datetime import *

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    res = set()
    prev = set()
    for val in a:
        curr = set()
        curr.add(val)
        for x in prev:
            curr.add(x | val)
        res.update(curr)
        prev = curr
    print(len(res))
