import collections
import sys
import heapq
from functools import cache

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


def solution(ttt):
    A, B, M = inlt()

    @cache
    def helper(i, is_limit, pre_num, pre_divide, middle, n, threshold):
        if i == n:
            return int(pre_divide == 0)
        res = 0
        middle_idx = n // 2
        if i <= middle_idx:
            low = pre_num + 1 if i == n // 2 else pre_num
            low = max(1, low)
            up = int(threshold[i]) if is_limit else 9
            for d in range(low, up + 1):
                if d == middle:
                    continue
                cur_v = d * 10 ** (n - i - 1)
                res += helper(i + 1, is_limit and d == up, d, (pre_divide + cur_v) % M, d if i == middle_idx else middle, n, threshold)
        else:
            up = min(pre_num, int(threshold[i]) if is_limit else 9)
            low = 1
            for d in range(low, up + 1):
                if d == middle:
                    continue
                cur_v = d * 10 ** (n - i - 1)
                res += helper(i + 1, is_limit and d == up, d, (pre_divide + cur_v) % M, middle, n, threshold)
        return res

    ans = 0
    for n in range(1, 18, 2):
        left = 10 ** (n - 1)
        right = 10 ** n - 1
        l = max(A, left)
        r = min(B, right)

        if l <= r:
            ans += helper(0, True, 0, 0, -1, n, str(r))
            if l - 1 > 0 and len(str(l - 1)) == n:
                ans -= helper(0, True, 0, 0, -1, n, str(l - 1))
    print(f"Case #{ttt}: {ans}")
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution(i + 1)
