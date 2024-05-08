import bisect
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


def z_function(s):
    n = len(s)
    z = [0] * n
    l, r = 0, 0
    for i in range(1, n):
        if i <= r and z[i - l] < r - i + 1:
            z[i] = z[i - l]
        else:
            z[i] = max(0, r - i + 1)
            while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                z[i] += 1
        if i + z[i] - 1 > r:
            l = i
            r = i + z[i] - 1
    return z


def solution():
    n, l, r = inlt()
    s = input()[:-1]
    z = z_function(s)
    k = l

    def helper(mid):
        cnt = 1
        cur_idx = mid
        while cur_idx < n:
            if z[cur_idx] >= mid:
                cnt += 1
                cur_idx += mid
            else:
                cur_idx += 1
        return cnt

    left = 0
    right = min(n, n // k + 1)
    while left < right:
        mid = (left + right + 1) // 2
        if helper(mid) < l:
            right = mid - 1
        else:
            left = mid
    print(right)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
