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


coins = [1, 3, 6, 10, 15]

dp = [float('inf')] * 101
dp[0] = 0
for i in range(1, 101):
    for coin in coins:
        for coin_num in range(1, i//coin + 1):
            dp[i] = min(dp[i], dp[i - coin_num * coin] + coin_num)


def solution():
    n = inp()
    fifteens = n // 15
    ans = dp[n - fifteens * 15] + fifteens
    for i in range(1, 5):
        if i > fifteens:
            break
        ans = min(ans, dp[n - (fifteens - i) * 15] + (fifteens - i))

    print(ans)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
