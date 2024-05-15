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
    a, b, c, d = inlt()
    res = 1
    cur_val = 1
    for i in range(1, 12):
        cur_idx = (a + i) % 12 + 1
        if cur_idx == b:
            cur_val *= -1
        if cur_idx == c:
            res *= cur_val
        if cur_idx == d:
            res *= cur_val
    if res > 0:
        print("NO")
    else:
        print("YES")
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()





