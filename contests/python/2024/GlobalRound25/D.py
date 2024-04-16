import sys
import collections
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
    n, k = inlt()

    if n == k:
        print("YES")
        print(1)
        print(1)
        return

    if k > (n + 1) // 2:
        print("NO")
        return
    else:
        print("YES")
        print(2)
        print(n - (k - 1), 1)
        return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
