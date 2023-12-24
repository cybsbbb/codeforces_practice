
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
    n, k = inlt()
    a = inlt()

    tmp = []
    for i in range(n):
        tmp.append((-a[i] % k, i+1))
    for i in range(n):
        if tmp[i] == 0:
            tmp[i] = k

    tmp.sort()
    res = [tmp[i][1] for i in range(n)]
    print(' '.join(map(str, res)))


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
