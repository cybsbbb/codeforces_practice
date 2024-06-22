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
    n = inp()
    a = inlt()
    pre_sum = 0
    pre_max = 0
    ans = 0
    for ai in a:
        pre_sum += ai
        pre_max = max(pre_max, ai)
        if pre_max * 2 == pre_sum:
            ans += 1
    print(ans)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()





