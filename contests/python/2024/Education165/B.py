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


t = inp()
for _ in range(t):
    s = input()[:-1]
    n = len(s)
    idxs = []
    one = 0
    ans = 0
    for i in range(n):
        if s[i] == '1':
            one += 1
        else:
            if one > 0:
                ans += one + 1
    print(ans)


