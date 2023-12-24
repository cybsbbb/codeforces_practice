
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
    n, m, k = inlt()
    a = inlt()
    b = inlt()
    a_min = min(a)
    a_max = max(a)
    b_min = min(b)
    b_max = max(b)
    a_sum = sum(a)

    if a_min <= b_min and a_max >= b_max:
        if k % 2 == 1:
            print(a_sum + b_max - a_min)
        else:
            print(a_sum + b_max - a_min - a_max + a_min)
    elif a_min >= b_min and a_max >= b_max:
        if a_min > b_max:
            if k % 2 == 1:
                print(a_sum)
            else:
                print(a_sum - a_max + b_min)
        else:
            if k % 2 == 1:
                print(a_sum + b_max - a_min)
            else:
                print(a_sum + b_max - a_min - a_max + b_min)
    elif a_min <= b_min and a_max <= b_max:
        if k % 2 == 1:
            print(a_sum + b_max - a_min)
        else:
            print(a_sum)
    elif a_min > b_min and a_max < b_max:
        if k % 2 == 1:
            print(a_sum + b_max - a_min)
        else:
            print(a_sum + b_max - a_min - b_max + b_min)

    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
