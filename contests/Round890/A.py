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
    cur_max = a[0]
    res = 0
    for i in range(1, n):
        if a[i] < cur_max:
            res = max(res, cur_max)
        cur_max = max(cur_max, a[i])
    print(res)
    return 0


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
