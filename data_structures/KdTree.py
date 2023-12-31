import sys
import math
import heapq
input = sys.stdin.readline


class KdTree():
    def __init__(self, points):
        self.d = len(points[0])
        self.n = len(points)
        self.tree = [None] * self.n
        self.build_tree(points, 0, 0, self.n - 1)

    def build_tree(self, points, depth, left, right):
        if left > right:
            return
        dimension = depth % self.d
        points[left: right + 1] = sorted(points[left: right + 1], key=lambda X: X[dimension])
        mid = (left + right) // 2
        self.tree[mid] = points[mid]
        self.build_tree(points, depth + 1, left, mid - 1)
        self.build_tree(points, depth + 1, mid + 1, right)
        return

    def query(self, query_point, heap, k, depth, left, right):
        if left > right:
            return
        dimension = depth % self.d
        # mid
        mid = (left + right) // 2
        mid_dist = sum((x1 - x2) ** 2 for x1, x2 in zip(query_point, self.tree[mid]))
        heapq.heappush(heap, -mid_dist)
        if len(heap) > k:
            heapq.heappop(heap)
        # left
        if query_point[dimension] <= self.tree[mid][dimension]:
            self.query(query_point, heap, k, depth + 1, left, mid - 1)
            if len(heap) < k or (query_point[dimension] - self.tree[mid][dimension]) ** 2 <= -heap[0]:
                self.query(query_point, heap, k, depth + 1, mid + 1, right)
        # right
        else:
            self.query(query_point, heap, k, depth + 1, mid + 1, right)
            if len(heap) < k or (query_point[dimension] - self.tree[mid][dimension]) ** 2 <= -heap[0]:
                self.query(query_point, heap, k, depth + 1, left, mid - 1)


n, d = list(map(int, input().split()))
points = []
for _ in range(n):
    point = list(map(float, input().split()))
    points.append(point)

tree = KdTree(points)

q = int(input())
for _ in range(q):
    query = input().split()
    k = int(query[0])
    query_point = list(map(float, query[1:]))
    heap = []
    tree.query(query_point, heap, k, 0, 0, len(points) - 1)
    print(math.sqrt(-heap[0]))
