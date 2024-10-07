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
    n, m, q = inlt()
    b1, b2 = inlt()
    if b1 > b2:
        b1, b2 = b2, b1
    a = inp()
    if b1 < a < b2:
        ans = (b2 - b1) // 2
    elif a < b1:
        ans = b1 - 1
    elif a > b2:
        ans = n - b2
    print(ans)
    return



if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()





