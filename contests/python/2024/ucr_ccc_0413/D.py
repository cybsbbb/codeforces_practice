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
    n, m, k = inlt()
    nm_lcm = math.lcm(n, m)
    left = 1
    right = 10 ** 18
    while left < right:
        mid = left + (right - left) // 2
        if (mid // n) + (mid // m) - 2 * (mid // nm_lcm) < k:
            left = mid + 1
        else:
            right = mid

    print(left)
    return


if __name__ == '__main__':
    t = 1
    for i in range(t):
        solution()
