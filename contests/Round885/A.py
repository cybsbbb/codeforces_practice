
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
    n, m, k = inlt()
    x, y = inlt()
    res = 'YES'
    for i in range(k):
        xx, yy = inlt()
        if (x + y) % 2 == (xx + yy) % 2:
            res = 'NO'
    print(res)


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
