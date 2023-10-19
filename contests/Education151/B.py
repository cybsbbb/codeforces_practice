import collections
import sys
import math
input = sys.stdin.readline

def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))


def solution():
    xa, ya = inlt()
    xb, yb = inlt()
    xc, yc = inlt()

    dxb, dyb = xb - xa, yb - ya
    dxc, dyc = xc - xa, yc - ya

    res = 1
    if dxb * dxc > 0:
        res += min(abs(dxb), abs(dxc))
    if dyb * dyc > 0:
        res += min(abs(dyb), abs(dyc))

    print(res)


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
