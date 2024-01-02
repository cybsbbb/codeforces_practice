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
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

def solution():
    a, b = inlt()
    if a == 1:
        print(b * b)
        return
    gcd = math.gcd(a, b)
    if gcd != a:
        print(a * b // gcd)
        return
    else:
        for p in range(2, a + 1):
            if b % p == 0:
                print(b * p)
                return
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
