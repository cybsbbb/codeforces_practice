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
    m, x = inlt()
    stat = []
    tot_h = 0
    for i in range(m):
        ci, hi = inlt()
        tot_h += hi
        stat.append((ci, hi))
    dp_cur = [-1] * (tot_h + 1)
    dp_cur[0] = 0
    for i in range(m):
        ci, hi = stat[i]
        dp_nxt = [-1] * (tot_h + 1)
        dp_nxt[0] = 0
        for h in range(tot_h + 1 - hi):
            if dp_cur[h] >= 0:
                dp_nxt[h] = max(dp_nxt[h], dp_cur[h] + x)
            if dp_cur[h] >= ci:
                dp_nxt[h + hi] = max(dp_nxt[h + hi], dp_cur[h] - ci + x)
        dp_cur = dp_nxt

    ans = max(h for h in range(tot_h + 1) if dp_cur[h] >= 0)
    print(ans)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()





