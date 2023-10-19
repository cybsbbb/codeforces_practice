import bisect
import sys
input = sys.stdin.readline


def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))


# range queries and range modifications
class SegTree:
    def __init__(self, defenses):
        self.n = len(defenses)
        self.tree = [0] * (2 * self.n)
        for i in range(self.n):
            self.tree[self.n + i] = defenses[i]
        self.build()
        self.res = 0

    # Build the tree
    def build(self):
        for i in range(self.n-1, -1, -1):
            self.tree[i] = min(self.tree[i << 1], self.tree[i << 1 | 1])

    def attack(self, l, r, val):
        self.res = 0
        l += self.n
        r += self.n
        while l < r:
            if l & 1:
                self.attack_subtree(l, val)
                l += 1
            if r & 1:
                r -= 1
                self.attack_subtree(r, val)
            l >>= 1
            r >>= 1
        return self.res

    def attack_subtree(self, p, val):
        if self.tree[p] > val:
            return
        else:
            if p >= self.n:
                self.res += 1
                self.tree[p] = float('inf')
                self.button_up(p)
            else:
                self.attack_subtree(p << 1, val)
                self.attack_subtree(p << 1 | 1, val)

    def button_up(self, p):
        while p > 1:

            self.tree[p >> 1] = min(self.tree[p], self.tree[p ^ 1])
            p >>= 1


if __name__ == '__main__':
    n = inp()
    defenses = []
    for i in range(n):
        x, d = inlt()
        defenses.append([x, d])
    attacks = []
    m = inp()
    for j in range(m):
        a, b, y = inlt()
        attacks.append([a, b, y])

    defenses.sort()
    defenses_position = []
    defenses_val = []

    for i, (x, d) in enumerate(defenses):
        defenses_position.append(x)
        defenses_val.append(d)

    segtree = SegTree(defenses_val)

    for a, b, y in attacks:
        l = bisect.bisect_left(defenses_position, y-b)
        r = bisect.bisect_right(defenses_position, y+b)
        res = segtree.attack(l, r, a)
        print(res)
