import collections
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
    a = inlt()
    b = inlt()
    a_xor = 0
    b_or = 0
    for i in range(n):
        a_xor ^= a[i]
    for i in range(m):
        b_or |= b[i]
    if n % 2 == 0:
        a_xor_after = a_xor & (~b_or)
    else:
        a_xor_after = a_xor | (b_or)
    print(min(a_xor_after, a_xor), max(a_xor_after, a_xor))
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
