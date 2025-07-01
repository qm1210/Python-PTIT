from math import *
from functools import cmp_to_key
from itertools import permutations

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        t -= 1
        n = int(input()) 
        a = [i for i in range(1, n + 1)]
        res = sorted(permutations(a), reverse=True)
        print(len(res))
        for i in res:
            print("".join(map(str, i)), end=" ")
        print()