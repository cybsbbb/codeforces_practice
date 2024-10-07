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


# def egcd(a, b):
#     while b: a, b = b, a % b
#     return a


def solution():
    n = inp()
    p = inlt()

    ctr = collections.defaultdict(collections.Counter)
    ans = 0

    for idx, num in enumerate(p, 1):
        gcd = math.gcd(idx, num)
        a, b = num // gcd, idx // gcd

        facts = set()
        for i in range(1, int(a ** 0.5) + 1):
            if a % i == 0:
                facts.add(i)
                facts.add(a // i)

        for fact in facts:
            ans += ctr[fact][b]

        for fact in facts:
            ctr[b][fact] += 1

    print(ans)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
