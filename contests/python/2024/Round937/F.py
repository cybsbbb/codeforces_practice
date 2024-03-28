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
    a, b, c = inlt()
    n = a + b + c
    if 2 * a + b != n - 1:
        print(-1)
        return
    cur_leaf = c
    ans = b // c
    b %= c
    while a > 0 or b > 0:
        if b > 0:
            a -= (cur_leaf - b) // 2
            cur_leaf = b + (cur_leaf - b + 1) // 2
            b = 0
        else:
            a -= cur_leaf // 2
            cur_leaf = (cur_leaf + 1) // 2
        ans += 1

    print(ans)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
