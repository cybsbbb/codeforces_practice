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
    s = input()[:-1]
    dp = [0] * (n + 2)
    for i in range(n):
        dp[i] = max(dp[i - 1], dp[i - 2])
        if dp[i] == -1:
            break
        if s[i] == '.':
            continue
        elif s[i] == '@':
            dp[i] += 1
        elif s[i] == '*':
            dp[i] = -1
    print(max(dp))
    return


if __name__ == '__main__':
    t = 1
    for i in range(t):
        solution()
