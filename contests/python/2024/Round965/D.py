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


def solution():
    n, m = inlt()
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u, v = inlt()
        u -= 1
        v -= 1
        graph[u].append(v)
    ans = [0] * n
    cur_min = 0
    dp = [0] * (n + 1)
    for i in range(n):
        if i >= -cur_min:
            ans[i] = 1
        dp[i] = min(dp[i], dp[i - 1])
        for nxt in graph[i]:
            dp[nxt] = min(dp[nxt], dp[i] - (nxt - i - 1))
            cur_min = min(cur_min, dp[nxt])
    print(''.join(map(str, ans[:-1])))
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()





