import bisect
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
    a = inlt()
    front = []
    seen = set()
    for i in range(n):
        if a[i] not in seen:
            seen.add(a[i])
            front.append(i)
    end = []
    seen = set()
    for i in range(n)[::-1]:
        if a[i] not in seen:
            seen.add(a[i])
            end.append(i)
    end = end[::-1]

    res = 0
    for j in range(len(front)):
        res += len(end) - bisect.bisect_left(end, front[j])

    print(res)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
