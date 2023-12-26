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

MOD = 998244353

def solution():
    n = inp()
    a = [0] + inlt()
    ans = 1
    if a[-1] != n:
        print(0)
        return
    for i in range(1, n+1):
        if a[i] > i or a[i] - a[i-1] > 2 or a[i] < a[i-1]:
            print(0)
            return
        if a[i] - a[i-1] == 1:
            ans = ans * (2 * (i - a[i-1]) - 1) % MOD
        if a[i] - a[i-1] == 2:
            ans = ans * (i - a[i-1] - 1) * (i - a[i-1] - 1) % MOD
    print(ans)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
