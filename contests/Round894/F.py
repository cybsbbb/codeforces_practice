import collections
import math
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
    w, f = inlt()
    n = inp()
    s = inlt()
    tot = sum(s)
    dp = [0] * (tot + 1)
    dp[0] = 1
    for strength in s:
        for i in range(tot - strength, -1, -1):
            dp[i + strength] |= dp[i]
    res = (tot - 1) // max(w, f) + 1
    for i in range(1, tot):
        if dp[i] == 1:
            res = min(res, max((i - 1) // w + 1, (tot - i - 1) // f + 1))
    print(res)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
