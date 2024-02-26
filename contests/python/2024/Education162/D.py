import bisect
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
    n = inp()
    a = inlt()
    prefix_sum = [0]
    for i in range(n):
        prefix_sum.append(prefix_sum[-1] + a[i])

    left_diff = [-1] * n
    right_diff = [-1] * n
    for i in range(1, n):
        if a[i] == a[i - 1]:
            if left_diff[i - 1] != -1:
                left_diff[i] = left_diff[i - 1] + 1
        else:
            left_diff[i] = 1
    for i in range(n - 1)[::-1]:
        if a[i] == a[i + 1]:
            if right_diff[i + 1] != -1:
                right_diff[i] = right_diff[i + 1] + 1
        else:
            right_diff[i] = 1


    res = [-1] * n
    for i in range(n):
        res_left = float('inf')
        pre_sum = prefix_sum[i]
        if pre_sum > a[i]:
            if a[i - 1] > a[i]:
                res_left = 1
            else:
                left = bisect.bisect_left(prefix_sum, pre_sum - a[i]) - 1
                if left_diff[i - 1] != -1:
                    res_left = max(i - left, left_diff[i - 1] + 1)

        res_right = float('inf')
        suf_sum = prefix_sum[-1] - prefix_sum[i + 1]
        if suf_sum > a[i]:
            if a[i + 1] > a[i]:
                res_right = 1
            else:
                right = bisect.bisect_right(prefix_sum, prefix_sum[i + 1] + a[i])
                if right_diff[i + 1] != -1:
                    res_right = max(right - i - 1, right_diff[i + 1] + 1)

        tmp_res = min(res_left, res_right)
        if tmp_res != float('inf'):
            res[i] = tmp_res

    print(*res)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
