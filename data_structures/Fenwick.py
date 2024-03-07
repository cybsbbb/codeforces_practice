class FenwickTree():
    def __init__(self, n):
        self.fenwick = [0] * (n + 1)
        self.n = n

    def lowbit(self, x):
        return x & -x

    def update(self, index, d):
        while index <= self.n:
            self.fenwick[index] += d
            index += self.lowbit(index)

    def getsum(self, index):
        res = 0
        while index > 0:
            res += self.fenwick[index]
            index -= self.lowbit(index)
        return res

    def get_interval(self, left, right):
        return self.getsum(right) - self.getsum(left - 1)
