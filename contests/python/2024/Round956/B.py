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
    a = []
    b = []
    for _ in range(n):
        a.append(input()[:-1])
    for _ in range(n):
        b.append(input()[:-1])

    rows_a = [0] * n
    cols_a = [0] * m
    rows_b = [0] * n
    cols_b = [0] * m
    for i in range(n):
        for j in range(m):
            rows_a[i] += int(a[i][j])
            cols_a[j] += int(a[i][j])
            rows_b[i] += int(b[i][j])
            cols_b[j] += int(b[i][j])

    for i in range(n):
        rows_a[i] = rows_a[i] % 3
        rows_b[i] = rows_b[i] % 3

    for j in range(m):
        cols_a[j] = cols_a[j] % 3
        cols_b[j] = cols_b[j] % 3

    if rows_a == rows_b and cols_a == cols_b:
        print("YES")
    else:
        print("NO")

    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()





