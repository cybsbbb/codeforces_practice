
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
    n, m, k, h = inlt()
    hs = inlt()
    hs_cnt = collections.Counter(hs)
    res = 0
    for i in range(1, m):
        if h - k * i <= 0:
            break
        if (h - k * i) in hs_cnt:
            res += hs_cnt[(h - k * i)]
    for i in range(1, m):
        if h + k * i <= 0:
            break
        if (h + k * i) in hs_cnt:
            res += hs_cnt[(h + k * i)]
    print(res)
    return 0


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
