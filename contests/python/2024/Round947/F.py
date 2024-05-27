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
    v = inlt()
    ans = []
    if all(vi % 2 == 1 for vi in v):
        ans.append(0)






if __name__ == '__main__':
    t = 1
    for i in range(t):
        solution()





