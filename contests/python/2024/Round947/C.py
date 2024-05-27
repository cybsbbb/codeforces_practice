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
    a = inlt()
    ans = min(a[0], a[1])
    for i in range(n - 1):
        ans = max(ans, min(a[i], a[i + 1]))
    for i in range(n - 2):
        ans = max(ans, sorted(a[i: i + 3])[1])

    print(ans)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()





