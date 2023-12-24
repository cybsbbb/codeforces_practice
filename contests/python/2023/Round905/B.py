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
    n, k = inlt()
    a_list = inlt()
    if k == 2:
        is_even = False
        for a in a_list:
            if a % 2 == 0:
                is_even = True
                break
        if is_even is True:
            print(0)
            return
        else:
            print(1)
            return
    if k == 3:
        res = 2
        for a in a_list:
            res = min(res, (3 - a % 3) % 3)
        print(res)
        return
    if k == 4:
        even_cnt = 0
        odd_cnt = 0
        res = 4
        for a in a_list:
            if a % 2 == 0:
                even_cnt += 1
            else:
                odd_cnt += 1
            res = min(res, (4 - a % 4) % 4)
        if even_cnt >= 2:
            res = 0
        if even_cnt == 1 and odd_cnt > 0:
            res = min(res, 1)
        if odd_cnt >= 2:
            res = min(res, 2)
        print(res)
        return
    if k == 5:
        res = 5
        for a in a_list:
            res = min(res, (5 - a % 5) % 5)
        print(res)
        return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
