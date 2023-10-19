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
    strength = inlt()
    weaker = 1
    Monte = strength[0]
    for i in range(1, n):
        if strength[i] < Monte:
            weaker += 1
    res = 1
    while n & weaker == 0:
        n = n >> 1
        res = res << 1
    print(res)
    return


if __name__ == '__main__':
    t = 1
    for i in range(t):
        solution()
