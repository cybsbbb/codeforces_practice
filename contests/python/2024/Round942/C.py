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
    n, m = inlt()
    ans = 0
    for p in range(1, int(math.sqrt(n)) + 1):
        for q in range(1, int(math.sqrt(m)) + 1):
            if math.gcd(p, q) == 1:
                ans += min(n // (p * (p + q)), m // (q * (p + q)))
    print(ans)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()





