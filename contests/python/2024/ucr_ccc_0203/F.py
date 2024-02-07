import bisect
import collections
import math
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






def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def solution():
    n, k = inlt()
    santa_point = inlt()
    points = []
    for i in range(n):
        points.append(inlt())

    ans = 0
    for i in range(1, n):
        ans += distance(points[i], points[i - 1])
    ans += distance(santa_point, points[0])
    ans += distance(santa_point, points[-1])

    tree = [0] * (2 * n + 2)
    def build(arr):
        for i in range(n):
            tree[n + i] = arr[i]
        for i in range(n - 1, 0, -1):
            tree[i] = min(tree[i << 1], tree[i << 1 | 1])
    def updateTreeNode(p, value):
        tree[p + n] = value
        p = p + n
        i = p
        while i > 1:
            tree[i >> 1] = min(tree[i], tree[i ^ 1])
            i >>= 1
    def query(l, r):
        res = float('inf')
        l += n
        r += n
        while l < r:
            if (l & 1):
                res = min(res, tree[l])
                l += 1
            if (r & 1):
                r -= 1
                res = min(res, tree[r])
            l >>= 1
            r >>= 1
        return res

    for i in range(1, n):
        cur_val = query(max(0, i - k), i) + distance(santa_point, points[i - 1]) + distance(santa_point, points[i]) - distance(points[i - 1], points[i])
        updateTreeNode(i, cur_val)

    ans += query(max(0, n - k), n)
    print(ans)
    return


if __name__ == '__main__':
    t = 1
    for i in range(t):
        solution()
