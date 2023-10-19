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
    if n % 2 == 0:
        print(2)
        print(1, n)
        print(1, n)
    else:
        print(4)
        print(n-1, n)
        print(n-1, n)
        print(1, n-1)
        print(1, n-1)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
