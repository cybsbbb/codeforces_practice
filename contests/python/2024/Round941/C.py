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
for i in range(t):
    n = inp()
    s = input()[:-1]
    min_val = 0
    max_val = 0
    cur_val = 0

    for c in s:
        if (cur_val % 2 == 0) == (c == '1'):
            cur_val += 1
        else:
            cur_val -= 1

        min_val = min(min_val, cur_val)
        max_val = max(max_val, cur_val)

    print(max_val - min_val)
