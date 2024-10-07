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

MOD = 998244353

n = inp()
a = inlt()

dp = [collections.defaultdict(int) for _ in range(n + 1)]
dp[1][(a[0], -1)] = 1
for i in range(1, n):
    cur_val = a[i]
    for j in range(2, n)[::-1]:
        for last, diff in dp[j]:
            if last + diff == cur_val:
                dp[j + 1][(cur_val, diff)] += dp[j][(last, diff)]
                dp[j + 1][(cur_val, diff)] %= MOD
    for (last, _), val in dp[1].items():
        dp[2][(cur_val, cur_val - last)] += val
        dp[2][(cur_val, cur_val - last)] %= MOD
    dp[1][(cur_val, -1)] += 1

ans = [0] * n
for i in range(1, n + 1):
    for key, val in dp[i].items():
        ans[i - 1] += val
        ans[i - 1] %= MOD

print(*ans)
