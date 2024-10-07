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
    n, k = inlt()
    print((n - 1) * k + 1)
    return


t = inp()
for _ in range(t):
    solve()
