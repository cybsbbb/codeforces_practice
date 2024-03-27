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
    n, k = inlt()
    res = n
    for i in range(1, n):
        if (n - i) * i <= k:
            res = min(res, i, n - i)
    print(res)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
