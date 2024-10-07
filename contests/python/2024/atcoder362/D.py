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

n, m = inlt()
a = inlt()
graph = [[] for i in range(n)]
for _ in range(m):
    ui, vi, bi = inlt()
    ui -= 1
    vi -= 1
    graph[ui].append((vi, bi))
    graph[vi].append((ui, bi))

dist = [float('inf')] * n
dist[0] = a[0]

queue = [(a[0], 0)]

while queue:
    cur_dist, cur_node = heapq.heappop(queue)
    if dist[cur_node] != cur_dist:
        continue
    for nxt_node, bi in graph[cur_node]:
        nxt_dist = cur_dist + bi + a[nxt_node]
        if nxt_dist < dist[nxt_node]:
            dist[nxt_node] = nxt_dist
            heapq.heappush(queue, (nxt_dist, nxt_node))

print(*dist[1:])
