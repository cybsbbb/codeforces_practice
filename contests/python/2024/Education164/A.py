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
    n, m, k = inlt()
    largest = (n + m - 1) // m
    required = n - largest
    if k >= required:
        print("NO")
    else:
        print("YES")

