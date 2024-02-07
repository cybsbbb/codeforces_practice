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
    h, w = inlt()
    grid = []

    n = h * w
    parent = [i for i in range(n)]
    tot_union_cnt = [0]
    def find(x):
        x_copy = x
        while x != parent[x]:
            x = parent[x]
        while x_copy != x:
            parent[x_copy], x_copy = x, parent[x_copy]
        return x
    def union(a, b):
        a, b = find(a), find(b)
        if a != b:
            tot_union_cnt[0] -= 1
            parent[a] = b

    for _ in range(h):
        grid.append(insr())

    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    for i in range(h):
        for j in range(w):
            if grid[i][j] == '#':
                tot_union_cnt[0] += 1
                for di, dj in directions:
                    ii, jj = i + di, j + dj
                    if 0 <= ii < h and 0 <= jj < w and grid[ii][jj] == '#':
                        union(ii * w + jj, i * w + j)

    ans = 0
    tot_red_cnt = 0
    for i in range(h):
        for j in range(w):
            if grid[i][j] == '.':
                tot_red_cnt += 1
                parents = set()
                for di, dj in directions:
                    ii, jj = i + di, j + dj
                    if 0 <= i + di < h and 0 <= j + dj < w and grid[i + di][j + dj] == '#':
                        parents.add(find(ii * w + jj))
                if len(parents) == 0:
                    ans += tot_union_cnt[0] + 1
                else:
                    ans += tot_union_cnt[0] - (len(parents) - 1)

    MOD = 998244353
    divides = pow(tot_red_cnt, MOD-2, MOD)
    ans = (ans * divides) % MOD
    print(ans)
    return


if __name__ == '__main__':
    t = 1
    for i in range(t):
        solution()
