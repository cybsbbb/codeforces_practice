import sys

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
    n, q = inlt()
    a = inlt()
    b = inlt()
    c = inlt()
    sum_a = sum(a)

    seg_tree = SegTree(n + 1, update_func, query_func)

    suffix = [0]
    for i in range(n)[::-1]:
        suffix.append(suffix[-1] + (a[i] - b[i]))
        seg_tree.update(i, i + 1, suffix[-1])

    for i in range(q):
        p, x, y, z = inlt()
        p -= 1
        pre_val = a[p] - b[p]
        sum_a = sum_a - a[p] + x
        a[p] = x
        b[p] = y
        cur_val = a[p] - b[p]
        seg_tree.update(0, p + 1, cur_val - pre_val)
        ans = sum_a - seg_tree.query(0, n)
        print(ans)

    return


if __name__ == '__main__':
    t = 1
    for i in range(t):
        solution()