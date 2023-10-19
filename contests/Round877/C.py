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

    res = [[0]*m for i in range(n)]
    row = 0
    for i in range(1, n, 2):
        for j in range(m):
            res[row][j] = j + 1 + i * m
        row += 1

    for i in range(0, n, 2):
        for j in range(m):
            res[row][j] = j + 1 + i * m
        row += 1

    for i in range(n):
        print(' '.join(map(str,res[i])))


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
