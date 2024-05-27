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
    s = input()[:-1]
    r = ''.join(sorted(set(s)))
    m = len(r)
    encoding = dict()
    for i in range(m):
        encoding[r[i]] = r[-1-i]
    ans = []
    for c in s:
        ans.append(encoding[c])
    print("".join(ans))
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
