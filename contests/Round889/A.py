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
    n = inp()
    p = inlt()
    res = 0
    for i in range(n):
        if p[i] == (i+1):
            res += 1

    if res == 0:
        print(0)
    else:
        print((res - 1)//2 + 1)
    return 0


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
