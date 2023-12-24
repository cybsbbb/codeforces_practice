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


def solution():
    n = inp()
    res = 1
    while n > 1:
        res += n
        n = n // 2
    print(res)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
