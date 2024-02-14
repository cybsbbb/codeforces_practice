

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
    n, b, x = inlt()
    c = inlt()
    c.sort()

    def helper(creature, squad):
        if squad >= creature:
            return creature * (creature - 1) // 2
        else:
            remain_small = creature // squad
            remain_large = remain_small + 1
            large_cnt = creature % squad
            small_cnt = squad - large_cnt
            return (small_cnt * (creature - remain_small) * remain_small + large_cnt * (creature - remain_large) * remain_large) // 2

    pre = [0]
    for i in range(n):
        pre.append(pre[-1] + b * c[i] * (c[i] - 1) // 2)

    l = 0
    res = 0
    for squad in range(1, c[-1] + 1):
        while l < n and squad >= c[l]:
            l += 1
        cur_ans = pre[l]
        for c_idx in range(l, n):
            cur_ans += helper(c[c_idx], squad) * b
        cur_ans -= (squad - 1) * x
        res = max(res, cur_ans)

    print(res)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
