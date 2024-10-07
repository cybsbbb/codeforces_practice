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
    n, k = inlt()
    a = inlt()
    cur_own = 0
    ans = 0
    for ai in a:
        if ai >= k:
            cur_own += ai
        if ai == 0 and cur_own > 0:
            cur_own -= 1
            ans += 1
    print(ans)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()

