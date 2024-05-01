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


t = inp()
for _ in range(t):
    n, k = inlt()
    a = inlt()
    dp = [[0] * (k + 1) for i in range(n + 1)]
    dp[0][0] = 0
    for i in range(n):
        dp[i][0] = dp[i - 1][0] + a[i]

    for j in range(1, k + 1):
        for i in range(n):
            dp[i][j] = dp[i - 1][j] + a[i]
            for k in range(1, j + 1):
                if i - k < 0:
                    break
                dp[i][j] = min(dp[i][j], dp[i - k - 1][j - k] + min(a[i - k: i + 1]) * (k + 1))
    print(dp[n - 1][k])
