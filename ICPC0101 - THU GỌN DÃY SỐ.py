from math import *
from sys import *
from itertools import *
from functools import cmp_to_key
from datetime import *
import re
import sys

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    st = [a[0]]
    for i in range(1, n):
        st.append(a[i])
        if len(st) > 1 and (st[-2] + st[-1]) % 2 == 0:
            st.pop()
            st.pop()
    print(len(st))