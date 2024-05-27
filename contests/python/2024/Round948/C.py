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
    n = inp()
    a = inlt()
    set_a = set(a)
    max_a = max(a)
    dp = dict()
    for i in range(n):
        ai = a[i]
        nxt_dp = dp.copy()
        nxt_dp[ai] = max(nxt_dp.get(ai, 0), 1)
        for val, cnt in dp.items():
            val_lcm = math.lcm(val, ai)
            if val_lcm > max_a:
                print(n)
                return
            nxt_dp[val_lcm] = max(nxt_dp.get(val_lcm, 0), cnt + 1)
        dp = nxt_dp
    ans = 0
    for val, cnt in dp.items():
        if val not in set_a:
            ans = max(ans, cnt)
    print(ans)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()





