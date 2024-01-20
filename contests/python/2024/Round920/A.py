import collections
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
    x1, y1 = inlt()
    x2, y2 = inlt()
    x3, y3 = inlt()
    x4, y4 = inlt()
    side = max(abs(y1 - y2), abs(y1 - y3), abs(y1 - y4))
    print(side * side)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
