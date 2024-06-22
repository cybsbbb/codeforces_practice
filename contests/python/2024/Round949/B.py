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
    n, m = inlt()
    left = max(0, n - m)
    right = n + m
    ans = 0
    for i in range(32):
        if (1 << i) & left:
            ans ^= (1 << i)
        else:
            tmp = left - (left & ((1 << i) - 1)) + (1 << i)
            if tmp <= right:
                ans ^= (1 << i)
    print(ans)
    return



if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()





