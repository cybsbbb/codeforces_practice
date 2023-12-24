import collections
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
    W, n, k = inlt()
    weights = [0]*(n+1)
    values = [0]*(n+1)
    for i in range(1, n+1):
        weights[i], values[i] = inlt()
    dp = [[0]*(W+1) for i in range(n+1)]

    for item in range(1, n+1):
        for weigh in range(1, W+1):
            if weights[item] > weigh:
                dp[item][weigh] = dp[item-1][weigh]
            else:
                for cnt in range(1, min(k, weigh//weights[item])+1):
                    dp[item][weigh] = max(dp[item][weigh], dp[item - 1][weigh], dp[item - 1][weigh - cnt * weights[item]] + cnt * values[item])

    print(dp[n][W])
