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
    for i in range(n - 2):
        if a[i] < 0:
            print("NO")
            return
        else:
            a[i + 1] -= a[i] * 2
            a[i + 2] -= a[i]
            a[i] -= a[i]
    if a[-1] == 0 and a[-2] == 0:
        print("YES")
    else:
        print("NO")
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
