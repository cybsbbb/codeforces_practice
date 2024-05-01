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


def dis(x1, y1, x2, y2):
    return (x1 - x2) ** 2 + (y1 - y2) ** 2


t = inp()
for _ in range(t):
    n, m, k = inlt()
    g = [input() for _ in range(n)]
    dp = [0] * (1 << 12)

    for _ in range(k):
        i, j, p = inlt()
        i -= 1
        j -= 1
        d = [0] * 12
        for r in range(1, 12):
            d[r] = -pow(3, r)
            for x in range(max(0, i - r), min(n, i + r + 1)):
                for y in range(max(0, j - r), min(m, j + r + 1)):
                    if g[x][y] == '#' and dis(i, j, x, y) <= r ** 2:
                        d[r] += p

        ndp = [0] * (1 << 12)
        for r in range(1, 12):
            for mask in range(1 << 12):
                if (mask >> r) & 1:
                    continue
                ndp[mask | (1 << r)] = max(dp[mask | (1 << r)], ndp[mask | (1 << r)], dp[mask] + d[r])

        dp = ndp
    print(max(dp))

