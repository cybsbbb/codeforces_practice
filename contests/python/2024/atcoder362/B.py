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


xa, ya = inlt()
xb, yb = inlt()
xc, yc = inlt()

xab, yab = xa - xb, ya - yb
xac, yac = xa - xc, ya - yc
xbc, ybc = xb - xc, yb - yc

if xab * xac + yab * yac == 0 or xab * xbc + yab * ybc == 0 or xac * xbc + yac * ybc == 0:
    print("Yes")
else:
    print("No")

