from functools import cmp_to_key
from math import *
from collections import *

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t -= 1
        n = int(input())
        a = list(map(int, input().split()))
        res = [0] * n
        st = []
        for i in range(n):
            while st and a[st[-1]] <= a[i]:
                st.pop()
            if not st:
                res[i] = i + 1
            else:
                res[i] = i - st[-1]
            st.append(i)
        print(*res)