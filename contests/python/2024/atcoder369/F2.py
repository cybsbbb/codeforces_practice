import sys
import heapq
import itertools

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


h, w, n = inlt()
grid = [[0] * (w + 1) for _ in range(h + 1)]
for i in range(n):
    ri, ci = inlt()
    ri -= 1
    ci -= 1
    grid[ri][ci] = 1

for i in range(h):
    print(grid[i])

dp = [[0] * (w + 1) for _ in range(h + 1)]
stat = [[''] * (w + 1) for _ in range(h + 1)]

for i in range(1, h):
    dp[i][0] = dp[i - 1][0] + int(grid[i][0] == 1)
    stat[i][0] = 'D'

for j in range(1, w):
    dp[0][j] = dp[0][j - 1] + int(grid[0][j] == 1)
    stat[0][j] = 'R'

for i in range(1, h):
    for j in range(1, w):
        if dp[i - 1][j] > dp[i][j - 1]:
            dp[i][j] = dp[i - 1][j] + int(grid[i][j] == 1)
            stat[i][j] = 'D'
        else:
            dp[i][j] = dp[i][j - 1] + int(grid[i][j] == 1)
            stat[i][j] = 'R'

ans = []
i, j = h - 1, w - 1
for _ in range(h + w - 2):
    cur_stat = stat[i][j]
    ans.append(cur_stat)
    if cur_stat == 'R':
        j -= 1
    elif cur_stat == 'D':
        i -= 1

print(dp[h - 1][w - 1])
print(''.join(ans[::-1]))

