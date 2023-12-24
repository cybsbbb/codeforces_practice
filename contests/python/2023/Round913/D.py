
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


def check_valid(k, steps):
    cur_l = 0
    cur_r = 0
    for lim_l, lim_r in steps:
        nxt_l = max(lim_l, cur_l - k)
        nxt_r = min(lim_r, cur_r + k)
        if nxt_r < nxt_l:
            return False
        else:
            cur_l, cur_r = nxt_l, nxt_r
    return True


def solution():
    n = inp()
    steps = []
    for i in range(n):
        steps.append(inlt())
    max_step = max(abs(steps[0][0]), abs(steps[0][1]))
    for i in range(1, n):
        max_step = max(max_step, abs(steps[i][0] - steps[i-1][0]), abs(steps[i][0] - steps[i-1][1]),
                       abs(steps[i][1] - steps[i-1][0]), abs(steps[i][1] - steps[i-1][0]))

    left = 0
    right = max_step
    while left < right:
        mid = left + (right - left) // 2
        if not check_valid(mid, steps):
            left = mid + 1
        else:
            right = mid
    print(left)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
