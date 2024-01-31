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
    parents = [-1] + inlt()
    for i in range(1, n):
        parents[i] -= 1

    tree = [[] for _ in range(n)]
    for i in range(1, n):
        tree[parents[i]].append(i)

    dfs_order = []
    stack = [0]
    while stack:
        u = stack.pop()
        dfs_order.append(u)
        for v in tree[u]:
            stack.append(v)

    depth = [0] * n
    for i in dfs_order[1:]:
        depth[i] = depth[parents[i]] + 1

    max_depth = depth[:]
    for i in dfs_order[1:][::-1]:
        max_depth[parents[i]] = max(max_depth[parents[i]], max_depth[i])

    savings = []
    for i in range(n):
        values = [max_depth[j] for j in tree[i]]
        values.sort()
        for j in range(len(values) - 1):
            savings.append(values[j] - depth[i] * 2)
    savings.append(max(depth))

    for i in range(len(savings)):
        savings[i] = max(savings[i], 0)

    print(2 * (n - 1) - sum(heapq.nlargest(k + 1, savings)))
    return


if __name__ == '__main__':
    t = 1
    for i in range(t):
        solution()
