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
    n, q = inlt()
    matrix = []
    for i in range(n):
        matrix.append(input()[:-1])


    prefix_row = [[0] * (n + 1) for i in range(n + 1)]
    prefix_col = [[0] * (n + 1) for i in range(n + 1)]
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 'B':
                prefix_row[i][j] = prefix_row[i][j - 1] + 1
                prefix_col[i][j] = prefix_col[i - 1][j] + 1
            else:
                prefix_row[i][j] = prefix_row[i][j - 1]
                prefix_col[i][j] = prefix_col[i - 1][j]

    prefix_tot = [[0] * (n + 1) for i in range(n + 1)]
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 'B':
                prefix_tot[i][j] = prefix_tot[i - 1][j - 1] + prefix_row[i][j] + prefix_col[i][j] - 1
            else:
                prefix_tot[i][j] = prefix_tot[i - 1][j - 1] + prefix_row[i][j] + prefix_col[i][j]

    tot_black = prefix_tot[n - 1][n - 1]

    def left_top(i, j):
        if i < 0 or j < 0:
            return 0
        ans = 0
        ans += tot_black * (i // n) * (j // n)
        ans += prefix_tot[n - 1][j % n] * (i // n)
        ans += prefix_tot[i % n][n - 1] * (j // n)
        ans += prefix_tot[i % n][j % n]
        return ans

    for _ in range(q):
        a, b, c, d = inlt()
        ans = left_top(c, d) - left_top(a - 1, d) - left_top(c, b - 1) + left_top(a - 1, b - 1)
        print(ans)
    return


if __name__ == '__main__':
    t = 1
    for i in range(t):
        solution()