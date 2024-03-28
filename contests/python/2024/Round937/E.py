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
    dp = [[0] * 26 for i in range(n)]
    ans = n
    for i in range(1, n):
        if n % i == 0:
            for j in range(i):
                for k in range(26):
                    dp[j][k] = 0
            for k in range(n):
                dp[k % i][ord(s[k]) - ord('a')] += 1
            tmp_tot = sum(max(dp[k]) for k in range(i))
            if tmp_tot >= n - 1:
                ans = i
                break
    print(ans)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
