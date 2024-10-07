import bisect
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


def solution(t):
    n, g = inlt()
    e = []
    for _ in range(n):
        e.append(inp())
    e.sort()
    min_idx = -1
    min_dis = 10 ** 18
    idx = bisect.bisect_left(e, g)
    if idx < n:
        if abs(e[idx] - g) < min_dis:
            min_dis = abs(e[idx] - g)
            min_idx = n - (idx)
    if idx > 0:
        if abs(e[idx - 1] - g) < min_dis:
            min_dis = abs(e[idx - 1] - g)
            min_idx = n - (idx - 1)
    print(f'Case #{t}: {min_idx} {min_dis}')
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution(i + 1)
