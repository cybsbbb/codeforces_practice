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
    a = inlt()
    tmp = 1
    for ai in a:
        tmp = tmp * ai
    if tmp <= 0:
        print(0)
    else:
        print(1)
        print(1, 0)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
