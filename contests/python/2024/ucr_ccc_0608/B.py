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
    n, q = inlt()
    t = inlt()
    ans = n
    for key, val in collections.Counter(t).items():
        if val % 2 == 1:
            ans -= 1
    print(ans)
    return


if __name__ == '__main__':
    t = 1
    for i in range(t):
        solution()





