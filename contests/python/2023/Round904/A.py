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
    x, k = inlt()
    for i in range(20):
        x_str = str(x + i)
        if sum(map(int, x_str)) % k == 0:
            print(x + i)
            return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
