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
    p1, p2, p3 = inlt()
    if (p1 + p2 + p3) % 2 == 1:
        print(-1)
        return
    if p3 > p1 + p2:
        print(p1 + p2)
    else:
        print((p1 + p2 + p3) // 2)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()





