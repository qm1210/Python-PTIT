from math import *

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t -= 1
        n = int(input())
        res = ["1"]
        for i in range(2, int(sqrt(n)) + 1):
            cnt = 0
            while n % i == 0:
                n //= i
                cnt += 1
            if cnt > 0:
                res.append(f"{i}^{cnt}")
        if n > 1:
            res.append(f"{n}^1")
        print(" * ".join(map(str, res)))
        
