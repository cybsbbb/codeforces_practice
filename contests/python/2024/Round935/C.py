import collections
import sys
import math
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
    a = input()[:-1]
    prefix = [0]
    for i in range(n):
        prefix.append(prefix[-1] + int(a[i]))
    tot_right = prefix[-1]
    res = -1
    res_dis = n
    for i in range(n + 1):
        left_cnt = i
        left_satisfied = left_cnt - prefix[i]
        right_cnt = n - i
        right_satisfied = tot_right - prefix[i]
        if (left_cnt == 0 or left_satisfied >= (left_cnt + 1) // 2) and (right_cnt == 0 or right_satisfied >= (right_cnt + 1) // 2):
            dist = abs(n / 2 - i)
            if dist < res_dis:
                res = i
                res_dis = dist
    print(res)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
