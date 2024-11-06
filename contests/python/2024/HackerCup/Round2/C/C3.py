import sys
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


class NodeY:
    def __init__(self, y1, y2, data):
        self.y1 = y1
        self.y2 = y2
        self.left = None
        self.right = None
        self.data = data  # list of (y_index, value)
        self.values = sorted([v for idx, v in data])
        if y1 != y2:
            y_mid = (y1 + y2) // 2
            left_data = [(idx, v) for idx, v in data if y1 <= idx <= y_mid]
            right_data = [(idx, v) for idx, v in data if y_mid + 1 <= idx <= y2]
            self.left = NodeY(y1, y_mid, left_data)
            self.right = NodeY(y_mid + 1, y2, right_data)

    @staticmethod
    def merge(left_y_tree, right_y_tree):
        node = NodeY(left_y_tree.y1, right_y_tree.y2, [])
        node.left = left_y_tree
        node.right = right_y_tree
        node.data = left_y_tree.data + right_y_tree.data
        node.values = sorted([v for idx, v in node.data])
        return node

    def query(self, y1_query, y2_query, val):
        if self.y2 < y1_query or self.y1 > y2_query:
            return 0
        if y1_query <= self.y1 and self.y2 <= y2_query:
            # Total elements in this node
            total_elements = len(self.values)
            # Number of elements equal to val
            left = bisect_left(self.values, val)
            right = bisect_right(self.values, val)
            count_equal = right - left
            # Return number of elements not equal to val
            return total_elements - count_equal
        res = 0
        if self.left:
            res += self.left.query(y1_query, y2_query, val)
        if self.right:
            res += self.right.query(y1_query, y2_query, val)
        return res


class NodeX:
    def __init__(self, x1, x2, grid):
        self.x1 = x1
        self.x2 = x2
        self.left = None
        self.right = None
        if x1 == x2:
            # Leaf node over x
            data = [(y, grid[x1][y]) for y in range(len(grid[0]))]
            self.y_tree = NodeY(0, len(grid[0]) - 1, data)
        else:
            x_mid = (x1 + x2) // 2
            self.left = NodeX(x1, x_mid, grid)
            self.right = NodeX(x_mid + 1, x2, grid)
            self.y_tree = NodeY.merge(self.left.y_tree, self.right.y_tree)

    def query(self, x1_query, x2_query, y1_query, y2_query, val):
        if self.x2 < x1_query or self.x1 > x2_query:
            return 0
        if x1_query <= self.x1 and self.x2 <= x2_query:
            return self.y_tree.query(y1_query, y2_query, val)
        res = 0
        if self.left:
            res += self.left.query(x1_query, x2_query, y1_query, y2_query, val)
        if self.right:
            res += self.right.query(x1_query, x2_query, y1_query, y2_query, val)
        return res


def solution(ttt):
    R, C, K = inlt()
    grid = []
    for _ in range(R):
        grid.append(inlt())
    tree = NodeX(0, len(grid) - 1, grid)

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
