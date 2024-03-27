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
    n, m = inlt()
    a = inlt()
    b = inlt()
    res = [0] * n
    pre_min = 0
    for i in range(n)[::-1]:
        res[i] = pre_min + a[i]
        pre_min += min(a[i], b[i])
    print(min(res[:m]))
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
