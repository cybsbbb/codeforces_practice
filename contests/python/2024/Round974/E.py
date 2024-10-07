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
    n, m, h = inlt()
    graph = [[] for _ in range(n * 2)]
    a = inlt()
    for ai in a:
        ai -= 1
        graph[ai].append((ai + n, 0))
    for _ in range(m):
        ui, vi, wi = inlt()
        ui -= 1
        vi -= 1
        graph[ui].append((vi, wi))
        graph[vi].append((ui, wi))
        graph[ui + n].append((vi + n, wi // 2))
        graph[vi + n].append((ui + n, wi // 2))

    dist_forward = [float('inf')] * (2 * n)
    dist_forward[0] = 0
    heap = [(0, 0)]
    while heap:
        dist, u = heapq.heappop(heap)
        if dist_forward[u] != dist:
            continue
        for nxt, w in graph[u]:
            if dist_forward[nxt] > dist + w:
                dist_forward[nxt] = dist + w
                heapq.heappush(heap, (dist + w, nxt))

    dist_backward = [float('inf')] * (2 * n)
    dist_backward[n - 1] = 0
    heap = [(0, n - 1)]
    while heap:
        dist, u = heapq.heappop(heap)
        if dist_backward[u] != dist:
            continue
        for nxt, w in graph[u]:
            if dist_backward[nxt] > dist + w:
                dist_backward[nxt] = dist + w
                heapq.heappush(heap, (dist + w, nxt))

    ans = float('inf')
    for i in range(n):
        ans = min(ans, max(min(dist_forward[i], dist_forward[i + n]), min(dist_backward[i], dist_backward[i + n])))

    if ans == float('inf'):
        print(-1)
    else:
        print(ans)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()

