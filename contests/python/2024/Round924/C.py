
import collections
import math
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
    n, x = inlt()

    ans = set()
    for i in range(1, int(math.sqrt(n - x)) + 1):
        if (n - x) % i == 0:
            if i % 2 == 0:
                ans.add(i // 2 + 1)
            if (n - x) // i % 2 == 0:
                ans.add((n - x) // i // 2 + 1)

    for i in range(1, int(math.sqrt(n + x - 2)) + 1):
        if (n + x - 2) % i == 0:
            if i % 2 == 0:
                ans.add(i // 2 + 1)
            if (n + x - 2) // i % 2 == 0:
                ans.add((n + x - 2) // i // 2 + 1)

    res = 0
    for i in ans:
        if i >= x:
            res += 1
    print(res)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
