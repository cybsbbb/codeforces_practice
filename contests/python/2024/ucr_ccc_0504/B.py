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
    a = input()[:-1]
    b = input()[:-1]
    cur_a_idx = 0
    for i in range(m):
        if cur_a_idx < n and b[i] == a[cur_a_idx]:
            cur_a_idx += 1
    print(cur_a_idx)



if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()




