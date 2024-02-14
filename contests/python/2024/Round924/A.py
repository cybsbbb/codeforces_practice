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
    if a > b:
        a, b = b, a
    if a % 2 == 0:
        print("Yes")
        return
    if b % 2 == 0 and b // 2 != a:
        print("Yes")
        return
    print("No")
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
