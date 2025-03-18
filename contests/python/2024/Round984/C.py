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
    s = insr()
    n = len(s)
    cnt = 0
    magic = ['1', '1', '0', '0']
    for i in range(n - 3):
        if s[i:i + 4] == magic:
            cnt += 1
    q = inp()
    for _ in range(q):
        i, v = inlt()
        i -= 1
        for j in range(4):
            if 0 <= i - j < n - 3 and s[i - j:i - j + 4] == magic:
                cnt -= 1
        s[i] = str(v)
        for j in range(4):
            if 0 <= i - j < n - 3 and s[i - j:i - j + 4] == magic:
                cnt += 1
        print("YES" if cnt > 0 else "NO")
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
