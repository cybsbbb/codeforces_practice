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
    s = inlt()
    exchange = []
    for i in range(n - 1):
        exchange.append(inlt())

    for i in range(n - 1):
        a, b = exchange[i]
        s[i + 1] += (s[i] // a) * b

    print(s[-1])
    return


if __name__ == '__main__':
    t = 1
    for i in range(t):
        solution()
