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
    a = inlt()
    cnt = [0] * (n + 1)

    ans = 0
    cur_max = 0
    a1 = [0] * n
    for i in range(n):
        ai = a[i]
        ans += ai
        if cnt[ai] > 0:
            cur_max = max(cur_max, ai)
        cnt[ai] += 1
        a1[i] = cur_max

    ans += sum(a1)

    last = 0
    for i in range(1, n):
        if a1[i] == a1[i - 1]:
            last = max(last, a1[i])
        ans += last * (n - i)

    print(ans)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()





