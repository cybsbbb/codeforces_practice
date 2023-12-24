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
    s = insr()
    first_a = -1
    last_b = -1
    for i in range(n):
        if s[i] == 'A':
            first_a = i
            break

    for i in range(n)[::-1]:
        if s[i] == 'B':
            last_b = i
            break

    if first_a == -1 or last_b == -1:
        print(0)
        return
    else:
        print(max(0, last_b - first_a))
        return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
