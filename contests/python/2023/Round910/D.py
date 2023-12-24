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
    b = inlt()
    ans = 0
    for i in range(n):
        ans += abs(a[i] - b[i])
        if a[i] > b[i]:
            a[i], b[i] = b[i], a[i]

    ans += max(0, 2 * (max(a) - min(b)))
    print(ans)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
