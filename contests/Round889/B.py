

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
    res = 1
    cur_num = 2

    while n % cur_num == 0:
        res += 1
        cur_num += 1

    print(res)
    return 0




if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
