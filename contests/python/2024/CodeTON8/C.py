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
    n, x, y = inlt()
    a = inlt()
    a.sort()
    ans = x - 2
    for i in range(len(a) - 1):
        if a[i + 1] - a[i] == 2:
            ans += 1
    if a[0] + n - a[-1] == 2:
        ans += 1

    print(ans)
    return




if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
