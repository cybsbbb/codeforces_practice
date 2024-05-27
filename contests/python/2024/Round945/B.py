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
    if len(set(a)) == 1:
        print(1)
        return

    vals = []
    for bit in range(20):
        occur = False
        last = -1
        max_interval = 0
        for i in range(n):
            if a[i] & (1 << bit) > 0:
                occur = True
                max_interval = max(max_interval, i - last)
                last = i
        max_interval = max(max_interval, n - last)
        if occur is True:
            vals.append(max_interval)

    print(max(vals))
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()





