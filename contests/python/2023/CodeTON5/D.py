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
    dist = [[float('inf')] * n for _ in range(n)]
    for _ in range(m):
        u, v, y = inlt()
        u -= 1
        v -= 1
        dist[u][v] = dist[v][u] = y

    for i in range(n):
        dist[i][i] = 0

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    if dist[0][n-1] == float('inf'):
        print('inf')
        return

    dist_start = [(d, i) for i, d in enumerate(dist[0])]
    dist_start.sort()

    res = []
    tot_time = 0
    cur = [0] * n
    for d, i in dist_start:
        cur_time = d - tot_time
        if cur_time > 0:
            game = ''.join(map(str, cur))
            tot_time += cur_time
            res.append(f'{game} {cur_time}')
        cur[i] = 1
        if i == n-1:
            break

    print(f'{tot_time} {len(res)}')
    for game in res:
        print(game)


if __name__ == '__main__':
    t = 1
    for i in range(t):
        solution()
