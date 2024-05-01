import collections
import itertools
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


def cross_product(p1, p2):
    return p1[0] * p2[1] - p1[1] * p2[0]

n = inp()
a = inlt()
b = [0] + list(itertools.accumulate(a))
convex_hull = []
convex_hull.append((n, b[n]))
convex_hull.append((n - 1, b[n - 1]))
ans = [a[-1]]
for i in range(n - 2, -1, -1):
    p0 = (i, b[i])
    while len(convex_hull) >= 2:    
        p1 = convex_hull[-1]
        p2 = convex_hull[-2]
        if cross_product((p1[0] - p2[0], p1[1] - p2[1]), (p0[0] - p1[0], p0[1] - p1[1])) < 0:
            convex_hull.pop()
        else:
            break
    convex_hull.append(p0)
    ans.append((convex_hull[-2][1] - convex_hull[-1][1]) / (convex_hull[-2][0] - convex_hull[-1][0]))

for i in range(n - 1, -1, -1):
    print(ans[i])
