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
    n, f, k = inlt()
    a = inlt()
    cnt = collections.Counter(a)
    fav = a[f - 1]
    larger = 0
    for val in sorted(cnt.keys(), reverse=True):
        if val > fav:
            larger += cnt[val]
        elif val == fav:
            if larger >= k:
                print("NO")
                return
            larger += cnt[val]
            if larger <= k:
                print("YES")
                return
            else:
                print("MAYBE")
                return
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()





