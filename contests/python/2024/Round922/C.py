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
    a, b, r = inlt()

    if a > b:
        a, b = b, a

    cur_r = 0
    find_highest = False
    for bit in range(64)[::-1]:
        if (1 << bit) & a == 0 and (1 << bit) & b != 0:
            if not find_highest:
                find_highest = True
                continue
            else:
                if cur_r + (1 << bit) <= r:
                    cur_r += (1 << bit)
                    a += (1 << bit)
                    b -= (1 << bit)

    print(abs(b - a))
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
