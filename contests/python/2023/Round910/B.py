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
    ans = 0
    pre_val = a[-1]
    for i in range(n-1)[::-1]:
        if a[i] <= pre_val:
            pre_val = a[i]
            continue
        else:
            number = (a[i] - 1) // pre_val + 1
            ans += (number - 1)
            pre_val = a[i] // number
    print(ans)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
