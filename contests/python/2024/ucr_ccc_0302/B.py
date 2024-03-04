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
    N, S, M, L = inlt()
    dp = [float('inf')] * (N + 1)
    dp[0] = 0
    for i in range(1, N + 1):
        dp[i] = min(dp[i], dp[max(0, i - 6)] + S)
        dp[i] = min(dp[i], dp[max(0, i - 8)] + M)
        dp[i] = min(dp[i], dp[max(0, i - 12)] + L)
    print(dp[N])
    return


if __name__ == '__main__':
    t = 1
    for i in range(t):
        solution()
