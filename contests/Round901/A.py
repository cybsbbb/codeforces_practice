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
    a, b, n = inlt()
    x = inlt()
    res = b
    for xi in x:
        res += min(a-1, xi)
    print(res)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
