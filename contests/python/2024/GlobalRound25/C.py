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
    n, m, k = inlt()
    a = inlt()
    a.sort()
    ans = k * (k - 1) // 2
    cur_idx = 0
    while k > 0:
        buy = min(k, m)
        ans += a[cur_idx] * buy
        ans -= buy * (buy - 1) // 2
        k -= buy
        cur_idx += 1
    print(ans)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
