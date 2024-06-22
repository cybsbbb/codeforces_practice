import collections
import sys
import heapq
import math

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
    grid = []
    for _ in range(n):
        grid.append(input()[:-1])
    max_cnt = 0
    max_idx = -1
    for i in range(n):
        cur_cnt = grid[i].count('#')
        if cur_cnt > max_cnt:
            max_cnt = cur_cnt
            max_idx = i
    col = 0
    for j in range(m):
        if grid[max_idx][j] == '#':
            col = j
            break
    col += max_cnt // 2

    print(max_idx + 1, col + 1)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()





