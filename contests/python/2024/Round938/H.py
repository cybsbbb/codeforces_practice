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


t = inp()
for _ in range(t):
    n, m, k = inlt()
    g = [input() for _ in range(n)]
    dis = lambda x, y, a, b: ((x - a) ** 2 + (y - b) ** 2) ** .5
    dp = [0] * (1 << 12)

    for _ in range(k):
        i, j, p = inlt()
        i -= 1;
        j -= 1
        d = [0] * 12
        for r in range(1, 12):
            d[r] = -pow(3, r)
            for x in range(n):
                for y in range(m):
                    if g[x][y] == '#' and dis(i, j, x, y) <= r:
                        d[r] += p

        ndp = [0] * (1 << 12)
        for r in range(1, 12):
            for mask in range(1 << 12):
                if mask >> r & 1: continue
                ndp[mask | (1 << r)] = max(dp[mask | (1 << r)], ndp[mask | (1 << r)], dp[mask] + d[r])

        dp = ndp

    print(max(dp))
