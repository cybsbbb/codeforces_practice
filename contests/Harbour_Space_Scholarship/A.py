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
    x, y, n = inlt()
    intervals = y - x
    needs = ((n) * (n-1)) // 2
    if needs > intervals:
        print(-1)
        return
    else:
        res = []
        res.append(x)
        res.append(x + intervals - needs + n - 1)
        for i in range(2, n):
            res.append(res[-1] + n - i)
        print(*res)
        return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
