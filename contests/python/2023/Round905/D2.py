import bisect
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
    n, m = inlt()
    a = inlt()
    b = inlt()
    a.sort()
    b.sort()
    b_idx = 0
    a_idx = 0
    max_unmatch_b = -1
    while a_idx < n - 1:
        while b_idx < n and b[b_idx] <= a[a_idx]:
            max_unmatch_b = b[b_idx]
            b_idx += 1
        if b_idx == n:
            break
        else:
            a_idx += 1
            b_idx += 1
    if b_idx != n:
        max_unmatch_b = b[-1]
    ops = n - a_idx

    if m < max_unmatch_b:
        print(m * (ops - 1))
    else:
        print((max_unmatch_b - 1) * (ops - 1) + (m - max_unmatch_b + 1) * ops)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
