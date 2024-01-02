import collections
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


class Fenwick:
    def __init__(self, n):
        self.bit = [0] * (n + 1)
        self.n = n

    def update(self, idx, val):
        idx += 1
        while idx <= self.n:
            self.bit[idx] += val
            idx += idx & (-idx)

    def prefixSum(self, idx):
        idx += 1
        ans = 0
        while idx > 0:
            ans += self.bit[idx]
            idx -= idx & (-idx)
        return ans

    def rangeSum(self, l, r):
        if l > r:
            return 0
        else:
            return self.prefixSum(r) - self.prefixSum(l - 1)


MOD = 998244353


def solution():
    n, k = inlt()
    p = inlt()
    q = inlt()

    # Get the inversion in the q
    fenwick_q = Fenwick(k)
    inversion_q = 0
    for i in range(k):
        inversion_q += (i - fenwick_q.prefixSum(q[i]))
        fenwick_q.update(q[i], 1)
    ans = (inversion_q * n) % MOD

    between_p = {}
    for d in range(-19, 20):
        if d < 0:
            if k + d - 1 >= 0:
                between_p[d] = k * k - (k + d) * (k + d - 1) // 2
            else:
                between_p[d] = k * k
        else:
            if k >= d:
                between_p[d] = (k - d) * (k - d + 1) // 2
            else:
                between_p[d] = 0

    fenwick_p = Fenwick(2 * n)
    for i in range(n):
        for d in range(-19, 20):
            if d == 0:
                lower = p[i]
                upper = 2 * p[i]
            elif d < 0:
                lower = p[i] << (-d)
                upper = p[i] << (-d + 1)
            else:
                lower = p[i] >> d
                upper = p[i] >> (d - 1)
            if lower >= 2 * n or upper == 0:
                continue
            quantity = fenwick_p.rangeSum(lower + 1, min(2*n - 1, upper))
            ans += quantity * between_p[d]
            ans %= MOD
        fenwick_p.update(p[i], 1)

    print(ans)
    return 0


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()


