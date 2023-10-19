
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
    n = n - m * (n // m)
    res = 0

    cnt = 0
    while n != 0 and cnt < 1000:
        if m % 2 == 1:
            print(-1)
            return
        res += n
        n = n * 2
        n = n - m * (n // m)
        cnt += 1

    if n == 0:
        print(res)
    else:
        print(-1)
    return 0


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
