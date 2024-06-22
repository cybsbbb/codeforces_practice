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
    n, a, b = inlt()
    if b <= a:
        print(n * a)
        return
    k = min(n, b - a)
    ans = (b + b - k + 1) * k // 2
    ans += (n - k) * a
    print(ans)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()





