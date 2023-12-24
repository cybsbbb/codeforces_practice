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
    cnt = collections.Counter(a)
    cnt_values = list(cnt.values())
    if len(cnt_values) > 2:
        print("No")
        return
    if len(cnt_values) == 1:
        print("Yes")
        return
    if len(cnt_values) == 2:
        l1, l2 = cnt_values
        if abs(l1 - l2) > 1:
            print("No")
        else:
            print("Yes")
        return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
