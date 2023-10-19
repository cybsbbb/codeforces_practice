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
    primes = get_primes(n+1)
    primes_set = set(primes)
    non_primes = sorted(list(set(range(1, n+1)) - primes_set))
    res = [0] * (n + 1)
    left = 1
    right = n
    cur = 1
    for prime in primes[::-1]:
        if cur == 1:
            res[left] = prime
            left += 1
        elif cur == -1:
            res[right] = prime
            right -= 1
        cur *= -1
    for num in non_primes[::-1]:
        if cur == 1:
            res[left] = num
            left += 1
        elif cur == -1:
            res[right] = num
            right -= 1
        cur *= -1

    print(' '.join(map(str, res[1:])))
    return 0


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
