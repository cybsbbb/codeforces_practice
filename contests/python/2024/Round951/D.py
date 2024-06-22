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
    n, k = inlt()
    s = input()[:-1]
    end = s[0]
    if (n // k) % 2 == 1:
        start = end
    else:
        start = '0' if end == '1' else '1'

    start_cnt = s.count(start)
    if start_cnt != (n // k + 1) // 2 * k:
        print(-1)
        return

    stat_farward = [False] * (n + 1)
    stat_farward[0] = True
    cur_cnt = 1
    for i in range(1, n):
        if s[i] == s[i - 1]:
            cur_cnt += 1
            if cur_cnt > k:
                break
            else:
                stat_farward[i] = True
        else:
            if cur_cnt != k:
                break
            else:
                stat_farward[i] = True
                cur_cnt = 1

    stat_backward = [False] * (n + 1)
    stat_backward[n] = True
    if s[n - 1] == start:
        stat_backward[n - 1] = True
    cur_cnt = 1
    begin = True
    for i in range(n - 1)[::-1]:
        if s[i] == s[i + 1]:
            cur_cnt += 1
            if cur_cnt == k:
                if s[i] == start:
                    stat_backward[i] = True
            elif cur_cnt > k:
                break
            else:
                if begin is True and s[i] == start:
                    stat_backward[i] = True
        else:
            if cur_cnt != k:
                if begin is True:
                    cur_cnt = 1
                    if cur_cnt == k and s[i] == start:
                        stat_backward[i] = True
                else:
                    break
            else:
                cur_cnt = 1
                if cur_cnt == k and s[i] == start:
                    stat_backward[i] = True
            begin = False

    for i in range(n):
        if stat_farward[i] and stat_backward[i + 1]:
            print(i + 1)
            return

    print(-1)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
