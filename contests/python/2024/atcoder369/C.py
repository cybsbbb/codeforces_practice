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


n = inp()
a = inlt()
if n == 1:
    print(1)
else:
    ans = 3
    pre_len = 2
    pre_diff = a[1] - a[0]
    for i in range(2, n):
        if a[i] - a[i-1] == pre_diff:
            pre_len += 1
        else:
            pre_len = 2
            pre_diff = a[i] - a[i-1]
        ans += pre_len
    print(ans)
