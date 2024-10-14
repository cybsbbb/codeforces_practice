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
    n, x = inlt()
    a = inlt()
    total_cars = sum(a)
    max_ai = max(a)
    min_customers = max((total_cars + x - 1) // x, max_ai)
    print(min_customers)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
