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


t = inp()
for _ in range(t):
    n = inp()
    p = inlt()
    ans = 3
    for i in range(n):
        if i + 1 == p[p[i] - 1]:
            ans = 2
            break
    print(ans)
    continue

