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
    l, r, k = inlt()
    ans = max(r // k - l + 1, 0)
    print(ans)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
