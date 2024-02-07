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
    a, m, l, r = inlt()
    kl = (l - a) // m
    if (a + kl * m) < l:
        kl += 1
    kr = (r - a) // m
    if (a + kr * m) > r:
        kr -= 1

    ans = kr - kl + 1
    print(ans)
    return


if __name__ == '__main__':
    t = 1
    for i in range(t):
        solution()
