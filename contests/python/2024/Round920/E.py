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


def solution():
    h, w, xa, ya, xb, yb = inlt()
    if xa >= xb:
        print("Draw")
        return
    else:
        dx = xb - xa
        # Alice Chance
        if dx % 2 == 1:
            if abs(ya - yb) <= 1:
                print("Alice")
                return
            if ya < yb and (w - ya) <= (dx // 2 + 1):
                print("Alice")
                return
            if ya > yb and (ya - 1) <= (dx // 2 + 1):
                print("Alice")
                return
        # Bob Chance
        else:
            if abs(ya - yb) == 0:
                print("Bob")
                return
            if yb < ya and (w - yb) <= (dx // 2):
                print("Bob")
                return
            if yb > ya and (yb - 1) <= (dx // 2):
                print("Bob")
                return
        print("Draw")
        return
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
