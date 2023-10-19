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
    n, m, h = inlt()

    t = []
    for i in range(n):
        t.append(inlt())
    res = 1
    Rudolf_point, Rudolf_penalty = get_point_penalty(t[0], h)

    for times in t[1:]:
        tmp_point, tmp_penalty = get_point_penalty(times, h)
        if tmp_point > Rudolf_point:
            res += 1
        elif tmp_point == Rudolf_point and Rudolf_penalty > tmp_penalty:
            res += 1

    print(res)
    return



if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
