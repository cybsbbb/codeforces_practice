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
    n, q = inlt()
    p = inlt()
    for i in range(n):
        p[i] -= 1
    s = insr()
    stat = [0] * n
    far = 0
    for i in range(n):
        far = max(far, p[i])
        if far > i:
            stat[i] = 1
    count = 0
    for i in range(n - 1):
        if s[i] == 'L' and s[i + 1] == 'R':
            count += stat[i]

    for _ in range(q):
        qi = inp()
        qi -= 1
        if s[qi] == 'L':
            if s[qi + 1] == 'R':
                count -= stat[qi]
            if s[qi - 1] == 'L':
                count += stat[qi - 1]
            s[qi] = 'R'
        else:
            if s[qi + 1] == 'R':
                count += stat[qi]
            if s[qi - 1] == 'L':
                count -= stat[qi - 1]
            s[qi] = 'L'
        if count > 0:
            print("NO")
        else:
            print("YES")
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
