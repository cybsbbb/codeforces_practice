import collections
import sys
import heapq
import math
from functools import cache

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
    n, a, x, y = inlt()

    @cache
    def helper(n):
        if n == 0:
            return 0
        else:
            return min(helper(n // a) + x, (6 * y + sum(helper(n // b) for b in range(2, 7))) / 5)

    print(helper(n))
    return



if __name__ == '__main__':
    t = 1
    for i in range(t):
        solution()





