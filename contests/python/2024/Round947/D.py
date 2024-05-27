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
    n = inp()
    a, b = inlt()
    graph = collections.defaultdict(list)
    for i in range(n - 1):
        x, y = inlt()
        graph[x].append(y)
        graph[y].append(x)

    parent = [-1 for i in range(n + 1)]
    queue = collections.deque()
    queue.append(a)
    while queue:
        cur_node = queue.popleft()
        for nxt_node in graph[cur_node]:
            if nxt_node != parent[cur_node]:
                parent[nxt_node] = cur_node
                queue.append(nxt_node)

    path = [b]
    while parent[path[-1]] > 0:
        path.append(parent[path[-1]])

    ans = len(path) // 2
    start_node = path[len(path) // 2]

    parent = [-1 for _ in range(n + 1)]
    depth = [-1 for _ in range(n + 1)]
    depth[start_node] = 0
    queue = collections.deque()
    queue.append(start_node)
    while queue:
        cur_node = queue.popleft()
        for nxt_node in graph[cur_node]:
            if nxt_node != parent[cur_node]:
                parent[nxt_node] = cur_node
                depth[nxt_node] = depth[cur_node] + 1
                queue.append(nxt_node)

    ans += (n - 1) * 2 - max(depth)
    print(ans)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()





