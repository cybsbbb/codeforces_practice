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
    n, c = inlt()
    a = inlt()
    a[0] += c
    max_val = max(a)
    found = False
    prefix = 0
    ans = []
    for i in range(n):
        if a[i] == max_val and found is False:
            found = True
            ans.append(0)
        else:
            cur_val = a[i] + prefix
            if cur_val >= max_val:
                ans.append(i)
            else:
                ans.append(i + 1)
        prefix += a[i]
    print(*ans)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()





