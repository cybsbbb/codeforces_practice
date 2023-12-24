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
    n, d, h = inlt()
    y = inlt()
    res = 0
    for i in range(1, n):
        x = y[i] - y[i-1]
        if x >= h:
            res += d * h / 2
        else:
            res += (2*h - x)*d*x / (h*2)
    res += d * h / 2
    print(res)
    return



if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
