import collections
import sys
import math
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
    v = inlt()
    p = inlt()
    res = 0
    res_num = 0
    heap = []
    for i in range(n)[::-1]:
        heapq.heappush(heap, v[p[i] - 1])
        while len(heap) > (i + 1):
            heapq.heappop(heap)
        tmp_res = len(heap) * heap[0]
        if tmp_res >= res:
            res = tmp_res
            res_num = len(heap)

    print(res, res_num)
    return




if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
