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
    n, x = inlt()
    cnt = [0] * (n)
    a = inlt()
    for ai in a:
        if ai < n:
            cnt[ai] += 1
    ans = 0
    while ans < n and cnt[ans] > 0:
        if ans + x < n:
            cnt[ans + x] += cnt[ans] - 1
        ans += 1
    print(ans)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
