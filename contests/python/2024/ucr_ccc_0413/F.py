import collections
import sys
import math
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



def build(arr):
    for i in range(n):
        tree[n + i] = arr[i];
    for i in range(n - 1, 0, -1):
        tree[i] = tree[i << 1] + tree[i << 1 | 1]


def updateTreeNode(p, value):
    tree[p + n] = value
    p = p + n
    i = p
    while i > 1:
        tree[i >> 1] = tree[i] + tree[i ^ 1]
        i >>= 1


def query(l, r):
    res = 0
    l += n
    r += n
    while l < r:
        if (l & 1):
            res += tree[l]
            l += 1
        if (r & 1):
            r -= 1
            res += tree[r]
        l >>= 1
        r >>= 1
    return res


n, q = inlt()
s = input()[:-1]

tree = [0] * (2 * n)

for i in range()
