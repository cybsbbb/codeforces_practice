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
    a = [0] + inlt()
    ans = []
    positions = [-1] * (n + 1)
    for i in range(1, n + 1):
        positions[a[i]] = i

    for i in range(1, n + 1):
        if positions[i] != i:
            ans.append((i, positions[i]))
            a[i], a[positions[i]] = a[positions[i]], a[i]
            positions[a[positions[i]]] = positions[i]
            positions[a[i]] = i

    print(len(ans))
    for i in range(len(ans)):
        print(*ans[i])
    return




if __name__ == '__main__':
    t = 1
    for i in range(t):
        solution()





