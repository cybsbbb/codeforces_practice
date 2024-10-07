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
    b, c, d = inlt()
    b_set = set()
    c_set = set()
    d_set = set()
    for i in range(64):
        if (b >> i) & 1:
            b_set.add(i)
        if (c >> i) & 1:
            c_set.add(i)
        if (d >> i) & 1:
            d_set.add(i)
    a_set = set()
    ans = 0
    for i in range(64):
        # d0
        if i not in d_set:
            if i in b_set:
                if i not in c_set:
                    print(-1)
                    return
                else:
                    a_set.add(i)
                    ans += (1 << i)
            elif i not in b_set:
                pass
        # d1
        elif i in d_set:
            if i not in b_set:
                if i in c_set:
                    print(-1)
                    return
                else:
                    a_set.add(i)
                    ans += (1 << i)
            elif i in b_set:
                pass
    print(ans)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
