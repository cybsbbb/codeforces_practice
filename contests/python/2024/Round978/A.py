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
    n, r = inlt()
    a = inlt()
    ans = 0
    remaining = 0
    for ai in a:
        r -= ai // 2
        remaining += ai % 2
        ans += (ai // 2) * 2
    if r >= remaining:
        ans += remaining
    else:
        ans += 2 * r - remaining
    print(ans)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
