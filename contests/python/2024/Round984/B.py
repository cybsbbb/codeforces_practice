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
    n, k = inlt()
    stat = collections.defaultdict(int)
    ops = []
    for _ in range(k):
        ops.append(inlt())
    ops.sort()
    for bi, ci in ops:
        stat[bi] += ci
    values = sorted(stat.values(), reverse=True)
    print(sum(values[:n]))
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
