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
    a = inlt()
    res = 0
    intervals = []
    for i in range(1, n):
        interval = abs(a[i] - a[i-1])
        intervals.append(interval)
        res += interval
    intervals.sort(reverse=True)
    for i in range(k-1):
        res -= intervals[i]
    print(res)
    return 0


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
