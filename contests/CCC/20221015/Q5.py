import collections
import sys
import heapq
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


def dijkstra(N, start_node, graph, res_edges):
    priority_queue = [(0, start_node, start_node)]
    visited = set()
    distance = {i: float('inf') for i in range(1, N + 1)}
    distance[start_node] = 0

    while priority_queue:
        weigth, cur_node, prior_node = heapq.heappop(priority_queue)
        if cur_node in visited:
            continue
        visited.add(cur_node)
        if prior_node == cur_node:
            pass
        else:
            edge = str(sorted((prior_node, cur_node)))
            res_edges.add(edge)

        if len(visited) == N:
            return
        for nxt_node in sorted(graph[cur_node].keys()):
            nxt_weight = graph[cur_node][nxt_node]
            if weigth + nxt_weight < distance[nxt_node] and nxt_node not in visited:
                distance[nxt_node] = weigth + nxt_weight
                heapq.heappush(priority_queue, (weigth + nxt_weight, nxt_node, cur_node))
    return


if __name__ == '__main__':
    N, M = inlt()
    graph = collections.defaultdict(dict)
    for i in range(M):
        A, B, C = inlt()
        graph[A][B] = C
        graph[B][A] = C
    nodes = list(graph.keys())

    if M == N-1:
        print('0')
    elif M == N:
        print('1')
    else:
        res_edges = set()
        for start_node in nodes:
            dijkstra(N, start_node, graph, res_edges)
        print(M - len(res_edges))
