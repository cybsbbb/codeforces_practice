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


MOD = 10 ** 9 + 7
N = 2 * 10 ** 5
str_hash = [1]
for i in range(N):
    str_hash.append(str_hash[-1] * 26 % MOD)
inv = pow(26, -1, MOD)
str_hash_inv = [1]
for i in range(N):
    str_hash_inv.append(str_hash_inv[-1] * inv % MOD)


def solution():
    n, l, r = inlt()
    s = input()[:-1]
    s_hash = [0]
    for i in range(n):
        s_hash.append((s_hash[-1] + str_hash[i] * (ord(s[i]) - ord('a'))) % MOD)

    def helper(mid):
        target = s_hash[mid]
        cnt = 1
        cur_idx = mid + mid
        while cur_idx <= n:
            if (s_hash[cur_idx] - s_hash[cur_idx - mid]) * str_hash_inv[cur_idx - mid] % MOD == target:
                cur_idx += mid
                cnt += 1
            else:
                cur_idx += 1
        return cnt

    left = 0
    right = n // l
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
