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
    a.sort()
    median = (n + 1) // 2 - 1
    res = 1
    a[median] += 1
    while median + 1 < n and a[median + 1] < a[median]:
        a[median + 1] += 1
        res += 1
        median += 1
    print(res)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
