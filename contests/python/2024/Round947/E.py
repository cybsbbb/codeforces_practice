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
    n, q = inlt()
    c = inlt()
    graph = collections.defaultdict(list)
    for i in range(n - 1):
        x, y = inlt()
        graph[x].append(y)
        graph[y].append(x)

    for _ in range(q):
        ui = inp()



if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()





