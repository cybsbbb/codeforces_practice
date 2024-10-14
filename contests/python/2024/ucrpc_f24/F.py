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


n, m = inlt()
p = inp()
ps = inlt()
ps_set = set(ps)
t = inp()
graph = [[] for _ in range(n)]
for _ in range(m):
    ui, vi, li = inlt()
    graph[ui].append((vi, li))
    graph[vi].append((ui, li))

max_dist = 0

for pi in ps:
    remaining = n
    dist = [10 ** 18] * n
    dist[pi] = 0
    heap = [(0, pi)]
    while heap:
        cur_dist, cur_node = heapq.heappop(heap)
        if dist[cur_node] != cur_dist:
            continue
        if cur_node in ps_set:
            remaining -= 1
            max_dist = max(max_dist, cur_dist)
            if remaining == 0:
                break
        for ui, li in graph[cur_node]:
            nxt_dist = cur_dist + li
            if nxt_dist < dist[ui]:
                dist[ui] = nxt_dist
                heapq.heappush(heap, (nxt_dist, ui))

print(f'{max_dist / (t * 60):.3f}')

