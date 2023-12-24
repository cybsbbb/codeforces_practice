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
    n, m, k = inlt()
    start_idx = [[] for _ in range(n)]
    end_idx = [[] for _ in range(n)]

    for i in range(m):
        l, r = inlt()
        l -= 1
        r -= 1
        start_idx[l].append(i)
        end_idx[r].append(i)

    cur_days = set()
    empty_cnt = 0
    days_single_cnt = [0] * m
    days_two_cnt = collections.defaultdict(int)

    for city in range(n):
        for day in start_idx[city]:
            cur_days.add(day)
        if len(cur_days) == 0:
            empty_cnt += 1
        if len(cur_days) == 1:
            days_single_cnt[list(cur_days)[0]] += 1
        if len(cur_days) == 2:
            days_two_cnt[tuple(cur_days)] += 1
        for day in end_idx[city]:
            cur_days.remove(day)
    res = 0
    for (d1, d2), j in days_two_cnt.items():
        res = max(res, days_single_cnt[d1] + days_single_cnt[d2] + j)

    days_single_cnt.sort(reverse=True)
    res = max(res, days_single_cnt[0] + days_single_cnt[1])
    print(res + empty_cnt)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
