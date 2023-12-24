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
    suffix_sum = [0]
    for i in range(n)[::-1]:
        suffix_sum.append(suffix_sum[-1] + a[i])
    suffix_sum = suffix_sum[::-1]
    ans = 0
    for i in range(n)[::-1]:
        if suffix_sum[i + 1] > 0:
            ans += suffix_sum[i+1]
        ans += a[i]
    print(ans)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
