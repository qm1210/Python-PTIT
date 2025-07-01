MOD = 10**9 + 7

def power(a, b):
    res = 1
    a %= MOD
    while b:
        if b & 1:
            res = res * a % MOD
        a = a * a % MOD
        b >>= 1
    return res

def inv(a):
    return power(a, MOD - 2)

def sum_pows(n, k):
    if n <= k + 2:
        res = 0
        for i in range(1, n + 1):
            res = (res + power(i, k)) % MOD
        return res

    y = [0] * (k + 3)
    for i in range(1, k + 3):
        y[i] = (y[i-1] + power(i, k)) % MOD

    def lagrange(x, y, n):
        k = len(x) - 1
        res = 0

        fact = [1] * (k + 2)
        for i in range(1, k + 2):
            fact[i] = fact[i - 1] * i % MOD

        inv_fact = [1] * (k + 2)
        inv_fact[k + 1] = inv(fact[k + 1])
        for i in range(k, -1, -1):
            inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD

        for i in range(k + 1):
            xi, yi = x[i], y[i]
            num = 1
            den = 1
            for j in range(k + 1):
                if i != j:
                    num = num * (n - x[j]) % MOD
                    den = den * (x[i] - x[j]) % MOD
            res = (res + yi * num % MOD * inv(den)) % MOD
        return res

    x = [i for i in range(k + 2 + 1)]
    return lagrange(x, y, n)

T = int(input())
for _ in range(T):
    n, k = map(int, input().split())
    print(sum_pows(n, k))