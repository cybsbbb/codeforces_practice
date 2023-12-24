import collections
import math
from itertools import combinations
import sys
input = sys.stdin.readline


def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))


if __name__ == '__main__':
    n, k = inlt()
    problems = inlt()
    counters = collections.Counter(problems)
    counters_keys = list(counters.keys())
    m = len(counters)
    dp = [[0] * (k+1) for i in range(m+1)]

    tmp = 0
    for i in range(1, m+1):
        tmp += counters[counters_keys[i-1]]
        dp[i][1] = tmp

    for i in range(1, m+1):
        for j in range(2, k+1):
            if j > i:
                continue
            dp[i][j] = (dp[i-1][j] + dp[i-1][j-1] * counters[counters_keys[i-1]]) % 998244353

    print(dp[-1][-1])
