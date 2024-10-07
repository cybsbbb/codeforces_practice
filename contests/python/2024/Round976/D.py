import bisect
import collections
import sys
import heapq
import math

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


def find(x, parent):
    x_copy = x
    while x != parent[x]:
        x = parent[x]
    while x_copy != x:
        parent[x_copy], x_copy = x, parent[x_copy]
    return x


def union(a, b, parent, size):
    a, b = find(a, parent), find(b, parent)
    if a != b:
        size[0] -= 1
        parent[a] = b


def solution():
    n, m = inlt()
    ranges = collections.defaultdict(list)
    for _ in range(m):
        ai, di, ki = inlt()
        ranges[(ai % di, di)].append([ai, ai + ki * di])

    ranges_nxt = collections.defaultdict(list)
    for key, intervals in ranges.items():
        intervals.sort()
        nxt_interval = []
        cur_interval = intervals[0]
        for interval in intervals[1:]:
            if interval[0] <= cur_interval[1]:
                cur_interval[1] = max(cur_interval[1], interval[1])
            else:
                nxt_interval.append(cur_interval)
                cur_interval = interval
        nxt_interval.append(cur_interval)
        ranges_nxt[key] = nxt_interval

    parent = list(range(n + 1))
    size = [n]

    for i in range(1, n + 1):
        for d in range(1, 11):
            if i - d <= 0:
                break
            key = (i % d, d)
            if key in ranges_nxt:
                idx = bisect.bisect_left(ranges_nxt[key], [i, 10 ** 18])
                if idx > 0 and ranges_nxt[key][idx - 1][1] >= i:
                    union(i, ranges_nxt[key][idx - 1][0], parent, size)

    print(size[0])
    return



if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
