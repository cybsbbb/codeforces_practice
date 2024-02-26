import sys
import math
import heapq
import collections


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


def f(x, ds, dl, H):
    d = math.gcd(ds, H)
    if dl % d:
        return -1
    k = pow(ds//d, -1, H // d) * (dl // d) % (H // d) + 1
    return ((x - k) // (H // d) + 1) * (H // d) + k


for _ in range(inp()):
    n, m, H = inlt()
    l = inlt()
    s = inlt()
    graph = [[] for i in range(n)]
    for i in range(m):
        p1, p2 = inlt()
        p1 -= 1
        p2 -= 1
        graph[p1].append(p2)
        graph[p2].append(p1)

    dist = [-1] * n
    dist[0] = 0
    q = []
    heapq.heappush(q, [0, 0])
    while q:
        d_v, v = heapq.heappop(q)
        if dist[v] != d_v:
            continue
        for u in graph[v]:
            if dist[u] == -1 or dist[u] > dist[v] + 1:
                a = f(dist[v], s[v] - s[u], l[u] - l[v], H)
                if a != -1 and (dist[u] == -1 or dist[u] > a):
                    dist[u] = a
                    heapq.heappush(q, [a, u])
    print(dist)
    print(dist[-1])

