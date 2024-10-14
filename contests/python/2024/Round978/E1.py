import collections
import sys
import heapq
import math

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

MOD = 10 ** 9 + 7
candidate = (1 << 30)


def solution():
    n, m, k, q = inlt()
    points = []
    r_set = collections.Counter()
    c_set = collections.Counter()
    for _ in range(k):
        r, c, v = inlt()
        r_set[r] += 1
        c_set[c] += 1
    remaining = n + m - len(r_set) - len(c_set)
    max_cnt = max(max(r_set.values()), max(c_set.values()))
    remaining += int(max_cnt == 1)
    ans = pow(candidate, remaining, MOD)
    print(ans)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
