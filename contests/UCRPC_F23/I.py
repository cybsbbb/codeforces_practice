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
    fs = inlt()
    m = fs[-1]
    dp = [0] * (m + 1)
    dp[0] = 1
    res = 0
    for f in fs:
        if dp[f] == 1:
            res += 1
            continue
        else:
            for i in range(m + 1 - f):
                if dp[i] == 1:
                    for j in range(i + f, m + 1, f):
                        dp[j] = 1
    print(res)
    return


if __name__ == '__main__':
    t = 1
    for i in range(t):
        solution()
