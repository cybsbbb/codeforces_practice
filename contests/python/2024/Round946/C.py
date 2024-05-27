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
    n = inp()
    a = inlt()
    ans = 0
    stat_tot = collections.defaultdict(int)
    for i in range(n - 2):
        b, c, d = a[i], a[i + 1], a[i + 2]
        ans += stat_tot[(b << 40) + (c << 20)] - stat_tot[(b << 40) + (c << 20) + d]
        ans += stat_tot[(b << 40) + d] - stat_tot[(b << 40) + (c << 20) + d]
        ans += stat_tot[(c << 20) + d] - stat_tot[(b << 40) + (c << 20) + d]
        stat_tot[(b << 40) + (c << 20)] += 1
        stat_tot[(b << 40) + d] += 1
        stat_tot[(c << 20) + d] += 1
        stat_tot[(b << 40) + (c << 20) + d] += 1
    print(ans)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
