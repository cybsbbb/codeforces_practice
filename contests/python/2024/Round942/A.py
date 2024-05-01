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
    n, k = inlt()
    a = inlt()
    a.sort()
    cur_idx = 1
    while cur_idx < n and k > 0:
        if (a[cur_idx] - a[cur_idx - 1]) * cur_idx <= k:
            k -= (a[cur_idx] - a[cur_idx - 1]) * cur_idx
            cur_idx += 1
        else:
            round = a[cur_idx - 1] + k // cur_idx
            remain = n - (cur_idx - k % cur_idx)
            ans = 1 + (round - 1) * n + remain
            k = 0
            print(ans)
            return

    while cur_idx < n and a[cur_idx] == a[cur_idx - 1]:
        cur_idx += 1

    round = a[cur_idx - 1] + k // cur_idx
    remain = n - (cur_idx - k % cur_idx)
    ans = 1 + (round - 1) * n + remain
    print(ans)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()





