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
    n, k, x = inlt()
    if k > n:
        print(-1)
        return
    if x < k - 1:
        print(-1)
        return
    res = 0
    for i in range(k):
        res += i
    if x <= k:
        res += (k - 1) * (n - k)
    else:
        res += x * (n - k)
    print(res)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
