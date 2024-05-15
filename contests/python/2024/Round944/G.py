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
    n = inp()
    a = inlt()
    stat = collections.defaultdict(list)
    for i in range(n):
        stat[(a[i] >> 2) + 233].append(i)
    ans = [0] * n
    for key, idx in stat.items():
        idx = stat[key]
        sorted_idx = sorted(idx, key=lambda x: a[x])
        for i, val_i in zip(idx, sorted_idx):
            ans[i] = a[val_i]

    print(*ans)
    return



if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()





