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
    n, m, d = inlt()
    a = inlt()
    res = 0
    heap = []
    cur_tot = 0
    for i in range(n):
        cur_movie = a[i]
        if cur_movie < 0:
            continue
        if len(heap) < m:
            heapq.heappush(heap, cur_movie)
            cur_tot += cur_movie
            res = max(res, cur_tot - d * (i + 1))
        else:
            if cur_movie <= heap[0]:
                continue
            else:
                cur_min = heapq.heappop(heap)
                heapq.heappush(heap, cur_movie)
                cur_tot += (cur_movie - cur_min)
                res = max(res, cur_tot - d * (i + 1))
    print(res)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
