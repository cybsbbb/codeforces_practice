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
    n = inp()

    parents = list(range(n+1))
    rank = [0] * (n+1)
    tot = [1] * (n+1)

    res = [0]

    def find(x):
        if parents[x] != x:
            parents[x] = find(parents[x])
        return parents[x]

    def union(a, b, weight):
        a = find(a)
        b = find(b)

        res[0] += tot[a] * tot[b] * weight

        if rank[a] == rank[b]:
            rank[a] += 1
        elif rank[b] > rank[a]:
            a, b = b, a

        parents[b] = a
        tot[a] += tot[b]
        return

    edges = []

    for i in range(n-1):
        a, b, weight = inlt()
        edges.append([weight, a, b])

    edges.sort()
    for weight, a, b in edges:
        union(a, b, weight)

    print(res[0])
