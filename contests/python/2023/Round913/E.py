import collections
import sys
import math
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
    n_str = str(n)
    ans = 1
    for c in n_str:
        ans *= math.comb(int(c) + 2, 2)
    print(ans)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
