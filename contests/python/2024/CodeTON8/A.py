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
    n, k = inlt()
    if n == k:
        ans = list(1 for i in range(n))
    elif k == 1:
        ans = list(i + 1 for i in range(n))
    else:
        ans = [-1]
    print(*ans)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
