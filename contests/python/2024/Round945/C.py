import collections
import sys
import heapq
import math

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
    p = inlt()

    is_odd = True

    ans = [0] * n
    odd = []
    even = []
    for i in range(n):
        if i % 2 == 1:
            odd.append([p[i], i])
        else:
            even.append([p[i], i])
        if p[i] == n:
            if i % 2 == 1:
                is_odd = True
            else:
                is_odd = False
    odd.sort(reverse=True)
    even.sort(reverse=True)

    less = list(range(1, n // 2 + 1))
    large = list(range(n // 2 + 1, n + 1))

    if is_odd is True:
        for i in range(n // 2):
            ans[odd[i][1]] = large[i]
            ans[even[i][1]] = less[i]
    else:
        for i in range(n // 2):
            ans[odd[i][1]] = less[i]
            ans[even[i][1]] = large[i]

    print(*ans)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()





