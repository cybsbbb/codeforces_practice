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
    ans = n
    for b in range(2, m + 1):
        ans += (n // b + 1) // b
    print(ans)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()





