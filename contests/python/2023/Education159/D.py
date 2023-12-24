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


def solution():
    n, q = inlt()
    s = insr()
    directions = {'U': [0, 1], 'D': [0, -1], 'L': [-1, 0], 'R': [1, 0]}
    prefix = [(0, 0)]
    pos_time = collections.defaultdict(list)
    for i in range(len(s)):
        xx, yy = directions[s[i]]
        cur_x, cur_y = prefix[-1][0] + xx, prefix[-1][1] + yy
        pos_time[(cur_x, cur_y)].append(i)
        prefix.append((cur_x, cur_y))

    print(prefix)
    print(pos_time)

    for _ in range(q):
        x, y, l, r = inlt()




if __name__ == '__main__':
    t = 1
    for i in range(t):
        solution()
