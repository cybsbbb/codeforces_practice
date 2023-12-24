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


def perm(n, m):
    res = 1
    for i in range(m):
        res = res * (n-i) % 998244353
    return res


def solution():
    s = insr()
    n = len(s)
    pre = s[0]
    pre_idx = 0
    ops = 0
    shortest = 1
    for i in range(1, n):
        if s[i] != pre:
            ops += (i - pre_idx - 1)
            if i - pre_idx > 1:
                shortest = shortest * perm(i - pre_idx, i - pre_idx - 1) * math.comb(ops, i - pre_idx - 1) % 998244353
            pre = s[i]
            pre_idx = i
    ops += (n - pre_idx - 1)
    if n - pre_idx > 1:
        shortest = shortest * perm(n - pre_idx, n - pre_idx - 1) * math.comb(ops, n - pre_idx - 1) % 998244353
    print(ops, shortest)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
