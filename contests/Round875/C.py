import sys
from collections import defaultdict, deque
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


def solution():
    n = inp()
    edges = [inlt() for _ in range(n-1)]

    adj = defaultdict(list)
    for edge_idx in range(n-1):
        u, v = edges[edge_idx]
        adj[u].append((v, edge_idx))
        adj[v].append((u, edge_idx))

    queue = deque([(1, -1, 1)])
    visited = [False] * (n + 1)
    visited[1] = True
    res = 1
    while queue:
        node, edge_idx, readings = queue.popleft()
        for neighbor, neighbor_edge_idx in adj[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                if neighbor_edge_idx > edge_idx:
                    queue.append((neighbor, neighbor_edge_idx, readings))
                else:
                    queue.append((neighbor, neighbor_edge_idx, readings+1))
                    res = max(res, readings+1)

    print(res)


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
