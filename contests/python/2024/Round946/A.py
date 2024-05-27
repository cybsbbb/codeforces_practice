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
    x, y = inlt()
    c1 = (y + 1) // 2
    remain = 15 * c1 - y * 4
    if remain >= x:
        print(c1)
    else:
        c1 += (x - remain + 14) // 15
        print(c1)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()





