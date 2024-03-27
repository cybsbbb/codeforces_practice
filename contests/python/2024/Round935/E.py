import collections
import sys
import math
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
    n, x = inlt()
    p = inlt()
    x_idx = -1
    for i in range(n):
        if p[i] == x:
            x_idx = i + 1
            break
    l = 1
    r = n + 1
    while (r - l) > 1:
        m = (l + r) // 2
        if p[m - 1] <= x:
            l = m
        else:
            r = m

    if l == x_idx:
        print(0)
    else:
        print(1)
        print(x_idx, l)

    return



if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
