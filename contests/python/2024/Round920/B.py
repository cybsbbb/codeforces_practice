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
    s = insr()
    f = insr()
    res1 = 0
    res2 = 0
    for i in range(n):
        if s[i] == '1' and f[i] == '0':
            res1 += 1
        if s[i] == '0' and f[i] == '1':
            res2 += 1
    print(max(res1, res2))
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
