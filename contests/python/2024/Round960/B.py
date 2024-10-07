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


def solution():
    n, x, y = inlt()
    ans = [0] * n
    for i in range(y, x + 1):
        ans[i - 1] = 1
    cur = -1
    for i in range(x + 1, n + 1):
        ans[i - 1] = cur
        cur *= -1
    cur = -1
    for i in range(1, y)[::-1]:
        ans[i - 1] = cur
        cur *= -1
    print(*ans)
    return



if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()





