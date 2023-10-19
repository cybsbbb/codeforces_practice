
import collections
import math
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
    n, k = inlt()
    a = set(inlt())
    graph = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = inlt()
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)

    def bfs(start):
        queue = collections.deque()
        queue.append((start, -1))
        res = -1
        distance = -1
        step = -1
        while queue:
            step += 1
            for _ in range(len(queue)):
                cur, parent = queue.popleft()
                if cur + 1 in a:
                    res = cur
                    distance = step
                for nxt in graph[cur]:
                    if nxt != parent:
                        queue.append((nxt, cur))

        return res, distance

    x, _ = bfs(0)
    y, d = bfs(x)
    print((d + 1) // 2)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
