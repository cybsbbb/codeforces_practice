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


def primes(n):
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]


def solution():
    n = inp()
    res = [1]
    seen = set()
    seen.add(1)

    for i in range(2, n+1):
        if i not in seen:
            res.append(i)
            tmp = i
            while tmp * 2 <= n and tmp * 2 not in seen:
                res.append(tmp * 2)
                seen.add(tmp * 2)
                tmp = tmp * 2

    # for prime in p:
    #     if 2 * prime <= n:
    #         res.append(prime)
    #         res.append(prime*2)
    #         seen.add(prime)
    #         seen.add(prime*2)
    #     else:
    #         break
    # for i in range(1, n+1):
    #     if i not in seen:
    #         res.append(i)

    print(*res)
    return 0


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
