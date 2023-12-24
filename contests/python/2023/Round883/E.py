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


def get_point_penalty(times, h):
    point = 0
    penalty = 0
    tmp_time = 0
    for ti in sorted(times):
        tmp_time += ti
        if tmp_time <= h:
            point += 1
            penalty += tmp_time
        else:
            break
    return point, penalty


def solution():
    n = inp()
    power = 2
    while(True):
        k = int(math.pow(n, 1/power))
        if k <= 1:
            break
        tmp = 1
        res = 0
        for i in range(power+1):
            res += tmp
            tmp *= k
        if res == n:
            print("Yes")
            return 0
        power += 1
    print("No")
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
