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
    a = inlt()
    print(sum(a[:-2]) - a[-2] + a[-1])
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()





