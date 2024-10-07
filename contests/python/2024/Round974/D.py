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
    n, d, k = inlt()
    starts = [[] for _ in range(n + 2)]
    ends = [[] for _ in range(n + 2)]
    for i in range(k):
        li, ri = inlt()
        starts[li].append(i)
        ends[ri].append(i)

    sliding_set = set()
    for i in range(1, d + 1):
        for idx in starts[i]:
            sliding_set.add(idx)

    min_v = len(sliding_set)
    min_vs = 1
    max_v = len(sliding_set)
    max_vs = 1

    for l in range(1, n):
        r = l + d
        if r > n:
            break
        for idx in starts[r]:
            sliding_set.add(idx)
        for idx in ends[l]:
            sliding_set.remove(idx)
        if len(sliding_set) < min_v:
            min_v = len(sliding_set)
            min_vs = l + 1
        if len(sliding_set) > max_v:
            max_v = len(sliding_set)
            max_vs = l + 1

    print(max_vs, min_vs)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()

