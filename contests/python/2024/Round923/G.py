import bisect
import collections
import sys
import heapq
from functools import cache

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
    a = [0] + inlt()

    @cache
    def dfs(i, x):
        md = 0
        if i > n:
            return 0
        if i + x - 1 >= n:
            return 1
        x = max(x, a[i])
        # forward
        for j in range(i + 1, min(n + 1, i + x)):
            md = max(md, a[j] - (i + x - j))
        ans = dfs(i + x, min(md, n + 1 - (i + x))) + 1
        # backward
        for j in range(i + x, n + 1):
            md -= 1
            if a[j] >= j - i + 1:
                ans1 = dfs(j + 1, min(md, n + 1 - (j + 1))) + 1
                ans = min(ans, ans1)
            md = max(md, a[j] - 1)
        return ans

    res = dfs(1, a[1])
    print(res)
    return res


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
