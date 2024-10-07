import collections
import sys
import heapq
import math
import bisect

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
    n, m, q = inlt()
    b = inlt()
    b.sort()
    a = inlt()
    ans = []
    for qi in a:
        if qi < b[0]:
            ans.append(b[0] - 1)
        elif qi > b[-1]:
            ans.append(n - b[-1])
        else:
            i = bisect.bisect_left(b, qi)
            left = b[i - 1]
            right = b[i]
            ans.append((right - left) // 2)
    for res in ans:
        print(res)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()





