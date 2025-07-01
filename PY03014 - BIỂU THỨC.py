from math import *
from sys import *
from itertools import *
import re
from functools import cmp_to_key
from datetime import *

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        t -= 1
        s = input()
        st = []
        cnt = 0
        se = set()
        for c in s:
            if c == "(":
                cnt += 1
                st.append(cnt)
                print(cnt, end=" ")
            elif c == ")":
                print(st.pop(), end=" ")
        print()