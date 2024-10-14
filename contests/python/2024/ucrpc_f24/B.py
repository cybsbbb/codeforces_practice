import collections
import sys
import heapq
import math

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

e1 = (list(map(float, input().split())))
e2 = (list(map(float, input().split())))
s = (list(map(float, input().split())))
diff = (list(map(float, input().split())))

e1.sort()
e2.sort()
s.sort()

ans = (e1[1] + e2[1] + sum(s[1:-1])) * 0.6 * diff[0]
print(f'{ans:.1f}')
