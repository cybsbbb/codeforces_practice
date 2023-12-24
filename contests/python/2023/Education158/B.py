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
    c = inlt()
    ans = 0
    cur_val = c[0]
    for i in range(1, n):
        if c[i] >= cur_val:
            cur_val = c[i]
        else:
            ans += (cur_val - c[i])
            cur_val = c[i]
    ans += cur_val - 1
    print(ans)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
