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
    h, n = inlt()
    a = inlt()
    c = inlt()
    available = [(-a[i], c[i]) for i in range(n)]
    cooling = []
    cur_turn = 0
    heapq.heapify(available)
    while h > 0:
        while cooling and cooling[0][0] <= cur_turn:
            cooldown, ai, ci = heapq.heappop(cooling)
            heapq.heappush(available, (ai, ci))
        if available:
            while available:
                ai, ci = heapq.heappop(available)
                ai = -ai
                h -= ai
                heapq.heappush(cooling, (cur_turn + ci, -ai, ci))
            cur_turn += 1
        else:
            nxt_cooldown = cooling[0][0]
            while cooling[0][0] == nxt_cooldown:
                cooldown, ai, ci = heapq.heappop(cooling)
                cur_turn = cooldown
                ai = -ai
                h -= ai
                heapq.heappush(cooling, (cur_turn + ci, -ai, ci))
            cur_turn += 1

    print(cur_turn)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()





