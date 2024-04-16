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
    a11 = b[0]
    e = []
    for i in range(n):
        for j in range(n):
            e.append(a11 + i * c + j * d)
    e.sort()

    if b == e:
        print("YES")
    else:
        print("NO")
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
