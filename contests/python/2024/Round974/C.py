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
    a.sort()
    if n <= 2:
        print(-1)
        return
    tot = sum(a)
    threshold = a[n // 2] * 2
    ans = threshold * n + 1 - tot
    if ans < 0:
        print(0)
    else:
        print(ans)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()

