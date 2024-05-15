import bisect
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
    grid = []
    for i in range(3):
        grid.append(inlt())

    graph = [set() for i in range(2 * n + 1)]
    for a, b, c in zip(*grid):
        graph[-a].add(b)
        graph[-a].add(c)
        graph[-b].add(a)
        graph[-b].add(c)
        graph[-c].add(a)
        graph[-c].add(b)
    status = [0] * len(graph)

    def helper(i):
        traversal = [i]
        status[i] = 1
        status[-i] = -1
        processed = 0
        while processed < len(traversal):
            v = traversal[processed]
            processed += 1
            for u in graph[v]:
                if status[u] == -1:
                    for w in traversal:
                        status[w] = 0
                        status[-w] = 0
                    return False
                if status[u] == 0:
                    status[u] = 1
                    status[-u] = -1
                    traversal.append(u)
        return True

    for i in range(1, n + 1):
        if status[i] != 0:
            continue
        if not (helper(i) or helper(-i)):
            print("NO")
            return

    print("YES")
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()





