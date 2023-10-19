

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

    if max_val + min_val >= 0:
        print(2 * n - 2)
        for i in range(n):
            if i != max_idx:
                print(i + 1, max_idx + 1)
                a[i] += a[max_idx]
        for i in range(1, n):
            print(i + 1, i - 1 + 1)
            a[i] += a[i-1]
    else:
        print(2 * n - 2)
        for i in range(n):
            if i != min_idx:
                print(i + 1, min_idx + 1)
                a[i] += a[min_idx]
        for i in range(1, n)[::-1]:
            print(i - 1 + 1, i + 1)
            a[i-1] += a[i]
    # print(a)
    return 0

if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
