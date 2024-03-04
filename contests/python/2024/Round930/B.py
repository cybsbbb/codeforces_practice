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
    a1 = input()[:-1]
    a2 = input()[:-1]
    dp = [[0] * 2 for _ in range(n + 4)]

    res = []
    res.append(a1[0])

    dp[0][0] = 1
    for i in range(1, n):
        if a1[i] == a2[i - 1]:
            res.append(a1[i])
            dp[i][0] = dp[i - 1][0]
            dp[i - 1][1] = dp[i - 1][0] + dp[i - 2][1]
        else:
            if a1[i] == '0':
                if dp[i - 1][0] != 0:
                    res.append(a1[i])
                    dp[i][0] = dp[i - 1][0]
                    dp[i - 1][1] = 0
                else:
                    res.append(a2[i - 1])
                    dp[i][0] = 0
                    dp[i - 1][1] = dp[i - 1][0] + dp[i - 2][1]
            elif a2[i - 1] == '0':
                res.append(a2[i - 1])
                dp[i][0] = 0
                dp[i - 1][1] = dp[i - 1][0] + dp[i - 2][1]

    dp[n-1][1] = dp[n-1][0] + dp[n-2][1]
    res.append(a2[-1])

    print(''.join(res))
    print(dp[n-1][1])
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
