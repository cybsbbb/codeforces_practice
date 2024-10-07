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

def solve():
    n = inp()
    a = inlt()
    max_diff = 0
    ans = 0
    cur = a[0]
    for num in a[1:]:
        if num < cur:
            ans += cur - num
            max_diff = max(max_diff, cur - num)
        else:
            cur = num
    print(ans + max_diff)
    return




t = inp()
for _ in range(t):
    solve()
