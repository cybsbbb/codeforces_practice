

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
    n = inp()
    a = inlt()
    max_val, max_idx = max(zip(a, range(n)))
    min_val, min_idx = min(zip(a, range(n)))

    # All item  >= 0
    if max_val >= 0 and min_val >= 0:
        print(n-1)
        for i in range(1, n):
            print(i + 1, i - 1 + 1)
        return 0
    # All item  <= 0
    if max_val <= 0 and min_val <= 0:
        print(n - 1)
        for i in range(1, n)[::-1]:
            print(i - 1 + 1, i + 1)
        return 0

    max_val, max_idx = max(zip(a, range(n)))
    min_val, min_idx = min(zip(a, range(n)))
    res_positive = []
    while max_val + min_val < 0:
        res_positive.append((max_idx+1, max_idx+1))
        max_val *= 2
    for i in range(n):
        if a[i] < 0:
            res_positive.append((i + 1, max_idx + 1))
    for i in range(1, n):
        res_positive.append((i + 1, i - 1 + 1))

    max_val, max_idx = max(zip(a, range(n)))
    min_val, min_idx = min(zip(a, range(n)))
    res_negative = []
    while max_val + min_val > 0:
        res_negative.append((min_idx+1, min_idx+1))
        min_val *= 2
    for i in range(n):
        if a[i] > 0:
            res_negative.append((i + 1, min_idx + 1))
    for i in range(1, n)[::-1]:
        res_negative.append((i - 1 + 1, i + 1))

    res = res_positive if len(res_positive) < len(res_negative) else res_negative
    print(len(res))
    for i, j in res:
        print(i, j)


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
