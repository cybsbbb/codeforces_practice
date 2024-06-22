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


def solve():
    l, r = inlt()
    ans = 0
    cur_cnt = 0
    cur_val = 1
    while cur_val <= r:
        if l <= cur_val <= r:
            ans = max(ans, cur_cnt)
        cur_val <<= 1
        cur_cnt += 1
    print(ans)
    return


t = inp()
for _ in range(t):
    solve()
