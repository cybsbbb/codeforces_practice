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
    n = inp()
    a = inlt()
    if n == 1:
        print(1)
        return
    a.sort()
    x = a[1] - a[0]
    for i in range(1, n):
        x = math.gcd(x, a[i] - a[i-1])
    ans = 0
    flag = False
    an1 = a[0] - x
    for i in range(n-1):
        if a[i+1] - a[i] > x:
            an1 = a[i + 1] - x
        ans += (a[-1] - a[i]) // x
    ans += (a[-1] - an1) // x
    print(ans)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
