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


r, g, b = inlt()
c = input()[:-1]
if c == 'Red':
    print(min(g, b))
elif c == 'Green':
    print(min(r, b))
elif c == 'Blue':
    print(min(r, g))
