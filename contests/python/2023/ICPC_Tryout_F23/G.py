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
    n, m = inlt()
    x = inlt()
    x.sort()

    if n >= m:
        print(0)
        return

    intervals = []
    for i in range(1, m):
        intervals.append(x[i] - x[i-1])
    intervals.sort()
    # print(intervals)
    if n == 1:
        print(sum(intervals[:]))
    else:
        print(sum(intervals[:-(n - 1)]))
    return


if __name__ == '__main__':
    t = 1
    for i in range(t):
        solution()
