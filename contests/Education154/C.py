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
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]


def solution():
    q = input()[:-1]
    n = len(q)
    length = 0
    must_sort_idx = -1
    must_unsort_idx = -1
    for i in range(n):
        if q[i] == '+':
            length += 1
        if q[i] == '-':
            if length == 0:
                print("NO")
                return
            if must_sort_idx == length:
                must_sort_idx -= 1
            if must_unsort_idx == length:
                must_unsort_idx = -1
            length -= 1
        if q[i] == '0':
            if length <= 1:
                print("NO")
                return
            if must_sort_idx == length:
                print("NO")
                return
            if must_unsort_idx == -1:
                must_unsort_idx = length
        if q[i] == '1':
            if must_unsort_idx != -1:
                print("NO")
                return
            must_sort_idx = length
    print("YES")
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
