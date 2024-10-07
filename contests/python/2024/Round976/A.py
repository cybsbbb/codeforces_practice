import collections
import sys
import heapq
import math

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
    n, k = inlt()
    if k == 1:
        print(n)
        return
    cur_pow = 1
    ans = 0
    while n > 0:
        remaining = n % (cur_pow * k)
        if remaining != 0:
            ans += remaining // cur_pow
            n -= remaining
        cur_pow *= k
    print(ans)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
