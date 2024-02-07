import bisect
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


def solution():
    n, q = inlt()
    r = inlt()
    r.sort()
    prefix = [0]
    for ri in r:
        prefix.append(prefix[-1] + ri)
    for j in range(q):
        xj = inp()
        idx = bisect.bisect_right(prefix, xj)
        print(idx - 1)
    return


if __name__ == '__main__':
    t = 1
    for i in range(t):
        solution()
