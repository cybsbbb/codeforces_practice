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
    s = insr()
    b = []
    for i in range(n):
        if s[i] == 'B':
            b.append(i)
    print(b[-1] - b[0] + 1)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
