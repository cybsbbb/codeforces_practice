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
    x = inlt()
    x.sort()
    ans = x[1] - x[0] + x[2] - x[1]
    print(ans)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()





