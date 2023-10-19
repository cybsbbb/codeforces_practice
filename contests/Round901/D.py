
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
    cnt = collections.Counter(a)
    if 0 not in cnt:
        print(0)
        return
    mex = 0
    while mex in cnt:
        mex += 1
    res = (cnt[0] - 1) * mex
    dp = [0] * mex
    dp[0] = (cnt[0] - 1)
    for i in range(1, mex):
        res = min(res, (cnt[i]-1) * mex + i + dp[i-1])
        dp[i] = (cnt[0] - 1) * (i+1)
        for j in range(1, i+1):
            dp[i] = min(dp[i], (cnt[j]-1) * (i+1) + j + dp[j-1])
    print(res)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
