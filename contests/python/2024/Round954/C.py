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
    n, m = inlt()
    s = list(input()[:-1])
    ind = inlt()
    c = list(input()[:-1])
    c_uniqle = sorted(list(set(ind)))
    c.sort()
    for i in range(len(c_uniqle)):
        s[c_uniqle[i] - 1] = c[i]
    print(''.join(s))
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()





