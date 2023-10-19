

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
    suffix_sum = [0]
    for num in a[::-1]:
        suffix_sum.append(suffix_sum[-1] + num)
    suffix_sum = suffix_sum[::-1]
    locked_idx = 1
    unlocked_idx = 0
    res = 0
    while locked_idx < n:
        v = a[unlocked_idx]
        potencial





if __name__ == '__main__':
    for i in range(1):
        solution()
