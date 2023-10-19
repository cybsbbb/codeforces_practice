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
    a = inlt()
    bucket = set()
    bucket.add(0)
    res = 0
    tmp = 0
    for num in a:
        tmp = tmp ^ num
        for pre_num in bucket:
            res = max(res, tmp ^ pre_num)
        bucket.add(tmp)
    print(res)
    return 0


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
