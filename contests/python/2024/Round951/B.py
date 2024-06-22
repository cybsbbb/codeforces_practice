
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
    x, y = inlt()
    x_bin = bin(x)[2:].zfill(32)[::-1]
    y_bin = bin(y)[2:].zfill(32)[::-1]
    for i in range(32):
        if x_bin[i] != y_bin[i]:
            print(1 << i)
            return
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()





