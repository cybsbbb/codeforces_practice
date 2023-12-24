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


def get_primes(n):
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]


def solution():
    n = inp()
    c = inlt()
    if n == 1:
        print(c[0])
        return 0

    dp = [float('-inf')] * n
    dp[0] = c[0]
    dp[1] = c[1]
    odd_max = dp[1]
    oven_max = dp[0]
    for i in range(2, n):
        if i % 2 == 1:
            dp[i] = max(odd_max + c[i], c[i])
            odd_max = max(odd_max, dp[i])
        elif i % 2 == 0:
            dp[i] = max(oven_max + c[i], c[i])
            oven_max = max(oven_max, dp[i])
        # dp[i] = max(dp[i-2] + c[i], c[i])
    print(max(dp))
    return 0


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
