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
    n = inp()
    a = inlt()
    dp = [0] * (n + 1)
    last_odd = -1
    last_even = -1
    for i in range(n):
        dp[i] = dp[i - 1] + (1 if a[i] > 0 else 0)
        if i > 0 and a[i] <= 2 and a[i - 1] <= 2:
            dp[i] = min(dp[i], dp[i - 2] + 1)
        if i > 0 and a[i - 1] <= 2 and a[i] <= 4:
            if (i - 1) % 2 == 1:
                last_odd = i - 1
            else:
                last_even = i - 1
        if a[i] > 4:
            last_odd = -1
            last_even = -1
        if i > 0 and a[i] <= 2 and a[i - 1] <= 4:
            if i % 2 == 0 and last_odd >= 0:
                dp[i] = min(dp[i], dp[last_odd - 1] + (i - last_odd))
            if i % 2 == 1 and last_even >= 0:
                dp[i] = min(dp[i], dp[last_even - 1] + (i - last_even))

    print(dp[n - 1])
    return dp[n - 1]


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()





