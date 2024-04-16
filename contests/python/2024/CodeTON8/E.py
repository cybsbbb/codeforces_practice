import heapq
import sys

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


MOD = 998244353
MAXN = 2 * 10 ** 6 + 5

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
for _ in range(t):
    l, n = inlt()
    ans = 2 * combination(l, 2 * n) % MOD
    for s in range(0, l - 2 * n + 1, 2):
        ans = (ans - (combination(s // 2 + n - 1, n - 1) % MOD) * 2 * combination(l - s - n, n) % MOD) % MOD

    print(ans)
