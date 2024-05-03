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
    n = inp()
    print(1, 1)
    print(n, n)
    for i in range((n - 2) // 2):
        print(1, 2 * i + 2)
        print(2 * i + 3, 1)
    if n % 2 == 1:
        print(2 * ((n - 2) // 2) + 2, 1)

    print()
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
