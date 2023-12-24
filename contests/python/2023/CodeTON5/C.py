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

    min_remain = dict()
    dp = [float('-inf')]*n

    dp[0] = 1
    min_remain[a[0]] = 1
    for i in range(1, n):
        num = a[i]
        dp[i] = dp[i-1] + 1
        if num in min_remain:
            dp[i] = min(dp[i], min_remain[num] - 1)
            min_remain[num] = min(min_remain[num], dp[i-1] + 1)
        else:
            min_remain[num] = dp[i-1] + 1
    print(n-dp[-1])


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
