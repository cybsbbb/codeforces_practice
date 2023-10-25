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
    n, k = inlt()
    s = insr()
    cnt = collections.Counter(s)
    odd = 0
    for key, val in cnt.items():
        if val % 2 == 1:
            odd += 1

    if odd - k > 1:
        print("NO")
    else:
        print("YES")
    return 0


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
