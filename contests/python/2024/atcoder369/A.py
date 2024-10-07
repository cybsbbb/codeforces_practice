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


a, b = inlt()
if a == b:
    print(1)
elif abs(a - b) % 2 == 0:
    print(3)
else:
    print(2)
