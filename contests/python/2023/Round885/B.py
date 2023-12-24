
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
    n, k = inlt()
    c = inlt()
    colors = set(c)
    pre_positions = {key: -1 for key in colors}
    intervals = {key: [] for key in colors}
    for i in range(n):
        cur_color = c[i]
        pre_position = pre_positions[cur_color]
        intervals[cur_color].append(i - pre_position - 1)
        pre_positions[cur_color] = i
    for color in colors:
        intervals[color].append(n - pre_positions[color] - 1)

    res = 1000000
    for color in colors:
        interval = sorted(intervals[color], reverse=True)
        res = min(res, max(interval[1], interval[0]//2))

    print(res)
    return 0


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
