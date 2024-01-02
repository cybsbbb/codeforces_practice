import collections
import math
import sys
import heapq

input = sys.stdin.readline

# https://codeforces.com/contest/1916/submission/239765768


def inp():
    return (int(input()))
def inlt():
    return (list(map(int, input().split())))
def insr():
    s = input()
    return (list(s[:len(s) - 1]))
def invr():
    return (map(int, input().split()))


class SegTree:
    def __init__(self, n, update_func, query_func):
        self.n = n
        self.h = 1
        while 1 << self.h < n:
            self.h += 1
        self.update_func = update_func
        self.query_func = query_func
        self.tree = [0] * (2 * self.n)
        self.lazy = [0] * (self.n)

    def _apply(self, p, val):
        self.tree[p] = self.update_func(self.tree[p], val)
        if p < self.n:
            self.lazy[p] = self.update_func(self.lazy[p], val)

    def _pull(self, p):
        while p > 1:
            p >>= 1
            self.tree[p] = self.query_func(self.tree[p << 1], self.tree[p << 1 | 1])
            self.tree[p] = self.update_func(self.tree[p], self.lazy[p])

    def _push(self, p):
        for s in range(self.h, 0, -1):
            i = p >> s
            if self.lazy[i]:
                self._apply(i << 1, self.lazy[i])
                self._apply(i << 1 | 1, self.lazy[i])
                self.lazy[i] = 0

    def update(self, l, r, val):
        l += self.n
        r += self.n
        l0, r0 = l, r
        while l < r:
            if l & 1:
                self._apply(l, val)
                l += 1
            if r & 1:
                r -= 1
                self._apply(r, val)
            l >>= 1
            r >>= 1
        self._pull(l0)
        self._pull(r0 - 1)

    def query_single(self, p):
        self._push(p)
        return self.tree[p]

    def query(self, l, r):
        l += self.n
        r += self.n
        self._push(l)
        self._push(r)
        res = 0
        while l < r:
            if l & 1:
                res = self.query_func(res, self.tree[l])
                l += 1
            if r & 1:
                r -= 1
                res = self.query_func(res, self.tree[r])
            l >>= 1
            r >>= 1
        return res


def update_func(a, b):
    return a + b


def query_func(a, b):
    return max(a, b)


def solution():
    n = inp()
    parents = [0] + inlt()
    colors = [0] + inlt()
    children = [[] for _ in range(n + 1)]
    for i in range(1, n):
        children[parents[i]].append(i + 1)
    seg_tree = SegTree(n + 2, update_func, query_func)
    ans = [1]
    clock = [0]
    prev_color_node = [0] * (n + 1)
    nxt_color_node = [[] for _ in range(n + 1)]
    in_clock = [0] * (n + 1)
    out_clock = [0] * (n + 1)

    def dfs(u):
        clock[0] += 1
        in_clock[u] = clock[0]
        # If current color appeared before
        if prev_color_node[colors[u]]:
            nxt_color_node[prev_color_node[colors[u]]].append(u)
        tmp = prev_color_node[colors[u]]
        prev_color_node[colors[u]] = u
        for child in children[u]:
            dfs(child)
        out_clock[u] = clock[0]
        prev_color_node[colors[u]] = tmp
        seg_tree.update(in_clock[u], out_clock[u] + 1, 1)
        for v in nxt_color_node[u]:
            seg_tree.update(in_clock[v], out_clock[v] + 1, -1)
        mx = 1
        for v in children[u]:
            t = seg_tree.query(in_clock[v], out_clock[v] + 1)
            ans[0] = max(ans[0], t * mx)
            mx = max(mx, t)

    dfs(1)
    print(ans[0])
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()