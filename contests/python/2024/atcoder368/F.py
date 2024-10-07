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


n = inp()
a = inlt()

m = max(a)
dp = [0] * (m + 1)
divides = [set() for _ in range(m + 1)]
for div in range(1, int(math.sqrt(m)) + 2):
    for k in range(2 * div, m + 1, div):
        divides[k].add(div)
        if div > 1:
            divides[k].add(k // div)
for i in range(2, m + 1):
    reachable = set()
    for div in divides[i]:
        reachable.add(dp[div])
    mex = 0
    while mex in reachable:
        mex += 1
    dp[i] = mex

ans = 0
for ai in a:
    ans ^= dp[ai]

print("Anna" if ans else "Bruno")
