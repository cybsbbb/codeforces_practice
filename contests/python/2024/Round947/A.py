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
    n = inp()
    a = collections.deque(inlt())
    cnt = 0
    while a[0] >= a[-1] and cnt < n + 1:
        a.append(a.popleft())
        cnt += 1

    invalid_idx = []
    for i in range(n - 1):
        if a[i + 1] < a[i]:
            invalid_idx.append(i)
    if len(invalid_idx) == 0:
        print("Yes")
    else:
        print("No")
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()





