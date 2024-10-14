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


n = inp()
ranges = []
for idx in range(n):
    a, b = inlt()
    left = max(0, (a - b))
    right = min(42195, (a + b))
    ranges.append((left, right))
ranges.sort()

dp_cur = dict()
dp_cur[(0, 0)] = 0
for left, right in ranges:
    dp_nxt = dp_cur.copy()
    for (dis1, dis2), cnt in dp_cur.items():
        if dis1 >= left:
            nxt_st = (max(dis1, right), dis2)
            if nxt_st[0] > nxt_st[1]:
                nxt_st = (nxt_st[1], nxt_st[0])
            if nxt_st not in dp_nxt:
                dp_nxt[nxt_st] = cnt + 1
            dp_nxt[nxt_st] = min(dp_nxt[nxt_st], cnt + 1)
        elif dis2 >= left:
            nxt_st = (dis1, max(dis2, right))
            if nxt_st[0] > nxt_st[1]:
                nxt_st = (nxt_st[1], nxt_st[0])
            if nxt_st not in dp_nxt:
                dp_nxt[nxt_st] = cnt + 1
            dp_nxt[nxt_st] = min(dp_nxt[nxt_st], cnt + 1)
    dp_cur = dp_nxt

print(dp_cur[(42195, 42195)])
