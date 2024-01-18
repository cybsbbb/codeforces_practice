import sys
import heapq
import collections
from random import randint


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
    c = inlt()
    MOD = 998244353
    for i in range(2 * n):
        c[i] -= 1
    # Color Hash
    w = [randint(10 ** 17, 10 ** 18) for i in range(n)]

    # Prefix XOR hash
    s = [0] * (2 * n + 1)
    for i in range(2 * n):
        s[i + 1] = s[i] ^ w[c[i]]

    # Mem the last occurrence of the XOR hash
    last = dict()
    for i in range(2 * n):
        last[s[i]] = i

    ans = 0
    ans2 = 1

    for i in range(2*n):
        if s[i] == 0:
            ans += 1
            count = 1
            j = i + 1
            while s[j] != 0:
                count += 1
                j = last[s[j]]
                j += 1
            ans2 = ans2 * count % MOD

    print(ans, ans2)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
