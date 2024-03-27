import sys
import math
import heapq

input = sys.stdin.readline


def inp():
    return (int(input()))
def inlt():
    return (list(map(int, input().split())))
def insr():
    s = input()
    return (list(s[:len(s) - 1]))
def invr():
    return (map(int, input().split()))


MOD = 10 ** 9 + 7
MAXN = 2 * 10 ** 5 + 5

fac = [1] * MAXN
inv_fac = [1] * MAXN

for i in range(1, MAXN):
    fac[i] = fac[i - 1] * i % MOD
inv_fac[MAXN - 1] = pow(fac[MAXN - 1], -1, MOD)
for i in range(MAXN - 2, -1, -1):
    inv_fac[i] = inv_fac[i + 1] * (i + 1) % MOD


def combination(n, k):
    return (fac[n] * inv_fac[k] % MOD) * inv_fac[n - k] % MOD


def permutation(n, k):
    return fac[n] * inv_fac[n - k] % MOD


t = inp()
for i in range(t):
    n, m1, m2 = inlt()
    p = inlt()
    s = inlt()
    if p[0] != 1 or p[-1] != s[0] or s[-1] != n:
        print(0)
        continue

    ans = combination(n - 1, p[-1] - 1)

    remain = p[-1] - 1
    for i in range(m1-2, -1, -1):
        remain -= 1
        k = p[i + 1] - p[i] - 1
        ans = ans * permutation(remain, k) % MOD
        remain -= k

    remain = n - s[0]
    for i in range(m2 - 1):
        remain -= 1
        k = s[i + 1] - s[i] - 1
        ans = ans * permutation(remain, k) % MOD
        remain -= k

    print(ans)

