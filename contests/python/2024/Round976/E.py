import bisect
import collections
import sys
import heapq
import math

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


def solution():
    n = inp()
    a = inlt()
    p = inlt()
    dp = [0] * 1024
    dp_nxt = [0] * 1024
    dp[0] = 1
    for i in range(n):
        ai, pi = a[i], p[i]
        npi = 10000 - pi
        for i in range(1024):
            dp_nxt[i] = (dp[i] * npi) % MOD
        for i in range(1024):
            dp_nxt[i ^ ai] += dp[i] * pi
            dp_nxt[i ^ ai] %= MOD
        dp, dp_nxt = dp_nxt, dp

    down = pow(10000, -n, MOD)
    ans = 0
    for i in range(1024):
        ans += i * i * dp[i] * down
        ans %= MOD
    print(ans)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
