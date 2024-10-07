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
    k = inp()
    l = 1
    r = 2 * 10 ** 18
    while l < r:
        mid = (l + r) // 2
        sq = int(math.sqrt(mid))
        while sq * sq > mid:
            sq -= 1
        while (sq + 1) * (sq + 1) <= mid:
            sq += 1
        if mid - sq < k:
            l = mid + 1
        else:
            r = mid
    print(l)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
