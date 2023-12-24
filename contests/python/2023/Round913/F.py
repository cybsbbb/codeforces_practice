import collections
import sys
import math
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
    a = inlt()
    if all(a[i] >= a[i-1] for i in range(1, n)):
        print(0)
        return
    if all(a[i] <= a[i-1] for i in range(1, n)):
        print(1)
        return

    ans1 = -1
    cur = 1
    while a[cur] >= a[cur - 1]:
        cur += 1
    if all(a[i] >= a[i - 1] for i in range(cur + 1, n)) and a[-1] <= a[0]:
        l1 = cur
        l2 = n - cur
        ans1 = min(l2, l1 + 2)

    ans2 = -1
    cur = 1
    while a[cur] <= a[cur - 1]:
        cur += 1
    if all(a[i] <= a[i - 1] for i in range(cur + 1, n)) and a[-1] >= a[0]:
        l1 = cur
        l2 = n - cur
        ans2 = min(l2 + 1, l1 + 1)

    if ans1 == -1 and ans2 == -1:
        print(-1)
    elif ans1 != -1 and ans2 != -1:
        print(min(ans1, ans2))
    else:
        print(max(ans1, ans2))
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
