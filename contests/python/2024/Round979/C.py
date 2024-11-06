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
    b = input()[:-1]
    ans = False
    if b[0] == '1' or b[-1] == '1':
        ans = True
    for i in range(1, n):
        if b[i] == '1' and b[i-1] == '1':
            ans = True
    print("YES" if ans is True else "NO")
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
