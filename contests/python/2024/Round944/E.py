import bisect
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
    n, k, q = inlt()
    a = [0] + inlt()
    b = [0] + inlt()
    res = []

    for _ in range(q):
        d = inp()
        idx = bisect.bisect_left(a, d)
        ans = b[idx - 1] + (b[idx] - b[idx - 1]) * (d - a[idx - 1]) // (a[idx] - a[idx - 1])
        res.append(ans)
    print(*res)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()





