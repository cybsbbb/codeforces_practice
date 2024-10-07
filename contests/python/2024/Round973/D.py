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
    max_v = 0
    min_v = 10 ** 18
    prefix = 0
    for i in range(n):
        prefix += a[i]
        min_v = min(min_v, (prefix) // (i + 1))
    suffix = 0
    for i in range(n):
        suffix += a[-1-i]
        max_v = max(max_v, (suffix + i) // (i + 1))
    print(max_v - min_v)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()





