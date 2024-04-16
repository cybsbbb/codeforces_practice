import sys
import math
from itertools import count

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


N = 100
dp = [[False] * (N + 1) for _ in range(N + 1)]
dp[0][0] = True


t = inp()
for i in range(t):
    n, m = inlt()
    grid = []
    for i in range(n):
        grid.append(inlt())
    start = grid[0][0]
    end = grid[-1][-1]
    gcd = math.gcd(start, end)

    def helper(x):
        for i in range(1, n):
            dp[i][0] = dp[i - 1][0] and (grid[i][0] % x == 0)
        for j in range(1, m):
            dp[0][j] = dp[0][j - 1] and (grid[0][j] % x == 0)
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = (dp[i][j - 1] or dp[i - 1][j]) and (grid[i][j] % x == 0)
        return dp[n - 1][m - 1]

    factors = []
    for i in count(1):
        if gcd % i == 0:
            factors.append(i)
            factors.append(gcd // i)
        if i * i >= gcd:
            break
    factors.sort(reverse=True)

    ans = 1
    for x in factors:
        if helper(x):
            ans = x
            break

    print(ans)
