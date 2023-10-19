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
    n, m = inlt()
    h = [-1] + inlt()
    roads = []
    for _ in range(m):
        u, v = inlt()
        if h[u] > h[v]:
            roads.append((v, u, h[u]))
        else:
            roads.append((u, v, h[v]))
    roads.sort(key=lambda x: x[2])
    q = inp()
    queries = []
    for i in range(q):
        a, b, e = inlt()
        queries.append((h[a]+e, i, a, b, e))
    queries.sort()

    parents = [i for i in range(n + 1)]
    def find(x):
        if parents[x] != x:
            parents[x] = find(parents[x])
        return parents[x]
    def union(a, b):
        a = find(a)
        b = find(b)
        parents[b] = a

    res = ["NO"] * q

    road_idx = 0
    for max_height, i, a, b, e in queries:
        while road_idx < m and roads[road_idx][2] <= max_height:
            union(roads[road_idx][0], roads[road_idx][1])
            road_idx += 1

        if find(a) == find(b):
            res[i] = 'YES'

    for each_res in res:
        print(each_res)


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
