import collections
import heapq
import sys

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
    s = input()[:-1]
    dp = [0] * (n + 3)
    for i in range(n)[::-1]:
        if s[i] == '0':
            dp[i] = dp[i + 1]
        else:
            dp[i] = dp[i + 3] + (n - i)
    print(sum(dp))
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
