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
    n = inp()
    p = inlt()
    diff = set()
    for i in range(n):
        diff.add(i + p[i] + 1)
    ans = 0
    if len(diff) == 1:
        ans = 1





if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()





