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
    b = inlt()
    res = []
    res.append(b[0])
    for i in range(1, n):
        if b[i-1] <= b[i]:
            res.append(b[i])
        else:
            res.append(b[i])
            res.append(b[i])

    print(len(res))
    print(*res)


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
