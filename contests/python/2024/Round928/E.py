import collections
import sys

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


for i in range(inp()):
    n, k = inlt()
    cur_len = 1
    while (n - cur_len) // (cur_len * 2) + 1 < k:
        k -= ((n - cur_len) // (cur_len * 2) + 1)
        cur_len = cur_len * 2
    print(cur_len + (k - 1) * cur_len * 2)

