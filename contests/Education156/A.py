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
    n = inp()
    if n % 3 == 1:
        if n < 7:
            print("NO")
            return
        else:
            print("YES")
            print(f"{1} {2} {n-3}")
            return
    if n % 3 == 2:
        if n < 8:
            print("NO")
            return
        else:
            print("YES")
            print(f"{1} {2} {n-3}")
            return
    if n % 3 == 0:
        if n < 11:
            print("NO")
            return
        else:
            print("YES")
            print(f"{1} {4} {n-5}")
            return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
