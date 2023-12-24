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
    n, m = inlt()
    if m == 1:
        print(0)
        for _ in range(n):
            print(0)
        return
    base_perm = list(range(m))
    if n >= m - 1:
        print(m)
        for i in range(1, m):
            print(*(base_perm[i:] + base_perm[:i]))
        for i in range(n - (m - 1)):
            print(*(base_perm[1:] + base_perm[:1]))
    else:
        print(n+1)
        for i in range(1, n+1):
            print(*(base_perm[i:] + base_perm[:i]))

    return




if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
