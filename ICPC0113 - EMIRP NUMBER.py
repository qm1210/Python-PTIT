from math import *
from sys import *
from itertools import *
from functools import cmp_to_key
from datetime import *
import re
import sys

prime = [True] * 1000001
prime[0] = prime[1] = False

def sieve():
    for i in range(2, 1000001):
        if prime[i]:
            for j in range(i + i, 1000001, i):
                prime[j] = False

if __name__ == '__main__':
    t = int(input())
    sieve()
    while t > 0:  
        t -= 1
        n = int(input())
        dd = [0] * 1000001
        res = []
        for i in range(n):
            rev = int(str(i)[::-1])
            if i != rev and dd[i] == 0:
                if prime[i] and prime[rev] and i < n and rev < n:
                    res.append(i)
                    res.append(rev)
                    dd[i] = 1
                    dd[rev] = 1
        print(*res)
