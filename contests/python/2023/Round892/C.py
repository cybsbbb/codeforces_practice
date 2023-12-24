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


def get_value(n, permutation):
    res = 0
    cur_max = 0
    for i in range(n):
        cur_term = (i+1) * permutation[i]
        cur_max = max(cur_max, cur_term)
        res += cur_term
    return res - cur_max


def solution():
    n = inp()
    res = 0
    permutation = [i for i in range(1, n + 1)]

    for idx in range(n):
        tmp_permutation = permutation[:idx] + permutation[idx:][::-1]
        res = max(res, get_value(n, tmp_permutation))

    print(res)

    return 0


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
