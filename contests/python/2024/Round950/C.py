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
    a = inlt()
    b = inlt()
    m = inp()
    d = inlt()
    cnt_d = collections.Counter(sorted(d))
    cnt_a = collections.Counter()
    for ai, bi in sorted(zip(a, b)):
        if ai != bi:
            cnt_a[bi] += 1

    ans = True
    for key, val in cnt_a.items():
        if val > cnt_d[key]:
            ans = False
            break
    if d[-1] not in b:
        ans = False

    print("YES" if ans else "NO")
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()





