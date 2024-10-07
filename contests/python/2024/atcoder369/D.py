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
cur_even = 0
cur_odd = float('-inf')
for ai in a:
    nxt_odd = max(cur_odd, cur_even + ai)
    nxt_even = max(cur_even, cur_odd + ai * 2)
    cur_odd, cur_even = nxt_odd, nxt_even

print(max(cur_even, cur_odd))
