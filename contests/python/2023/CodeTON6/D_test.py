import collections
import sys
import heapq

input = sys.stdin.readline

sys.setrecursionlimit(50000)


def inp():
    return (int(input()))
def inlt():
    return (list(map(int, input().split())))
def insr():
    s = input()
    return (list(s[:len(s) - 1]))
def invr():
    return (map(int, input().split()))


def subproblem(n, c, k, base, threshold):
    if n == 0:
        return []
    min_idx = -1
    min_val = 10 ** 10
    for i in range(n):
        if c[i] <= min_val:
            min_idx = i
            min_val = c[i]
    max_count = min(threshold, k // (min_val - base))
    if max_count == 0:
        return [0] * n
    remaining = k - max_count * (min_val - base)
    res = [max_count] * (min_idx + 1)
    if remaining > 0:
        res += subproblem(n - (min_idx + 1), c[(min_idx + 1):], remaining, min_val, max_count)
    else:
        res += [0] * (n - (min_idx + 1))
    return res


def solution():
    n = inp()
    c = inlt()
    k = inp()
    print(*subproblem(n, c, k, 0, 10 ** 10))
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
