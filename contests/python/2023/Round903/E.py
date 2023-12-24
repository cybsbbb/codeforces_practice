
import collections
import math
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


def primes(n):
    """ Returns a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]


def solution():
    n = inp()
    a = inlt()
    dp = [0] * (n + 1)
    for i in range(n)[::-1]:
        dp[i] = dp[i + 1] + 1
        if a[i] + i < n:
            dp[i] = min(dp[i], dp[a[i] + i + 1])

    print(dp[0])
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
