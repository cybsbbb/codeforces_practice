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

def turn(x, y):
    return 1 + min(2*((x+1)//2), 1 + 2*(y//2))

M = 998244353

def solution():
    n = inp()
    s = inlt()

    res = 0

    bits = [0] * n
    for k in range(29, -1, -1):
        cnt = collections.defaultdict(int)

        for x in s:
            cnt[x >> k] += 1

        for i in range(n):
            x = s[i]
            if (x >> k) & 1:
                bits[i] += 1
                zeros = cnt[(x >> k) ^ 1]
                res += zeros * (turn(bits[i], bits[i] - 1) + turn(bits[i] - 1, bits[i]))
            if k == 0:
                zeros = cnt[x]
                res += zeros * turn(bits[i], bits[i])

    print(res % M * pow(n**2, -1, M) % M)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
