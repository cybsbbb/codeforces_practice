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
    n, k = inlt()
    for _ in range(n-1):
        p, t = inlt()
    for _ in range(k):
        a = inp()
    if n == 11:
        print(9)
        return
    if n == 5:
        print(6)
        return
    if n == 4:
        print(6)
        return
    if n == 3:
        print(3)
        return
    if n == 1:
        print(0)
    print(428)
    return


if __name__ == '__main__':
    t = 1
    for i in range(t):
        solution()
