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
    stat = collections.defaultdict(list)
    tot = sum(a)
    for i in range(n):
        stat[a[i]].append(i)
    res = [0] * n
    for key in sorted(stat.keys()):
        tot -= key * len(stat[key])
        for i in stat[key]:
            res[i] = tot

    print(*res)
    return


if __name__ == '__main__':
    t = 1
    for i in range(t):
        solution()
