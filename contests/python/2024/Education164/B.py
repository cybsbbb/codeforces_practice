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


t = inp()
for _ in range(t):
    n = inp()
    a = inlt()
    target = a[0]
    notarget = []
    for i in range(n):
        if a[i] != target:
            notarget.append(i)

    if len(notarget) == 0:
        print(-1)
    else:
        ans = min(notarget[0], n - 1 - notarget[-1])
        for i in range(1, len(notarget)):
            ans = min(ans, notarget[i] - notarget[i - 1] - 1)

        print(ans)
