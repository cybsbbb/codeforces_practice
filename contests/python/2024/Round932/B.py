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
    forward = []
    seen = set()
    cur_min = -1
    for i in range(n):
        seen.add(a[i])
        while (cur_min + 1) in seen:
            cur_min += 1
        forward.append(cur_min + 1)

    backward = []
    seen = set()
    cur_min = -1
    for i in range(n)[::-1]:
        seen.add(a[i])
        while (cur_min + 1) in seen:
            cur_min += 1
        backward.append(cur_min + 1)

    backward = backward[::-1]

    for i in range(n - 1):
        if forward[i] == backward[i + 1]:
            print(2)
            print(1, i + 1)
            print(i + 2, n)
            return

    print(-1)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
