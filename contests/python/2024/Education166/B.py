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
    n = inp()
    a = inlt()
    b = inlt()
    ans = 1
    ops = float('inf')
    for i in range(n):
        ai, bi = a[i], b[i]
        if ai > bi:
            ai, bi = bi, ai
        ans += abs(bi - ai)
        if ai <= b[-1] <= bi:
            ops = 0
        else:
            ops = min(ops, abs(b[-1] - ai), abs(b[-1] - bi))

    ans += ops
    print(ans)
    return


t = inp()
for _ in range(t):
    solve()
