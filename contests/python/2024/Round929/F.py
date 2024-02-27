import bisect
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
    matrix = []
    for i in range(n):
        matrix.append(inlt())
    dist = [[float('inf')] * m for _ in range(n)]
    dist[0][0] = 0

    directions = [[2, 0], [1, 1]]
    queue = [(0, 0, 0)]
    while queue:
        cur_t, cur_x, cur_y = heapq.heappop(queue)
        if dist[cur_x][cur_y] != cur_t:
            continue
        nxt_x, nxt_y = (cur_x + 1) % n, (cur_y + 1) % m
        if matrix[nxt_x][nxt_y] == 0 and dist[nxt_x][nxt_y] > cur_t + 1:
            dist[nxt_x][nxt_y] = cur_t + 1
            heapq.heappush(queue, (cur_t + 1, nxt_x, nxt_y))

        nxt_x, nxt_y = (cur_x + 2) % n, (cur_y) % m
        if matrix[nxt_x][nxt_y] == 0 and matrix[(nxt_x-1) % n][nxt_y] == 0 and dist[nxt_x][nxt_y] > cur_t + 1:
            dist[nxt_x][nxt_y] = cur_t + 1
            heapq.heappush(queue, (cur_t + 1, nxt_x, nxt_y))

    ans = float('inf')
    for x in range(n):
        if dist[x][-1] != float('inf'):
            tmp = (x - dist[x][-1]) % n
            ans = min(ans, dist[x][-1] + min(tmp + 1, n - 1 - tmp))
    print(ans if ans != float('inf') else -1)
    return



if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
