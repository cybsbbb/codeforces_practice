
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
    s = insr()
    cnt = collections.Counter(s)
    max_cnt = max(cnt.values())
    if max_cnt <= n // 2:
        ans = n - (n // 2) * 2
    else:
        ans = n - (n - max_cnt) * 2
    print(ans)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
