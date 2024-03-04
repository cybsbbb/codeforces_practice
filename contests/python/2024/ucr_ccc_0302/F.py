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

MOD = 10 ** 9 + 7
class FenwickTree():
    def __init__(self, n):
        self.fenwick = [0] * (n + 1)
        self.n = n

    # def lowbit(self, x):
    #     return x & -x

    def update(self, index, d):
        # index += 1
        while index <= self.n:
            self.fenwick[index] = (self.fenwick[index] + d) % MOD
            # index += self.lowbit(index)
            index += index & -index

    def getsum(self, index):
        # index += 1
        res = 0
        while index > 0:
            res = (res + self.fenwick[index]) % MOD
            # index -= self.lowbit(index)
            index -= index & -index
        return res

    def get_interval(self, left, right):
        return self.getsum(right) - self.getsum(left - 1)


def solution():
    n, q = inlt()

    s = insr()
    fenwick_forward = FenwickTree(n)
    fenwick_backward = FenwickTree(n)

    pows = [1]
    for i in range(n):
        pows.append(pows[-1] * 27 % MOD)

    inv = pow(27, -1, MOD)
    pows_neg = [1]
    for i in range(n):
        pows_neg.append(pows_neg[-1] * inv % MOD)

    for i in range(n):
        fenwick_forward.update(i + 1, (ord(s[i]) - ord('a') + 1) * pows[i + 1])
        fenwick_backward.update(n - i, (ord(s[i]) - ord('a') + 1) * pows[n - i])

    for _ in range(q):
        ind, a, b = input()[:-1].split()
        if ind == '1':
            i = int(a) - 1
            fenwick_forward.update(i + 1, -(ord(s[i]) - ord('a') + 1) * pows[i + 1])
            fenwick_forward.update(i + 1, +(ord(b) - ord('a') + 1) * pows[i + 1])
            fenwick_backward.update(n - i, -(ord(s[i]) - ord('a') + 1) * pows[n - i])
            fenwick_backward.update(n - i, +(ord(b) - ord('a') + 1) * pows[n - i])
            s[i] = b
        else:
            l = int(a)
            r = int(b)
            hash1 = fenwick_forward.get_interval(l, r) * pows_neg[l] % MOD
            hash2 = fenwick_backward.get_interval(n - r + 1, n - l + 1) * pows_neg[n - r + 1] % MOD
            if hash1 == hash2:
                print("Yes")
            else:
                print("No")

    return


if __name__ == '__main__':
    t = 1
    for i in range(t):
        solution()