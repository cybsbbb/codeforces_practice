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


def solve():
    s = input()[:-1]
    t = input()[:-1]
    n = len(s)
    m = len(t)
    idx = 0
    while idx < n and idx < m:
        if s[idx] == t[idx]:
            idx += 1
        else:
            break
    print(n + m - idx + int(idx > 0))
    return

t = inp()
for _ in range(t):
    solve()
