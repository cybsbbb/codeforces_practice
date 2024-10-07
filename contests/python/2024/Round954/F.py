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
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u, v = inlt()
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)
    timestamp = [0] * n
    low = [0] * n
    used = [0] * n
    index = [0] * n
    sub_size = [0] * n
    cur_time = 0

    dfs = []
    dfs.append((0, -1))
    ans = 0
    while len(dfs) > 0:
        v, p = dfs[-1]
        if index[v] == 0:
            used[v] = 1
            timestamp[v] = cur_time
            low[v] = cur_time
            cur_time += 1
            sub_size[v] = 1
        if index[v] == len(graph[v]):
            dfs.pop()
            if p != -1:
                low[p] = min(low[p], low[v])
                sub_size[p] += sub_size[v]
                if low[v] == timestamp[v]:
                    ans = max(ans, (n - sub_size[v]) * sub_size[v])
        else:
            u = graph[v][index[v]]
            if used[u] == 1:
                if u != p:
                    low[v] = min(low[v], timestamp[u])
            else:
                dfs.append((u, v))
            index[v] += 1
    print(n * (n - 1) // 2 - ans)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
