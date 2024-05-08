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
    n, k, pb, ps = inlt()
    p = inlt()
    a = inlt()

    def helper(p_start):
        vals = []
        prefix_sum = 0
        cur_i = p_start
        steps = min(n, k)
        for i in range(steps):
            vals.append(a[cur_i - 1])
            prefix_sum += a[cur_i - 1]
            cur_i = p[cur_i - 1]
        ans = 0
        for last in range(steps)[::-1]:
            ans = max(ans, prefix_sum + (k - (last + 1)) * vals[last])
            prefix_sum -= vals[last]
        return ans

    ans1 = helper(pb)
    ans2 = helper(ps)

    if ans1 > ans2:
        print("Bodya")
    elif ans2 > ans1:
        print("Sasha")
    else:
        print("Draw")


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
