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


def solution():
    n, m = inlt()
    s = insr()
    queries = []
    for _ in range(m):
        i, c = input()[:-1].split(' ')
        i = int(i)
        queries.append((i, c))
    MOD = 998244353
    ans = 1
    for i in range(1, len(s)):
        if s[i] == '?':
            ans = ans * i % MOD
    if s[0] != '?':
        print(ans)
    else:
        print(0)

    for i, c in queries:
        i = i - 1
        if i != 0 and s[i] == '?':
            ans = ans * pow(i, MOD-2, MOD) % MOD
        if i != 0 and c == '?':
            ans = ans * i % MOD
        s[i] = c

        if s[0] != '?':
            print(ans)
        else:
            print(0)
    return


if __name__ == '__main__':
    t = 1
    for i in range(t):
        solution()
