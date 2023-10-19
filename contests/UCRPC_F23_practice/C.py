import collections
import sys
import heapq
import datetime

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
    y, m, d = inlt()
    cur_date = datetime.date(2008, 4, 28)
    inter_date = datetime.date(2001, 1, 1)
    res = (inter_date - cur_date).days
    within_year = (datetime.date(2001, m, d) - datetime.date(2001, 1, 1)).days
    res += (y - 2001) * 365 + (y - 2001) // 4 - (y - 2001) // 100 + (y - 2001) // 400
    res += within_year
    if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
        if m > 2 or (m == 2 and d == 29):
            res += 1
    print(res)
    return


if __name__ == '__main__':
    # t = inp()
    for i in range(1):
        solution()
