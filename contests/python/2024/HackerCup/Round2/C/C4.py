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


class WaveletTree2D:
    def __init__(self, points, x1, x2, y1, y2):
        self.x1, self.x2 = x1, x2  # x 轴范围
        self.y1, self.y2 = y1, y2  # y 轴范围
        self.points = points  # 当前节点的点集
        self.left = None
        self.right = None
        if x1 == x2 and y1 == y2:
            return
        if x1 == x2:
            y_mid = (y1 + y2) // 2
            left_points = [p for p in points if p[1] <= y_mid]
            right_points = [p for p in points if p[1] > y_mid]
            self.left = WaveletTree2D(left_points, x1, x2, y1, y_mid)
            self.right = WaveletTree2D(right_points, x1, x2, y_mid + 1, y2)
        else:
            x_mid = (x1 + x2) // 2
            left_points = [p for p in points if p[0] <= x_mid]
            right_points = [p for p in points if p[0] > x_mid]
            self.left = WaveletTree2D(left_points, x1, x_mid, y1, y2)
            self.right = WaveletTree2D(right_points, x_mid + 1, x2, y1, y2)

    def query(self, x1_query, x2_query, y1_query, y2_query):
        if self.x2 < x1_query or self.x1 > x2_query or self.y2 < y1_query or self.y1 > y2_query:
            return 0
        if x1_query <= self.x1 and self.x2 <= x2_query and y1_query <= self.y1 and self.y2 <= y2_query:
            return len(self.points)
        res = 0
        if self.left:
            res += self.left.query(x1_query, x2_query, y1_query, y2_query)
        if self.right:
            res += self.right.query(x1_query, x2_query, y1_query, y2_query)
        return res

    def count_equal(self, x1_query, x2_query, y1_query, y2_query, val, grid):
        if not self.points:
            return 0
        if self.x2 < x1_query or self.x1 > x2_query or self.y2 < y1_query or self.y1 > y2_query:
            return 0
        if self.x1 == self.x2 and self.y1 == self.y2:
            x, y = self.points[0]
            return 1 if grid[x][y] == val else 0
        res = 0
        if self.left:
            res += self.left.count_equal(x1_query, x2_query, y1_query, y2_query, val, grid)
        if self.right:
            res += self.right.count_equal(x1_query, x2_query, y1_query, y2_query, val, grid)
        return res


def solution(ttt):
    R, C, K = inlt()
    grid = []
    for _ in range(R):
        grid.append(inlt())

    points = []
    for x in range(R):
        for y in range(C):
            points.append((x, y))
    tree = WaveletTree2D(points, 0, R - 1, 0, C - 1)

    left = 1
    right = max(len(grid), len(grid[0]))

    while left < right:
        mid = (left + right) // 2
        tmp = 0
        for i in range(R):
            for j in range(C):
                val = grid[i][j]
                r1, c1 = max(0, i - mid), max(0, j - mid)
                r2, c2 = min(R - 1, i + mid), min(C - 1, j + mid)
                total_elements = (r2 - r1 + 1) * (c2 - c1 + 1)
                count_equal = tree.count_equal(r1, r2, c1, c2, val, grid)
                tmp += total_elements - count_equal
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
