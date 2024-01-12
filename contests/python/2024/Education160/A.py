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
    s = input()[:-1]
    for i in range(1, len(s)):
        if int(s[:i]) < int(s[i:]) and s[i] != '0':
            print(int(s[:i]), int(s[i:]))
            return
    print(-1)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
