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
    n, x = inlt()
    a = [0] + inlt()
    ans = 0
    for i in range(1, n+1):
        ans = max(ans, a[i] - a[i - 1])
    ans = max(ans, 2 * (x - a[-1]))
    print(ans)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
