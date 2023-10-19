import collections
import math
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
    n, q = inlt()
    a = inlt()
    queries = []
    for _ in range(q):
        queries.append(inlt())



if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
