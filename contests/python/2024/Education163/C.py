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
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    first_row = input()[:-1]
    second_row = input()[:-1]
    grid = list(zip(first_row, second_row))
    dp = [[False] * 2 for _ in range(n)]
    dp[0][0] = True
    queue = collections.deque()
    queue.append((0, 0))
    while queue:
        cur_x, cur_y = queue.popleft()
        for dx, dy in directions:
            nxt_x, nxt_y = cur_x + dx, cur_y + dy
            if 0 <= nxt_x < n and 0 <= nxt_y <= 1:
                if grid[nxt_x][nxt_y] == '<':
                    nxt_x -= 1
                else:
                    nxt_x += 1
                if dp[nxt_x][nxt_y] is False:
                    dp[nxt_x][nxt_y] = True
                    queue.append((nxt_x, nxt_y))

    if dp[-1][-1] is True:
        print("YES")
    else:
        print("NO")
    return



if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
