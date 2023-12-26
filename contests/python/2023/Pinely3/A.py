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


def solution():
    n = inp()
    max_x = - 1000
    min_x = 1000
    max_y = - 1000
    min_y = 1000
    for _ in range(n):
        xi, yi = inlt()
        max_x = max(max_x, xi)
        min_x = min(min_x, xi)
        max_y = max(max_y, yi)
        min_y = min(min_y, yi)

    if max_x <= 0 or min_x >= 0 or max_y <= 0 or min_y >= 0:
        print("YES")
    else:
        print("NO")
    return 0


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
