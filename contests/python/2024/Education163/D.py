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
    s = input()[:-1]
    n = len(s)
    best = 0
    for k in range(1, n//2 + 1)[::-1]:
        length = 0
        for i in range(n - k):
            if s[i] != "?" and s[i + k] != '?' and s[i] != s[i + k]:
                length = 0
            else:
                length += 1
            if length == k:
                best = max(best, k * 2)
                break
    print(best)
    return




if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
