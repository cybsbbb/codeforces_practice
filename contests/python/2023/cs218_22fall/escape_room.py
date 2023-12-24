import bisect
import sys
input = sys.stdin.readline


def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))


# range queries and range modifications
class SegTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (2 * self.n)

    def increment(self, l, r, val):
        l += self.n
        r += self.n
        while l < r:
            if l & 1:
                self.tree[l] += val
                l += 1
            if r & 1:
                r -= 1
                self.tree[r] += val
            l >>= 1
            r >>= 1

    def push(self):
        for i in range(1, self.n):
            self.tree[i << 1] += self.tree[i]
            self.tree[i << 1 | 1] += self.tree[i]
            self.tree[i] = 0

    def globle_min(self):
        self.push()
        return min(self.tree[self.n:])


def point_2_idx(x, y, l):
    if y == 0:
        return x
    elif x == l:
        return l + y
    elif y == l:
        return 3 * l - x
    else:
        return 4 * l - y


def idx_2_point(idx, l):
    line = idx // l
    remain = idx % l
    if line == 0:
        return remain, 0
    elif line == 1:
        return l, remain
    elif line == 2:
        return l-remain, l
    else:
        return 0, l-remain


def line_side(x1, y1, x2, y2, x3, y3):
    return (x3 - x1) * (y2 - y1) - (y3 - y1) * (x2 - x1) > 0


if __name__ == '__main__':
    n, l = inlt()
    segtree = SegTree(8*l)
    lines = []
    for i in range(n):
        lines.append(inlt())

    x3, y3 = (list(map(float, input().split())))

    for x1, y1, x2, y2 in lines:
        idx1 = point_2_idx(x1, y1, l)
        idx2 = point_2_idx(x2, y2, l)
        if idx1 > idx2:
            idx1, idx2 = idx2, idx1
        idx_tmp = (idx1 + 1) % (4 * l)
        x_tmp, y_tmp = idx_2_point(idx_tmp, l)

        if line_side(x1, y1, x2, y2, x3, y3) == line_side(x1, y1, x2, y2, x_tmp, y_tmp):
            segtree.increment(0, idx1 * 2 + 1, 1)
            segtree.increment(idx2 * 2, l * 8, 1)
        else:
            segtree.increment(idx1 * 2, idx2 * 2 + 1, 1)

    print(segtree.globle_min() + 1)
