import collections
import bisect
import sys
input = sys.stdin.readline


def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))


if __name__ == '__main__':
    n, m = inlt()
    parents = [i for i in range(n)]
    rank = [1 for i in range(n)]
    edges = []

    for i in range(m):
        x, y, z = inlt()
        edges.append([z, x, y])

    edges.sort()

    def find(x):
        if x != parents[x]:
            parents[x] = find(parents[x])
        return parents[x]

    def union(a, b):
        a = find(a)
        b = find(b)

        if rank[a] == rank[b]:
            rank[a] += 1
        elif rank[b] > rank[a]:
            a, b = b, a

        parents[b] = a

    res = 0
    edges_add = 0
    for z, x, y in edges:
        if find(x) != find(y):
            union(x, y)
            res = z
            edges_add += 1
            if edges_add == n-1:
                break

    print(res)

