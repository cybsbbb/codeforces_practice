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
boundaries = [(i / 10) ** 2 for i in range(0, 11)]

ans = 0
for _ in range(n):
    xi, yi = (list(map(float, input().split())))
    di = xi ** 2 + yi ** 2
    if di > 1:
        continue
    tmp = 0
    while boundaries[tmp] < di:
        tmp += 1
    ans += 11 - tmp

print(ans)
