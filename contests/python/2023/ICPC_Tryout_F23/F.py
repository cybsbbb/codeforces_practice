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

n = inp()
c, d = inlt()
dp = dict()
dp = [[1000] * (d+1) for _ in range(c + 1)]
dp[0][0] = 0
for i in range(n):
    c_i, d_i = inlt()
    for cc in range(c+1)[::-1]:
        for dd in range(d+1)[::-1]:
            dp[min(c, cc + c_i)][min(d, dd + d_i)] = min(dp[min(c, cc + c_i)][min(d, dd + d_i)], dp[cc][dd] + 1)

if dp[-1][-1] == 1000:
    print(-1)
else:
    print(dp[-1][-1])
