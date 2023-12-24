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
    n, m = inlt()
    x = input()[:-1]
    s = input()[:-1]

    ans = -1
    for i in range(10):
        if s in x:
            ans = i
            break
        x += x
    print(ans)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
