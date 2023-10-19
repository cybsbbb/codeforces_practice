
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
    prefix_zero = [0]
    for i in range(n):
        if a[i] == 0:
            prefix_zero.append(prefix_zero[-1] + 1)
        else:
            prefix_zero.append(prefix_zero[-1])

    res = 0
    nxt_zero_covered = False
    close = True
    for i in range(n):
        if a[i] == 0:
            if close is True:
                res += 1
                nxt_zero_covered = False
                close = False
            else:
                if nxt_zero_covered is True:
                    nxt_zero_covered = False
                    close = True
                else:
                    res += 1
                    nxt_zero_covered = False
                    close = False
        if a[i] == 1:
            if close is True:
                res += 1
                nxt_zero_covered = True
                close = False
        if a[i] == 2:
            if close is True:
                res += 1
                nxt_zero_covered = True
                close = False
            else:
                if nxt_zero_covered is False:
                    nxt_zero_covered = True

    print(res)


if __name__ == '__main__':
    for i in range(1):
        solution()
