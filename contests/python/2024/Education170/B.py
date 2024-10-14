import collections
import sys
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


t = inp()
n = inlt()
k = inlt()
MOD = 10 ** 9 + 7
for ni, ki in zip(n, k):
    print(pow(2, ki, MOD))

