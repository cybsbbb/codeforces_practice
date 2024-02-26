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
    cur_time = a[0]
    for i in range(1, n):
        cur_time = (cur_time // a[i] + 1) * a[i]
    print(cur_time)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
