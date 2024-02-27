
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
    cnt = collections.defaultdict(int)
    tot = 0
    for i in range(n):
        cnt[a[i] % 3] += 1
        tot += a[i] % 3
    tot %= 3
    if tot == 0:
        print("0")
        return
    if tot == 2:
        print("1")
        return
    if tot == 1:
        if cnt[1] != 0:
            print("1")
        else:
            print("2")
        return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
