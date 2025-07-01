from math import *
from sys import *
from itertools import *
import re
from functools import cmp_to_key
from datetime import *

if __name__ == '__main__':
    s = input()
    cnt = 0
    if len(s) <= 1:
        print(1)
    else:
        while len(s) > 1:
            tmp = 0
            for c in s:
                tmp += ord(c) - ord('0')
            s = str(tmp)
            cnt += 1
        print(cnt)