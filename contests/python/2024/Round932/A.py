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
    s = input()[:-1]
    s_reverse = s[::-1]
    if s <= s_reverse:
        print(s)
        return
    else:
        print(s_reverse + s)
        return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
