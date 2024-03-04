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
                prefix_col[i][j] = prefix_col[i - 1][j - 1]

    prefix_tot = [[0] * (n + 1) for i in range(n + 1)]
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 'B':
                prefix_tot[i][j] = prefix_tot[i - 1][j - 1] + prefix_row[i][j] + prefix_col[i][j] - 1
            else:
                prefix_tot[i][j] = prefix_tot[i - 1][j - 1] + prefix_row[i][j] + prefix_col[i][j]

    for _ in range(q):
        a, b, c, d = inlt()
        ans = 0
        top_idx = a // n
        down_idx = (c - 1) // n + 1
        left_idx = b // n
        right_idx = (d - 1) // n + 1
        tot_black = prefix_tot[n - 1][n - 1]
        ans += tot_black * (down_idx - top_idx) * (right_idx - left_idx)

        top_remain = a % n
        down_remain = n - 1 - c % n
        left_remain = b % n
        right_remain = n - 1 - d % n

        ans -= prefix_tot[top_remain - 1][n - 1] * (right_idx - left_idx)
        ans -= (tot_black - prefix_tot[n - 1 - down_remain][n - 1]) * (right_idx - left_idx)

        ans -= prefix_tot[n - 1][left_remain - 1] * (down_idx - top_idx)
        ans -= (tot_black - prefix_tot[n - 1][n - 1 - right_remain]) * (down_idx - top_idx)

        ans += prefix_tot[top_remain - 1][left_remain - 1]
        ans += prefix_tot[top_remain - 1][n - 1] - prefix_tot[top_remain - 1][n - 1 - right_remain]
        ans += prefix_tot[n - 1][left_remain - 1] - prefix_tot[n - 1 - down_remain][left_remain - 1]
        ans += tot_black - prefix_tot[n - 1 - down_remain][n - 1] - prefix_tot[n - 1][n - 1 - right_remain] + prefix_col[n - 1 - down_remain][n - 1 - right_remain]

        print(ans)

    return

# WWBWWB
# BBWBBW
# WBWWBW
# WWBWWB
# BBWBBW
# WBWWBW



if __name__ == '__main__':
    t = 1
    for i in range(t):
        solution()
