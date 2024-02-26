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
    a = inlt()
    ones = a.count(1)
    left = 0
    right = n - 1
    while a[left] == 0:
        left += 1
    while a[right] == 0:
        right -= 1
    print(right - left + 1 - ones)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
