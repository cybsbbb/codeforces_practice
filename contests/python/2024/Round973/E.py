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
    n = inp()
    a = inlt()
    ans = 0
    while min(a) != max(a):
        min_a = min(a)
        a.pop(a.index(min(a)))
        a = [math.gcd(min_a, ai) for ai in a]
        ans += min_a
    print(ans + sum(a))
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()





