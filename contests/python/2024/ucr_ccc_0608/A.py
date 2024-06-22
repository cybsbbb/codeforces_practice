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


def solution():
    s = input()[:-1]
    if 1 <= int(s[3:]) <= 349 and int(s[3:]) != 316:
        print("Yes")
    else:
        print("No")
    return


if __name__ == '__main__':
    t = 1
    for i in range(t):
        solution()





