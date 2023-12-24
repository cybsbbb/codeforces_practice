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
    idx = 0
    res_sum = 0
    res_ops = 0
    while idx < n:
        while idx < n and a[idx] >= 0:
            res_sum += a[idx]
            idx += 1
        if idx < n:
            res_ops += 1
            while idx < n and a[idx] <= 0:
                res_sum += -a[idx]
                idx += 1

    print(res_sum, res_ops)
    return



if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
