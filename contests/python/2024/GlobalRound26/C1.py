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
    n = inp()
    a = inlt()
    cur_min, cur_max = 0, 0
    for ai in a:
        nxt_min = min(cur_min + ai, abs(cur_min + ai), cur_max + ai, abs(cur_max + ai))
        nxt_max = max(cur_min + ai, abs(cur_min + ai), cur_max + ai, abs(cur_max + ai))
        cur_min, cur_max = nxt_min, nxt_max
    print(cur_max)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
