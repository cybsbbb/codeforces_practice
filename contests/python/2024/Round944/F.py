import bisect
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
    r = inp()
    upper = (r + 1) * (r + 1)
    lower = (r) * (r)
    cur_y = r
    res = 1
    for cur_x in range(1, r + 1):
        while cur_x ** 2 + cur_y ** 2 >= upper:
            cur_y -= 1
        tmp_y = cur_y
        while tmp_y > 0 and cur_x ** 2 + tmp_y ** 2 >= lower:
            res += 1
            tmp_y -= 1

    print(res * 4)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()





