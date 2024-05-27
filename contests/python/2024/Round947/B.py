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
    a.sort()
    first = a[0]
    second = -1
    for i in range(1, n):
        if a[i] % first == 0:
            continue
        else:
            if second != -1:
                if a[i] % second == 0:
                    continue
                else:
                    print("No")
                    return
            else:
                second = a[i]

    print("Yes")
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()





