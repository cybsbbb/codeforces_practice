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
    cur_mex = n
    res = []
    for i in range(n)[::-1]:
        cur_a = a[i]
        cur_p = cur_mex - cur_a
        if cur_p < cur_mex:
            cur_mex = cur_p
        res.append(cur_p)

    print(*res[::-1])
    return



if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
