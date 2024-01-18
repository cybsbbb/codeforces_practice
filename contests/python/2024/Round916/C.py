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
    a = inlt()
    b = inlt()
    max_b = 0
    sum_a = 0
    ans = 0
    for i in range(min(k, n)):
        sum_a += a[i]
        max_b = max(max_b, b[i])
        ans = max(ans, sum_a + (k - i - 1) * max_b )
    print(ans)
    return ans


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
