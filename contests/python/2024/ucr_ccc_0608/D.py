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

    parent = [i for i in range(n)]
    size = [1 for i in range(n)]
    edges = [0 for i in range(n)]

    def find(x):
        x_copy = x
        while x != parent[x]:
            x = parent[x]
        while x_copy != x:
            parent[x_copy], x_copy = x, parent[x_copy]
        return x

    def union(a, b):
        a, b = find(a), find(b)
        if a != b:
            parent[a] = b
            size[b] += size[a]
            edges[b] += edges[a]
        edges[b] += 1

    graph = collections.defaultdict(int)
    for _ in range(m):
        ai, bi = inlt()
        ai -= 1
        bi -= 1
        union(ai, bi)

    ans = 0
    for i in range(n):
        if parent[i] == i:
            ans += size[i] * (size[i] - 1) // 2 - edges[i]

    print(ans)
    return


if __name__ == '__main__':
    t = 1
    for i in range(t):
        solution()





