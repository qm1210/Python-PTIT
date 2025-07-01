from math import *
from sys import *
from itertools import *
from functools import cmp_to_key
from datetime import *
import re
import sys
from heapq import *

prime = [True] * 1000001
prime[0] = prime[1] = False

def sieve():
    for i in range(2, 1000001):
        if prime[i]:
            for j in range(i + i, 1000001, i):
                prime[j] = False

if __name__ == '__main__':
    sieve()
    n, x = map(int, input().split())
    res = [x]
    i = x + 1
    nt = []
    for i in range(len(prime)):
        if prime[i]:
            nt.append(i)
    for i in range(n):
        res.append(x + nt[i])
        x += nt[i]
    print(*res)