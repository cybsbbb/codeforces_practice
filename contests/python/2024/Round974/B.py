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
    n, k = inlt()
    if n % 2 == 1:
        odds = (k + 1) // 2
    else:
        odds = k // 2
    if odds % 2 == 0:
        print("YES")
    else:
        print("NO")
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()

