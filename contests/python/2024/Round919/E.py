import collections
import sys
import heapq
from functools import cache

sys.setrecursionlimit(50000)

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

# dp[i][j] (last element j, sum is i)
# dp[i][j] = SUM(1<= p <= min(i/p, k - j + 1)) dp[i - j * p][p]

def solution():
    n, k = inlt()
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(1, k + 1):
        dp[0][i] = 1

    for i in range(1, n+1):
        for j in range(1, k + 1):
            if i == j:
                dp[i][j] = 1
                continue
            for p in range(1, min(i // j, k - j + 1) + 1):
                dp[i][j] += dp[i - p * j][p]
                dp[i][j] %= MOD
    ans = 0
    for j in range(1, k+1):
        ans += dp[n][j]
        ans %= MOD
    print(ans)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
