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
    n, m = inlt()
    a = []
    for i in range(n):
        a.append(inlt())
    b = []
    for i in range(n):
        b.append(inlt())
    h1 = sorted(sorted(x) for x in a)
    h2 = sorted(sorted(x) for x in b)
    l1 = sorted(sorted(x) for x in zip(*a))
    l2 = sorted(sorted(x) for x in zip(*b))
    print("YES" if h1 == h2 and l1 == l2 else "NO")
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()





