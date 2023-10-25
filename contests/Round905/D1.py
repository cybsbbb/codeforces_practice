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
    a.append(1)
    a.sort()
    b.sort()
    b_idx = 0
    a_idx = 0
    while a_idx < n:
        while b_idx < n and b[b_idx] <= a[a_idx]:
            b_idx += 1
        if b_idx == n:
            break
        else:
            a_idx += 1
            b_idx += 1
    print(n - a_idx)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
