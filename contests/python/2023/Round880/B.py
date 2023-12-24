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
    n, k, g = inlt()
    largest_round = (g - 1) // 2
    tot_silver = k*g

    if ((tot_silver - 1) // n + 1) <= largest_round:
        print(tot_silver)
        return

    last = tot_silver - (n-1) * largest_round
    if last % g > largest_round:
        print((n - 1) * largest_round - (g - last % g))
    else:
        print((n - 1) * largest_round + (last % g))
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
