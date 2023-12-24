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

def lowbit(x):
    return x & -x

def update(index, d, tree):
    while index < len(tree):
        tree[index] += d
        index += lowbit(index)

def getsum(index, tree):
    res = 0
    while index > 0:
        res += tree[index]
        index -= lowbit(index)
    return res

def getsum_range(left, right, tree):
    res = 0 if left > right else getsum(right, tree) - getsum(left - 1, tree)
    return res


def solution():
    n, m = inlt()
    s = insr()
    s = [0] + [ord(i) - 97 for i in s]
    # x is the diff between s[i] and s[i+1]
    x = [-1] * (n + 1)
    for i in range(1, n):
        x[i] = (s[i + 1] - s[i]) % 26
    # y is the diff between s[i] and s[i+2]
    y = [-1] * (n + 1)
    for i in range(1, n - 1):
        y[i] = (s[i + 2] - s[i]) % 26
    # Fenwick tree of x and y, build the fenwick tree
    tree1 = [0] * (n + 5)
    tree2 = [0] * (n + 5)
    for i in range(1, n):
        if not x[i]:
            tree1[i] = 1
        if not y[i]:
            tree2[i] = 1
    for i in range(1, n + 5):
        j = i + lowbit(i)
        if j < n + 5:
            tree1[j] += tree1[i]
            tree2[j] += tree2[i]
    for _ in range(m):
        t = inlt()
        l, r = t[1], t[2]
        if t[0] == 1:
            u = t[3] % 26
            if not u:
                continue
            for i in [l-1, r]:
                d = u if i < l else -u
                if not 1 <= i < n:
                    continue
                if not x[i]:
                    update(i, -1, tree1)
                x[i] = (x[i] + d) % 26
                if not x[i]:
                    update(i, 1, tree1)
            z = [l - 2, l - 1, r - 1, r] if l != r else [l-2, r]
            for i in z:
                d = u if i < l else -u
                if not 1 <= i < n-1:
                    continue
                if not y[i]:
                    update(i, -1, tree2)
                y[i] = (y[i] + d) % 26
                if not y[i]:
                    update(i, 1, tree2)
        else:
            c = getsum_range(l, r - 1, tree1) + getsum_range(l, r - 2, tree2)
            ans = "YES" if not c else "NO"
            print(ans)


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
