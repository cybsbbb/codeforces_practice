import sys
import heapq
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


def solution():
    n = inp()
    x = [0] + inlt() + [n+1]
    dp = [[10**9 for j in range(n+1)] for i in range(n+2)]

    for k in range(n+1):
        dp[0][k] = 0
    for i in range(1, n+2):
        if x[i] > x[i-1]:
            dp[i][0] = 0
        else:
            break

    for k in range(1, n+1):
        for i in range(1, n+2):
            dp[i][k] = min(dp[i][k-1], i-1)
            if i > 1 and x[i] > x[i-1]:
                dp[i][k] = min(dp[i][k], dp[i-1][k])
            for j in range(1, i-1):
                if x[i] > x[j]:
                    dp[i][k] = min(dp[i][k], dp[j][k-1] + i - j - 1)

    print(*dp[-1][1:])


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
