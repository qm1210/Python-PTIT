from math import isqrt

prime = [True] * 100001
prime[0] = prime[1] = False

def sieve():
    for i in range(2, isqrt(100000) + 1):
        if prime[i]:
            for j in range(i * i, 100001, i):
                prime[j] = False

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    sieve()
    max_cnt = 0
    for i in range(len(a)):
        cnt = 0
        if prime[a[i]]:
            cnt += 0
        else:
            l, r = 0, 0
            x, y = a[i], a[i]
            while not prime[x]:
                x -= 1
                l += 1
            while not prime[y]:
                y += 1
                r += 1
            cnt += min(l, r)
            if cnt > max_cnt:
                max_cnt = cnt
    print(max_cnt)
