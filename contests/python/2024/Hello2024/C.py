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
    x, y = float('inf'), float('inf')
    ans = 0
    for ai in a:
        if ai <= x:
            x = ai
        elif ai > y:
            ans += 1
            x = ai
        else:
            y = ai
        if x > y:
            x, y = y, x
    print(ans)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()