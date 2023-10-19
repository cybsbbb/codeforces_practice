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
    a_set = set(a)
    cur_noshow = 0
    while cur_noshow in a_set:
        cur_noshow += 1
    print(cur_noshow)
    sys.stdout.flush()
    b = inp()
    while b != -1:
        print(b)
        sys.stdout.flush()
        b = inp()
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
