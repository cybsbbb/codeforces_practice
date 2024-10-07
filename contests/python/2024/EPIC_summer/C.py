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
    h = inlt()
    cur_time = 0
    for hi in h[::-1]:
        cur_time = max(hi, cur_time + 1)
    print(cur_time)
    return


t = inp()
for _ in range(t):
    solve()
