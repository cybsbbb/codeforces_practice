import sys
import collections
import heapq
from bisect import bisect_left, bisect_right

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


class SegmentTree2D:
    def __init__(self, matrix):
        self.R = len(matrix)
        self.C = len(matrix[0]) if self.R else 0
        self.N = 1
        while self.N < self.R:
            self.N *= 2
        self.M = 1
        while self.M < self.C:
            self.M *= 2

        # 初始化线段树，创建一个二维列表
        self.tree = [[{} for _ in range(2 * self.M)] for _ in range(2 * self.N)]

        # 构建线段树的叶节点
        for i in range(self.R):
            for j in range(self.C):
                x = i + self.N
                y = j + self.M
                val = matrix[i][j]
                self.tree[x][y][val] = self.tree[x][y].get(val, 0) + 1

        # 构建每一行的线段树（y方向）
        for x in range(self.N, 2 * self.N):
            for y in range(self.M - 1, 0, -1):
                left_child = self.tree[x][y * 2]
                right_child = self.tree[x][y * 2 + 1]
                self.tree[x][y] = self._merge_dicts(left_child, right_child)

        # 构建每一列的线段树（x方向）
        for x in range(self.N - 1, 0, -1):
            for y in range(1, 2 * self.M):
                left_child = self.tree[x * 2][y]
                right_child = self.tree[x * 2 + 1][y]
                self.tree[x][y] = self._merge_dicts(left_child, right_child)

    def _merge_dicts(self, dict1, dict2):
        result = dict1.copy()
        for k, v in dict2.items():
            result[k] = result.get(k, 0) + v
        return result

    def query(self, r1, c1, r2, c2, val):
        # 将索引调整为叶节点的起始位置
        r1 += self.N
        r2 += self.N + 1
        c1 += self.M
        c2 += self.M + 1
        res = 0
        total_elements = (r2 - r1) * (c2 - c1)

        r_start, r_end = r1, r2
        while r1 < r2:
            if r1 % 2 == 1:
                res += self._query_y(r1, c1, c2, val)
                r1 += 1
            if r2 % 2 == 1:
                r2 -= 1
                res += self._query_y(r2, c1, c2, val)
            r1 //= 2
            r2 //= 2
        return total_elements - res

    def _query_y(self, x, c1, c2, val):
        res = 0
        while c1 < c2:
            if c1 % 2 == 1:
                res += self.tree[x][c1].get(val, 0)
                c1 += 1
            if c2 % 2 == 1:
                c2 -= 1
                res += self.tree[x][c2].get(val, 0)
            c1 //= 2
            c2 //= 2
        return res


def solution(ttt):
    R, C, K = inlt()
    grid = []
    for _ in range(R):
        grid.append(inlt())
    tree = SegmentTree2D(grid)

    left = 1
    right = max(len(grid), len(grid[0])) - 1

    while left < right:
        mid = (left + right) // 2
        tmp = 0
        for i in range(R):
            for j in range(C):
                val = grid[i][j]
                r1, c1 = max(0, i - mid), max(0, j - mid)
                r2, c2 = min(R - 1, i + mid), min(C - 1, j + mid)
                tmp += tree.query(r1, r2, c1, c2, val)
        if tmp < K:
            left = mid + 1
        else:
            right = mid

    print(f"Case #{ttt}: {left}")
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution(i + 1)
