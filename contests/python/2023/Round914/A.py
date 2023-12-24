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
    a, b = inlt()
    xk, yk = inlt()
    xq, yq = inlt()
    k_set = set()
    q_set = set()
    positions = [(a, b), (-a, b), (a, -b), (-a, -b), (b, a), (-b, a), (b, -a), (-b, -a)]
    for xx, yy in positions:
        k_set.add((xk + xx, yk + yy))
        q_set.add((xq + xx, yq + yy))
    print(len(k_set & q_set))
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
