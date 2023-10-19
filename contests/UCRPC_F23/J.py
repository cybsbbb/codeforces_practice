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
    n, m = inlt()
    graph = collections.defaultdict(list)
    for i in range(m):
        a, b, c, d = inlt()
        graph[a].append((b, c, d))
        graph[b].append((a, c, d))
    distance = [(10**10, 10**10) for _ in range(n)]
    distance[0] = (0, 0)
    queue = []
    heapq.heappush(queue, (0, 0, 0))
    while queue:
        bumps, dis, loc = heapq.heappop(queue)
        if loc == n-1:
            print(bumps, dis)
            return
        else:
            for nxt_loc, path_nump, path_dis in graph[loc]:
                if (bumps + path_nump, dis + path_dis) < distance[nxt_loc]:
                    distance[nxt_loc] = (bumps + path_nump, dis + path_dis)
                    heapq.heappush(queue, (bumps + path_nump, dis + path_dis, nxt_loc))

    return



if __name__ == '__main__':
    t = 1
    for i in range(t):
        solution()
