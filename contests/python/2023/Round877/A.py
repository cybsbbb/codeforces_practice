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

    for i in range(n):
        if a[i] < 0:
            print(a[i])
            return

    print(max(a))
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()