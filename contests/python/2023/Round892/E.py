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


def solution():
    n, k = inlt()
    a = inlt()
    b = inlt()
    dp = [[0] * (k+1) for i in range(n+1)]
    # -a + b
    dp1 = [-10**18] * (n+1)
    # a + b
    dp2 = [-10**18] * (n + 1)
    # -a - b
    dp3 = [-10**18] * (n + 1)
    # a - b
    dp4 = [-10**18] * (n + 1)
    for i in range(n+1):
        for j in range(min(i, k)+1):
            if i != 0:
                dp[i][j] = dp[i-1][j]
            diag_val = i - j
            if i != 0:
                dp[i][j] = max(dp[i][j], - a[i - 1] + b[i - 1] + dp1[diag_val])
                dp[i][j] = max(dp[i][j], + a[i - 1] + b[i - 1] + dp3[diag_val])
                dp[i][j] = max(dp[i][j], - a[i - 1] - b[i - 1] + dp2[diag_val])
                dp[i][j] = max(dp[i][j], + a[i - 1] - b[i - 1] + dp4[diag_val])
            if i != n:
                dp1[diag_val] = max(dp1[diag_val], dp[i][j] - a[i] + b[i])
                dp2[diag_val] = max(dp2[diag_val], dp[i][j] + a[i] + b[i])
                dp3[diag_val] = max(dp3[diag_val], dp[i][j] - a[i] - b[i])
                dp4[diag_val] = max(dp4[diag_val], dp[i][j] + a[i] - b[i])

    print(dp[-1][-1])

    return 0


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
