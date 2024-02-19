

import collections
import sys

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


for _ in range(inp()):
    n, m, H = inlt()
    l = inlt()
    s = inlt()
    graph = collections.defaultdict(list)
    for i in range(m):
        p1, p2 = inlt()
        graph[p1].append(p2)
        graph[p2].append(p1)



