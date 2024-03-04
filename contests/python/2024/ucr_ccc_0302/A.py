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
    M, D = inlt()
    y, m, d = inlt()
    d += 1
    if d > D:
        d = 1
        m += 1
    if m > M:
        m = 1
        y += 1
    print(y, m, d)
    return


if __name__ == '__main__':
    t = 1
    for i in range(t):
        solution()
