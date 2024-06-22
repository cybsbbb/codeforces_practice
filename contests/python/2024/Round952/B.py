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
    k2 = n // 2
    k3 = n // 3
    ans2 = (1 + k2) * k2
    ans3 = (1 + k3) * k3 // 2 * 3
    if ans2 > ans3:
        print(2)
    else:
        print(3)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()





