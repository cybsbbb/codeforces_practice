
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
    px, py = inlt()
    ax, ay = inlt()
    bx, by = inlt()

    # use only A
    res1 = max(math.sqrt((ax - px) ** 2 + (ay - py) ** 2), math.sqrt((ax) ** 2 + (ay) ** 2))
    # use only B
    res2 = max(math.sqrt((bx - px) ** 2 + (by - py) ** 2), math.sqrt((bx) ** 2 + (by) ** 2))
    # first by A, then by B
    res3 = max(math.sqrt((ax) ** 2 + (ay) ** 2), math.sqrt((bx - px) ** 2 + (by - py) ** 2), math.sqrt((ax - bx) ** 2 + (ay - by) ** 2) / 2)
    # first by B, then by A
    res4 = max(math.sqrt((bx) ** 2 + (by) ** 2), math.sqrt((ax - px) ** 2 + (ay - py) ** 2), math.sqrt((ax - bx) ** 2 + (ay - by) ** 2) / 2)
    print(min(res1, res2, res3, res4))
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
