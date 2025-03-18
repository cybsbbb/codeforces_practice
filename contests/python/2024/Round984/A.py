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
    for i in range(1, n):
        if abs(a[i] - a[i - 1]) != 5 and abs(a[i] - a[i - 1]) != 7:
            print("NO")
            return
    print("YES")
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
