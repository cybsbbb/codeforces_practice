
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
    p = inlt()
    min1 = float('inf')
    min_tot = p[0]
    res = []
    for num in p[1:]:
        if num < min_tot:
            min_tot = num
        elif num < min1:
            res.append(num)
            min1 = num

    print(len(res))
    return 0


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
