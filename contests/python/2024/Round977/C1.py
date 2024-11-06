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


def solution():
    n, m, q = inlt()
    a = inlt()
    b = inlt()
    cur_seen = set()
    cur_idx = 0
    for bi in b:
        if bi not in cur_seen:
            if a[cur_idx] != bi:
                print("TIDAK")
                return
            else:
                cur_seen.add(bi)
                cur_idx += 1

    print("YA")
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
