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
    upper_bound = float('inf')
    lower_bound = float('-inf')
    type3 = set()
    for _ in range(n):
        a, x = inlt()
        if a == 1:
            lower_bound = max(lower_bound, x)
        if a == 2:
            upper_bound = min(upper_bound, x)
        if a == 3:
            type3.add(x)

    if lower_bound > upper_bound:
        print(0)
        return
    ans = upper_bound - lower_bound + 1
    for x in list(type3):
        if lower_bound <= x <= upper_bound:
            ans -= 1
    print(ans)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
