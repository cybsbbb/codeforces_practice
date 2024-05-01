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
    if n == 1:
        print(k)
    else:
        ans = []
        first = 1
        while (first << 1) - 1 <= k:
            first <<= 1
        first -= 1
        second = k - first
        ans.append(first)
        ans.append(second)
        ans += [0] * (n - 2)
        print(*ans)
        return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
