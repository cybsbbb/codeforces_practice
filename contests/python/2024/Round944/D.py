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
    length = []
    cur_len = 1
    pre_c = s[0]
    for i in range(1, len(s)):
        if s[i] == pre_c:
            cur_len += 1
        else:
            length.append(cur_len)
            pre_c = s[i]
            cur_len = 1
    length.append(cur_len)
    res = len(length)
    if s[0] == '0' and len(length) >= 2:
        res -= 1
    if s[0] == '1' and len(length) >= 3:
        res -= 1
    print(res)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()





