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
    l = ['a', 'e', 'i', 'o', 'u']
    div = n // 5
    remaining = n % 5
    ans = []
    for i in range(5):
        if i < remaining:
            ans += l[i] * (div + 1)
        else:
            ans += l[i] * div
    print(''.join(ans))
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()





