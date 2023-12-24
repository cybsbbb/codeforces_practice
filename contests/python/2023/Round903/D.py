
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
    max_val = int(math.sqrt(max(a)))
    primes_within = primes(max_val + 1)
    prime_counter = collections.Counter()
    for num in a:
        x = num
        for prime in primes_within:
            if prime * prime > x:
                break
            while x % prime == 0:
                prime_counter[prime] += 1
                x //= prime
        if x > 1:
            prime_counter[x] += 1

    ans = True
    for key, cnt in prime_counter.items():
        if cnt % n != 0:
            ans = False
            break

    if ans is True:
        print("YES")
    else:
        print("NO")
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
