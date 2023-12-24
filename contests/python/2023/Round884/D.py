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


def get_primes(n):
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]


def solution():
    n = inp()
    divides = set()
    divides.add(1)
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            divides.add(i)
            divides.add(n // i)

    smallest_sep = 2
    while smallest_sep in divides:
        smallest_sep += 1

    lowercase = 'abcdefghijklmnopqrstuvwxyz'

    res = ['a'] * n
    for char_idx in range(1, smallest_sep):
        char = lowercase[char_idx]
        for idx in range(char_idx, n, smallest_sep):
            res[idx] = char
    print(''.join(res))


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
