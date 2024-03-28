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
    res = [['.'] * (2 * n) for _ in range(2 * n)]
    for i in range(n):
        for j in range(n):
            if (i + j) % 2 == 0:
                res[2 * i][2 * j] = '#'
                res[2 * i + 1][2 * j] = '#'
                res[2 * i][2 * j + 1] = '#'
                res[2 * i + 1][2 * j + 1] = '#'
            else:
                res[2 * i][2 * j] = '.'
                res[2 * i + 1][2 * j] = '.'
                res[2 * i][2 * j + 1] = '.'
                res[2 * i + 1][2 * j + 1] = '.'

    for i in range(2 * n):
        print(''.join(res[i]))

    return



if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
