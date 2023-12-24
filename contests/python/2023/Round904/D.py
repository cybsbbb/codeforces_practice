import collections
import math
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
    n = inp()
    a = inlt()
    cnt = [0] * (n + 1)
    for x in a:
        cnt[x] += 1
    dp = [0] * (n + 1)
    for x in range(n, 0, -1):
        c = 0
        for i in range(x, n + 1, x):
            c += cnt[i]
        dp[x] = c * (c-1) // 2
        for i in range(2*x, n + 1, x):
            dp[x] -= dp[i]
    for x in range(n+1):
        if cnt[x]:
            for i in range(x, n+1, x):
                dp[i] = 0
    print(sum(dp))
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
