import collections
import sys
import heapq
import math
import bisect


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


class BinaryIndexTree:

    def __init__(self, n):
        self.size = n
        self.tree = [0 for _ in range(n + 1)]

    def lowbit(self, index):
        return index & (-index)

    def update(self, index, delta):
        while index <= self.size:
            self.tree[index] += delta
            index += self.lowbit(index)

    def query(self, index):
        res = 0
        while index > 0:
            res += self.tree[index]
            index -= self.lowbit(index)
        return res


def solution():
    n = inp()
    a = inlt()
    b = inlt()

    if sorted(a) != sorted(b):
        print("NO")
        return

    def reversePairs(nums):
        size = len(nums)
        sort_nums = sorted(nums)
        for i in range(size):
            nums[i] = bisect.bisect_left(sort_nums, nums[i]) + 1
        bit = BinaryIndexTree(size)
        ans = 0
        for i in range(size):
            bit.update(nums[i], 1)
            ans += (i + 1 - bit.query(nums[i]))
        return ans

    reverse_a = reversePairs(a)
    reverse_b = reversePairs(b)
    if reverse_a % 2 != reverse_b % 2:
        print("NO")
    else:
        print("YES")

    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()





