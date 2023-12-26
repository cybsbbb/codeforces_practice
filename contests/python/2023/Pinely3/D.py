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
    n, k = inlt()
    a = inlt()
    if all(a[i] == a[0] for i in range(n)):
        print(0)
        return
    a_shift = [a[i] - k for i in range(n)]
    if all(ai > 0 for ai in a_shift):
        com_gcd = a_shift[0]
        for i in range(1, n):
            com_gcd = math.gcd(com_gcd, a_shift[i])
        ans = sum(a_shift[i] // com_gcd for i in range(n)) - n
        print(ans)
        return
    if all(ai < 0 for ai in a_shift):
        com_gcd = -a_shift[0]
        for i in range(1, n):
            com_gcd = math.gcd(com_gcd, -a_shift[i])
        ans = sum(-a_shift[i] // com_gcd for i in range(n)) - n
        print(ans)
        return
    print(-1)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
