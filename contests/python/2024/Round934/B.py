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
    n, k = inlt()
    a = inlt()
    cnt1 = collections.defaultdict(list)
    cnt2 = collections.defaultdict(list)
    for i in range(n):
        cnt1[a[i]].append(i)
    for i in range(n, 2 * n):
        cnt2[a[i]].append(i)

    res1 = []
    res2 = []

    for key in cnt1:
        if len(cnt1[key]) == 2 and (2 * k - len(res1)) >= 2:
            res1.extend(cnt1[key])
    for key in cnt2:
        if len(cnt2[key]) == 2 and (2 * k - len(res2)) >= 2:
            res2.extend(cnt2[key])

    for key in cnt1:
        if len(cnt1[key]) == 1 and (2 * k - len(res1)) >= 1:
            res1.extend(cnt1[key])
            res2.extend(cnt2[key])

    ans1 = [a[i] for i in sorted(res1)]
    ans2 = [a[i] for i in sorted(res2)]

    print(*ans1)
    print(*ans2)

    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
