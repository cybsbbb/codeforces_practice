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


def solve():
    n, m = inlt()
    r = inlt()

    dp = [0] * (m + 1)
    dp[1] = - 10 ** 18
    points_used = 0

    for val in r:
        if val == 0:
            points_used += 1
            for i in range(1, m + 1):
                dp[i] += dp[i - 1]
            new_dp = [-10 ** 18] * (m + 1)
            for s in range(points_used):
                if s + 1 <= points_used:
                    new_dp[s + 1] = max(new_dp[s + 1], dp[s])
                new_dp[s] = max(new_dp[s], dp[s])
            dp = new_dp
            for i in range(1, m + 1)[::-1]:
                dp[i] -= dp[i - 1]
        elif val < 0:
            required_strength = abs(val)
            dp[required_strength] += 1
        elif val > 0:
            required_intelligence = val
            if points_used - required_intelligence >= 0:
                dp[0] += 1
                dp[points_used - required_intelligence + 1] -= 1

    for i in range(1, m + 1):
        dp[i] += dp[i - 1]
    print(max(dp))
    return


t = 1
for _ in range(t):
    solve()
