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
if a == 1 and b == 0:
    print("Yes")
elif a == 0 and b == 1:
    print("No")
else:
    print("Invalid")
