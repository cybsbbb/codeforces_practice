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
    n = inp()
    tree = collections.defaultdict(list)
    for i in range(n - 1):
        u, v = inlt()
        tree[u - 1].append(v - 1)
        tree[v - 1].append(u - 1)
    parents = [-1] * n
    travel = [0]
    cur_idx = 0
    while cur_idx < len(travel):
        cur_node = travel[cur_idx]
        cur_idx += 1
        for nxt_node in tree[cur_node]:
            if nxt_node == parents[cur_node]:
                continue
            parents[nxt_node] = cur_node
            travel.append(nxt_node)
    max_edges = collections.defaultdict(int)
    min_edges = collections.defaultdict(int)

    for cur_node in travel[1:][::-1]:
        cur_max = cur_node
        cur_min = cur_node
        for nxt_node in tree[cur_node]:
            if nxt_node == parents[cur_node]:
                continue
            cur_max = max(cur_max, max_edges[(cur_node, nxt_node)])
            cur_min = min(cur_min, min_edges[(cur_node, nxt_node)])
        max_edges[(parents[cur_node], cur_node)] = cur_max
        min_edges[(parents[cur_node], cur_node)] = cur_min

    for cur_node in travel:
        mins = [cur_node]
        maxs = [cur_node]
        for nxt_node in tree[cur_node]:
            mins.append(min_edges[(cur_node, nxt_node)])
            maxs.append(max_edges[(cur_node, nxt_node)])
        mins = heapq.nsmallest(2, mins)
        maxs = heapq.nlargest(2, maxs)
        for nxt_node in tree[cur_node]:
            if nxt_node == parents[cur_node]:
                continue
            if min_edges[(cur_node, nxt_node)] == mins[0]:
                min_edges[(nxt_node, cur_node)] = mins[1]
            else:
                min_edges[(nxt_node, cur_node)] = mins[0]

            if max_edges[(cur_node, nxt_node)] == maxs[0]:
                max_edges[(nxt_node, cur_node)] = maxs[1]
            else:
                max_edges[(nxt_node, cur_node)] = maxs[0]

    for cur_node in range(n):
        edges = []
        max_left_r = -1
        for nxt_node in tree[cur_node]:
            l, r = min_edges[(cur_node, nxt_node)], max_edges[(cur_node, nxt_node)]
            if l > cur_node:
                if r != n - 1:
                    edges.append((r, r + 1))
            else:
                if l != 0:
                    edges.append((l - 1, l))
                max_left_r = max(max_left_r, r)

        if max_left_r > cur_node and max_left_r != n - 1:
            edges.append((max_left_r, max_left_r + 1))
        if max_left_r < cur_node and 0 < cur_node < n - 1:
            edges.append((cur_node - 1, cur_node + 1))
        cost = sum(b - a for a, b in edges)

        print(cost, len(edges))
        for a, b in edges:
            print(a + 1, b + 1)
        print()
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()

