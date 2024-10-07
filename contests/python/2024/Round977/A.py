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
    n = inp()
    a = inlt()
    a.sort(reverse=True)
    while len(a) > 1:
        num1 = a.pop()
        num2 = a.pop()
        a.append((num1 + num2) // 2)
    print(a[0])
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
