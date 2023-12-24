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


def solution():
    n, m = inlt()
    intervals = []
    for _ in range(n):
        intervals.append(inlt())

    res = -1

    points = []
    for i in range(n):
        l, r = intervals[i]
        if l != 1:
            points.append((l, 1))
            points.append((r+1, -1))
    points.sort()
    cur_pos, cur_val = -1, 0
    for pos, val in points[:]:
        if pos == cur_pos or pos < 0:
            cur_val += val
        else:
            res = max(res, cur_val)
            cur_pos = pos
            cur_val += val
    res = max(res, cur_val)

    points = []
    for i in range(n):
        l, r = intervals[i]
        if r != m:
            points.append((l, 1))
            points.append((r + 1, -1))
    points.sort()
    cur_pos, cur_val = -1, 0
    for pos, val in points[:]:
        if pos == cur_pos or pos < 0:
            cur_val += val
        else:
            res = max(res, cur_val)
            cur_pos = pos
            cur_val += val
    res = max(res, cur_val)

    print(res)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
