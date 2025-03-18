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
    magic = ['1', '5', '4', '3']
    layers = min(n // 2, m // 2)
    ans = 0
    for i in range(layers):
        cur_layer = []
        cur_x, cur_y = i, i
        for dy in range(m - 2 * i - 1):
            cur_layer.append(grid[cur_x][cur_y + dy])
        cur_y += (m - 2 * i - 1)
        for dx in range(n - 2 * i - 1):
            cur_layer.append(grid[cur_x + dx][cur_y])
        cur_x += (n - 2 * i - 1)
        for dy in range(m - 2 * i - 1):
            cur_layer.append(grid[cur_x][cur_y - dy])
        cur_y -= (m - 2 * i - 1)
        for dx in range(n - 2 * i - 1):
            cur_layer.append(grid[cur_x - dx][cur_y])
        cur_x -= (n - 2 * i - 1)
        k = len(cur_layer)
        cur_layer += cur_layer[:3]
        for j in range(k):
            if cur_layer[j: j + 4] == magic:
                ans += 1
    print(ans)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
