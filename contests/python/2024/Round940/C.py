import collections
import sys
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
# MAXN = 3 * 10 ** 5 + 5
#
# fac = [1] * MAXN
# inv_fac = [1] * MAXN
# for i in range(1, MAXN):
#     fac[i] = fac[i - 1] * i % MOD
# inv_fac[MAXN - 1] = pow(fac[MAXN - 1], -1, MOD)
# for i in range(MAXN - 2, -1, -1):
#     inv_fac[i] = inv_fac[i + 1] * (i + 1) % MOD
# def combination(n, k):
#     return (fac[n] * inv_fac[k] % MOD) * inv_fac[n - k] % MOD
# def permutation(n, k):
#     return fac[n] * inv_fac[n - k] % MOD


def solution():
    n, k = inlt()
    empty = n
    for i in range(k):
        ri, ci = inlt()
        if ri != ci:
            empty -= 2
        else:
            empty -= 1
    dp = [0] * max(3, empty + 1)
    dp[0] = 1
    dp[1] = 1
    dp[2] = 3
    for i in range(3, empty + 1):
        dp[i] = (dp[i - 1] + dp[i - 2] * 2 * (i - 1)) % MOD
    print(dp[empty] % MOD)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
