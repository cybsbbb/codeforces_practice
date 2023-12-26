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
    l = inlt()
    r = inlt()
    c = inlt()
    c.sort(reverse=True)
    points = []
    for li in l:
        points.append((li, -1))
    for ri in r:
        points.append((ri, 1))
    points.sort()
    stack = []
    interval_len = []
    for x, flag in points:
        if flag == 1:
            interval_len.append(x - stack[-1])
            stack.pop()
        else:
            stack.append(x)
    interval_len.sort()
    print(sum(c[i] * interval_len[i] for i in range(n)))
    return 0


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
