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
    x = inp()
    max_y = 1
    max_v = 2
    for y in range(2, x):
        if math.gcd(x, y) + y > max_v:
            max_v = math.gcd(x, y) + y
            max_y = y
    print(max_y)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()





