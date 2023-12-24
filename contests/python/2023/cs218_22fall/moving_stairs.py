import collections
import heapq
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



def bfs(n, m, k, graph):
    cur_time = 0
    cur_layer = [0]
    seen = set()
    seen.add(0)

    while len(cur_layer) != 0:
        nxt_layer = []
        for node in cur_layer:
            for nxt_node in graph[node]:
                if nxt_node not in seen:
                    if nxt_node == k or nxt_node == n + k:
                        return cur_time + 1
                    nxt_layer.append(nxt_node)
                    seen.add(nxt_node)
        cur_time += 1
        cur_layer, nxt_layer = nxt_layer, cur_layer

    return -1


if __name__ == '__main__':
    n, m, k = inlt()
    graph = collections.defaultdict(set)
    for i in range(m):
        x, y, z = inlt()
        graph[x].add(n+z)
        graph[n+x].add(y)
        graph[y].add(n+z)
        graph[y].add(n+x)
        graph[y].add(n+y)
        graph[n+y].add(y)
        graph[n+z].add(y)
        graph[n+z].add(x)
        graph[n+z].add(z)
        graph[z].add(n+z)

    print(bfs(n, m, k, graph))
