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


n = inp()
ans = 0.0
for _ in range(n):
    di, si = (list(map(float, input().split())))
    ans += di / si
print(f'{ans:.5f}')
