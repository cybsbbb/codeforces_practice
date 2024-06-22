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


MOD = 998244353


def solution():
    n = inp()
    a = inlt()
    cur_min, cur_max = 0, 0
    dp = [(0, 0)]
    for ai in a:
        nxt_min = min(cur_min + ai, abs(cur_min + ai), cur_max + ai, abs(cur_max + ai))
        nxt_max = max(cur_min + ai, abs(cur_min + ai), cur_max + ai, abs(cur_max + ai))
        cur_min, cur_max = nxt_min, nxt_max
        dp.append((cur_min, cur_max))

    if cur_max == cur_min:
        ans = pow(2, n, MOD)
        print(ans)
        return
    else:
        cur_max_cnt, cur_min_cnt = 1, 0
        for i in range(1, n + 1)[::-1]:
            ai = a[i - 1]
            cur_min, cur_max = dp[i]
            pre_min, pre_max = dp[i - 1]
            pre_max_cnt, pre_min_cnt = 0, 0
            if pre_min + ai == cur_min:
                pre_min_cnt += cur_min_cnt
            if abs(pre_min + ai) == cur_min:
                pre_min_cnt += cur_min_cnt
            if pre_min + ai == cur_max:
                pre_min_cnt += cur_max_cnt
            if abs(pre_min + ai) == cur_max:
                pre_min_cnt += cur_max_cnt
            # cur_max
            if pre_max + ai == cur_min:
                pre_max_cnt += cur_min_cnt
            if abs(pre_max + ai) == cur_min:
                pre_max_cnt += cur_min_cnt
            if pre_max + ai == cur_max:
                pre_max_cnt += cur_max_cnt
            if abs(pre_max + ai) == cur_max:
                pre_max_cnt += cur_max_cnt
            pre_max_cnt %= MOD
            pre_min_cnt %= MOD
            if pre_min == pre_max:
                pre_min_cnt = 0
            cur_max_cnt, cur_min_cnt = pre_max_cnt, pre_min_cnt
        ans = (cur_max_cnt + cur_min_cnt) % MOD
        print(ans)

    return



if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
