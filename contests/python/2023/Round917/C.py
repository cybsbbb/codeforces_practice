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
    n, k, d = inlt()
    a = inlt()
    v = inlt()
    ans = 0
    for i in range(min(d, 2 * n + 2)):
        tmp = 0
        for j in range(n):
            if a[j] == j + 1:
                tmp += 1
        for j in range(v[i % len(v)]):
            a[j] += 1
        ans = max(ans, tmp + (d - i - 1) // 2)
    print(ans)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
