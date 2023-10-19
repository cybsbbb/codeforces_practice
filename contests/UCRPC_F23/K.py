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
    N, M, x, y = inlt()
    graph = []
    x -= 1
    y -= 1
    for i in range(N):
        graph.append(insr())
    instrctions = []
    for _ in range(M):
        instrctions.append(input()[:-1])
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    dp = collections.defaultdict(int)
    dp[(x, y, 0)] = 0
    for instrction in instrctions:
        dp_nxt = dp.copy()
        for cur_x, cur_y, cur_dir in list(dp.keys()):
            nxt_x, nxt_y, nxt_dir = cur_x, cur_y, cur_dir
            if instrction == 'FORWARD':
                nxt_x, nxt_y = cur_x + directions[cur_dir][0], cur_y + directions[cur_dir][1]
                if nxt_x < 0 or nxt_x >= N or nxt_y < 0 or nxt_y >= N or graph[nxt_x][nxt_y] == "*":
                    continue
            if instrction == 'BACK':
                nxt_x, nxt_y = cur_x - directions[cur_dir][0], cur_y - directions[cur_dir][1]
                if nxt_x < 0 or nxt_x >= N or nxt_y < 0 or nxt_y >= N or graph[nxt_x][nxt_y] == "*":
                    continue
            if instrction == 'LEFT':
                nxt_dir = (cur_dir + 1) % 4
            if instrction == 'RIGHT':
                nxt_dir = (cur_dir + 3) % 4
            dp_nxt[(nxt_x, nxt_y, nxt_dir)] = max(dp_nxt[(nxt_x, nxt_y, nxt_dir)], dp[(cur_x, cur_y, cur_dir)] + 1)
        dp = dp_nxt
    print(M - max(dp.values()))
    return


if __name__ == '__main__':
    t = 1
    for i in range(t):
        solution()
