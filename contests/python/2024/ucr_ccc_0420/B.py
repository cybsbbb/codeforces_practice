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
    n, c, d = inlt()
    b = inlt()
    b.sort()
    b2 = []
    for i in range(n):
        for j in range(n):
            b2.append(b[0] + c * i + d * j)
    b2.sort()
    if b == b2:
        print("YES")
    else:
        print("NO")
    return



if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
