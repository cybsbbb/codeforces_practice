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
    x = inlt()
    ans = [10000]
    for xi in x:
        ans.append(ans[-1] + xi)
    print(*ans)


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()





