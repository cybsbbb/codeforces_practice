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


n = inp()
grid = []
for _ in range(n):
    grid.append(inlt())

cur = 1
for i in range(1, n + 1):
    if cur >= i:
        cur = grid[cur - 1][i - 1]
    else:
        cur = grid[i - 1][cur - 1]
print(cur)

