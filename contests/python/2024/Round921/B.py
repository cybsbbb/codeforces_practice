import collections
import math
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
    x, n = inlt()
    ans = 1
    for m in range(1, int(math.sqrt(x)) + 2):
        if x % m == 0:
            if m >= n:
                ans = max(ans, x // m)
            if x // m >= n:
                ans = max(ans, m)
    print(ans)
    return ans


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
