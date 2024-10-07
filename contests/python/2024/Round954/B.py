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
    matrix = []
    for _ in range(n):
        matrix.append(inlt())
    neighbor = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    for i in range(n):
        for j in range(m):
            max_neighbor = -1
            for di, dj in neighbor:
                ii, jj = i + di, j + dj
                if 0 <= ii < n and 0 <= jj < m:
                    max_neighbor = max(max_neighbor, matrix[ii][jj])
            if max_neighbor > 0 and matrix[i][j] > max_neighbor:
                matrix[i][j] = max_neighbor

    for i in range(n):
        print(*matrix[i])
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()





