import collections
import sys
import heapq
from functools import cache

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


class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.arr = arr
        self.tree = [{} for _ in range(4 * self.n)]
        self.build(0, 0, self.n - 1)

    def build(self, node, start, end):
        if start == end:
            # Leaf node, just count the occurrence of the element
            self.tree[node] = {self.arr[start]: 1}
        else:
            mid = (start + end) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2
            # Build left and right children
            self.build(left_child, start, mid)
            self.build(right_child, mid + 1, end)
            # Merge child dictionaries
            self.tree[node] = self.merge_counts(self.tree[left_child], self.tree[right_child])

    def merge_counts(self, left_dict, right_dict):
        merged = left_dict.copy()
        for key, value in right_dict.items():
            if key in merged:
                merged[key] += value
            else:
                merged[key] = value
        return merged

    def update(self, index, value, node=0, start=0, end=None):
        if end is None:
            end = self.n - 1
        if start == end:
            # Leaf node update
            old_value = self.arr[index]
            self.arr[index] = value
            self.tree[node] = {value: 1}
        else:
            mid = (start + end) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2

            if start <= index <= mid:
                self.update(index, value, left_child, start, mid)
            else:
                self.update(index, value, right_child, mid + 1, end)

            self.tree[node] = self.merge_counts(self.tree[left_child], self.tree[right_child])

    def query(self, L, R, target, node=0, start=0, end=None):
        if end is None:
            end = self.n - 1

        # Completely outside the range
        if R < start or L > end:
            return 0

        # Completely inside the range
        if L <= start and end <= R:
            total_count = (end - start + 1)
            target_count = self.tree[node].get(target, 0)
            return total_count - target_count

        # Partial overlap
        mid = (start + end) // 2
        left_child = 2 * node + 1
        right_child = 2 * node + 2

        left_query = self.query(L, R, target, left_child, start, mid)
        right_query = self.query(L, R, target, right_child, mid + 1, end)

        return left_query + right_query


# arr = [1, 2, 3, 4, 2]
# st = SegmentTree(arr)
# st.update(1, 5)  # 将 arr[2] 更新为 5
# result = st.query(0, 4, 2)  # 查询区间 [1, 4] 中不等于 2 的个数
# print(result)


def solution(ttt):
    R, C, K = inlt()
    matrix = []




if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution(i + 1)
