import bisect
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
    edges = []
    for i in range(m):
        u, v, w = inlt()
        u -= 1
        v -= 1
        edges.append((w, u, v))
    edges.sort(reverse=True)

    parent = [i for i in range(n)]
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

    graph = [[] for _ in range(n)]
    res_w, end1, end2 = float('inf'), -1, -1
    for w, u, v in edges:
        pu, pv = find(u), find(v)
        if pu != pv:
            parent[pu] = pv
            graph[u].append(v)
            graph[v].append(u)
        else:
            res_w = w
            end1, end2 = u, v

    res_circle = []
    prev = [-1] * n
    stack = collections.deque()
    seen = set()
    seen.add(end1)
    stack.append(end1)
    while stack:
        cur_v = stack.popleft()
        seen.add(cur_v)
        for nxt_v in graph[cur_v]:
            if nxt_v not in seen:
                stack.append(nxt_v)
                prev[nxt_v] = cur_v

    res_circle.append(end2)
    while prev[res_circle[-1]] != -1:
        res_circle.append(prev[res_circle[-1]])

    for i in range(len(res_circle)):
        res_circle[i] += 1

    print(res_w, len(res_circle))
    print(*res_circle)

    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
