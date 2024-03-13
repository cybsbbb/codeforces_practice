import collections
import sys
import heapq
import bisect

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
    graph = collections.defaultdict(list)
    color_map = dict()
    color_idx = 1
    for i in range(m):
        u, v, c = inlt()
        if c not in color_map:
            color_map[c] = color_idx
            color_idx += 1
        graph[n + color_map[c]].append(v)
        graph[v].append(n + color_map[c])
        graph[n + color_map[c]].append(u)
        graph[u].append(n + color_map[c])

    b, e = inlt()

    queue = [(0, b)]
    dis = [float('inf')] * (n + len(color_map) + 2)
    dis[b] = 0
    while queue:
        cur_dis, node = heapq.heappop(queue)
        if node == e:
            print(cur_dis // 2)
            return
        if dis[node] != cur_dis:
            continue
        for nxt_node in graph[node]:
            if dis[nxt_node] > cur_dis + 1:
                dis[nxt_node] = cur_dis + 1
                heapq.heappush(queue, (cur_dis + 1, nxt_node))
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
