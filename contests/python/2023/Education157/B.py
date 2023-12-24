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
    a.sort()
    res = a[n-1] - a[0] + a[2 * n - 1] - a[n]
    print(res)
    for i in range(n):
        print(a[i], a[i + n])
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
