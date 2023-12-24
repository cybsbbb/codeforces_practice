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
    a_sorted = sorted((a[i], i) for i in range(n))
    res = [0] * n
    for i in range(n):
        res[a_sorted[i][1]] = n - i
    print(*res)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
