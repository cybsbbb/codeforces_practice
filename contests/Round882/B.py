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
    res = 0
    tmp = -1
    for num in a:
        tmp = tmp & num
        if tmp == 0:
            res += 1
            tmp = -1

    if res == 0:
        print("1")
    else:
        print(res)

    return 0



if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
