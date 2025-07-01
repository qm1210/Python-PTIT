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
        cnt = 0
        for i in range(n):
            if prime[i] and i + 6 < n:
                if prime[i + 2] and prime[i + 6]:
                    cnt += 1
                elif prime[i + 4] and prime[i + 6]:
                    cnt += 1
        print(cnt)

